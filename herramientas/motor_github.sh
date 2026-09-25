#!/usr/bin/env bash
# Una vuelta del jefe de un lote en una máquina de GitHub Actions (la lanza
# .github/workflows/lote.yml), con la suscripción Max del dueño (el secreto
# CLAUDE_CODE_OAUTH_TOKEN). Trabaja ~5 h 20, lo deja todo guardado y la vuelta
# siguiente sigue desde lotes/<L>.md.
#   herramientas/motor_github.sh G
#
# El jefe va en una terminal virtual (tmux) y no con `claude -p`: lanza a sus
# ayudantes en segundo plano y espera sus avisos, como en la caja de la PC.
# Cada 10 minutos se mira su pantalla y:
#   - límite de 5 horas de la Max («continuing automatically at …»): Claude
#     Code espera y sigue solo; no se toca nada;
#   - límite semanal o que tarda más de 24 h en recargarse: la vuelta termina
#     antes y no encadena otra; el cron de lote.yml lo reintenta cada 3 h;
#   - jefe parado 20 minutos sin nada en marcha: se le dice que siga.
set -uo pipefail

# Se copia a /tmp antes de nada: al cambiar a la rama del lote este archivo
# puede desaparecer del disco, y bash lo va leyendo mientras corre.
if [[ "$0" != /tmp/motor_github.sh ]]; then
  cp "$0" /tmp/motor_github.sh
  exec bash /tmp/motor_github.sh "$@"
fi
cd "${GITHUB_WORKSPACE:?corre dentro de GitHub Actions}"

L="${1:?falta la letra del lote}"; L="${L^^}"; l="${L,,}"
LIMITE="${LIMITE:-19200}"   # segundos de jefe por vuelta (5 h 20)
rama="claude/lote-$l-local"
resumen="${GITHUB_STEP_SUMMARY:-/dev/null}"
: "${CLAUDE_CODE_OAUTH_TOKEN:?falta el secreto CLAUDE_CODE_OAUTH_TOKEN}"

# ── el pase de la Max: si no vale, se para aquí y no se encadenan vueltas vacías ──
timeout 180 claude -p "Contesta sólo con la palabra: ok" --model sonnet >/tmp/prueba-pase.txt 2>&1
rc=$?
respuesta=$(head -c 300 /tmp/prueba-pase.txt | tr '\n' ' ')
if (( rc == 0 )); then
  echo "Pase de la Max: bien (respondió: ${respuesta:0:40})"
elif grep -qiE 'usage limit|limit reached|hit your limit|rate.?limit|429' /tmp/prueba-pase.txt; then
  echo "::warning::Lote $L: la cuenta Max está en su límite de uso ahora mismo; el jefe arranca y espera a que se recargue."
elif grep -qiE 'run /login|not logged in|invalid api key|authentication|401|403|expired|revoked' /tmp/prueba-pase.txt; then
  echo "::error::Lote $L: el pase de la Max no vale (mal pegado, caducado o revocado). En la PC: doble clic en «MAX EN GITHUB» y pega el pase nuevo. Respuesta: $respuesta"
  exit 1
else
  echo "::warning::Lote $L: no pude comprobar el pase (código $rc); sigo igual. Respuesta: $respuesta"
fi

# ── rama del lote: la suya, o la de la nube que tocó lotes/<L>.md por última vez ──
git fetch -q origin '+refs/heads/*:refs/remotes/origin/*'
if git show-ref -q "refs/remotes/origin/$rama"; then
  desde="origin/$rama"
else
  desde=$(for r in $(git for-each-ref --format='%(refname:short)' refs/remotes/origin/claude/); do
            t=$(git log -1 --format=%ct "$r" -- "lotes/$L.md"); [[ -n "$t" ]] && echo "$t $r"
          done | sort -rn | awk 'NR==1{print $2}')
  desde="${desde:-origin/main}"
fi
git checkout -q -B "$rama" "$desde"
echo "$L" > .lote
sha_inicio=$(git rev-parse HEAD)
echo "Lote $L en $rama (desde $desde, $(git log -1 --format='%h %s' | cut -c1-80))"

herramientas/guardar.sh --cada 300 &
guardador=$!

fin_vuelta=$(date -u -d "@$(( $(date +%s) + LIMITE ))" +%H:%M)
msg="Eres el jefe del lote $L, en una máquina de GitHub Actions (Ubuntu) que va con la suscripción Max del dueño. Esta vuelta termina a las $fin_vuelta UTC (unas 5 horas); al acabar se guarda todo y otra máquina sigue desde lo que haya en GitHub. En los últimos 30 minutos no lances agentes nuevos: cierra lo que puedas y deja lotes/$L.md al día.
1. Ya estás en la rama $rama. Corre herramientas/juntar.sh (el .lote ya dice $L).
2. Lee REPARTO.md y lotes/$L.md y sigue con la skill serie-en-equipo sólo con tu lote (python3 herramientas/siguiente.py 5 --lote $L), en cadena. Lo que diga siguiente.py manda (mira el disco); lotes/$L.md es orientativo y puede estar viejo. Relanza primero lo que quedó cortado: modo «seguir» = sólo los roles a medias o que falten; modo «redactar» = sólo el redactor.
Aquí las herramientas ya están instaladas y herramientas/guardar.sh --cada 300 ya corre: no instales nada ni lo lances otra vez. No hay send_later ni enlace de sesión: sáltate esos pasos. /home/user/sintonizando-investigacion apunta a este repo.
Límite de uso de la Max: si ves «Usage limit reached · continuing automatically at …», no hagas nada, Claude Code sigue solo cuando se recarga. Si un ayudante falla por el límite de uso, no lo relances en bucle: relánzalo una sola vez cuando el límite se haya recargado.
Apunta en lotes/$L.md el estado, los avisos y los tokens de cada agente al cerrar cada serie. No escribas correos de cuentas en ningún archivo. No toques ESTADO.md, DECISIONES.md, COSTOS.md ni TANDAS.md. Si ya no queda ninguna serie por hacer en tu lote, escribe «LOTE $L TERMINADO» en la primera línea de lotes/$L.md, súbelo con git y para."

lanzar() { tmux new-session -d -s jefe -x 220 -y 50 claude --dangerously-skip-permissions --model sonnet "$@"; }

# Pantallas de la primera vez, por si la configuración previa no bastara.
atender_dialogos() {
  for _ in $(seq 1 30); do
    sleep 4
    p=$(tmux capture-pane -p -t jefe 2>/dev/null) || return 0
    if grep -qE "Yes, I trust this folder|Yes, I accept" <<<"$p"; then tmux send-keys -t jefe Down Enter
    elif grep -q "Choose the text style" <<<"$p"; then tmux send-keys -t jefe Enter
    fi
  done
}

# ¿Escribió algo el jefe o algún ayudante en los últimos 20 minutos?
actividad_reciente() {
  [[ -n "$(find ~/.claude/projects biblias investigaciones lotes -type f -mmin -20 -print -quit 2>/dev/null)" ]]
}

lanzar "$msg"
atender_dialogos
inicio=$(date +%s); ultima_foto=0; relanzadas=0; ultimo_empujon=0; fin_anticipado=""
while (( $(date +%s) - inicio < LIMITE )); do
  sleep 60
  if ! tmux has-session -t jefe 2>/dev/null; then
    (( relanzadas >= 6 )) && { echo "El jefe se cerró 6 veces en esta vuelta: paro"; break; }
    relanzadas=$((relanzadas + 1))
    echo "$(date -u +%H:%M) el jefe se cerró: lo sigo ($relanzadas)"
    sleep 240
    lanzar --continue "sigue"
    atender_dialogos
  fi
  if (( $(date +%s) - ultima_foto >= 600 )); then
    ultima_foto=$(date +%s); ahora=$ultima_foto
    pantalla=$(tmux capture-pane -p -t jefe 2>/dev/null | grep -v '^[[:space:]]*$' | tail -25)
    echo "── $(date -u +%H:%M) pantalla del jefe ──"
    echo "$pantalla"
    if grep -qi 'continuing automatically' <<<"$pantalla"; then
      echo "   (límite de la Max: Claude Code espera y sigue solo)"
    elif grep -qiE 'will not resume on its own|more than 24 hours|rate-limit-options' <<<"$pantalla"; then
      echo "::notice::Lote $L: la cuenta Max topó un límite que tarda en recargarse (semanal o de más de 24 h). Termino la vuelta sin encadenar otra; el cron lo reintenta cada 3 h."
      fin_anticipado="límite largo de la Max"
      break
    elif grep -qiE 'usage limit|limit reached|hit your limit|limit will reset|resets (at|in) ' <<<"$pantalla"; then
      if (( ahora - ultimo_empujon >= 1800 )); then
        ultimo_empujon=$ahora
        tmux send-keys -t jefe "sigue" Enter
        echo "   (límite de la cuenta sin espera automática: le digo que siga)"
      fi
    elif grep -qs "LOTE $L TERMINADO" "lotes/$L.md"; then
      echo "::notice::Lote $L: el jefe dice que no queda nada por hacer en su lote."
      fin_anticipado="lote terminado"
      break
    elif ! grep -q 'esc to interrupt' <<<"$pantalla" && ! actividad_reciente && (( ahora - ultimo_empujon >= 1800 )); then
      ultimo_empujon=$ahora
      tmux send-keys -t jefe "Sigue con la skill serie-en-equipo: relanza lo que quedó cortado y continúa con la siguiente serie del lote $L (python3 herramientas/siguiente.py 5 --lote $L). Si no queda nada, escribe «LOTE $L TERMINADO» en la primera línea de lotes/$L.md, súbelo y para." Enter
      echo "   (jefe parado 20 min sin nada en marcha: le digo que siga)"
    fi
  fi
done

echo "── fin de la vuelta${fin_anticipado:+ ($fin_anticipado)}: guardo ──"
tmux kill-session -t jefe 2>/dev/null
kill "$guardador" 2>/dev/null
sleep 3
# Estado real en disco al cerrar, para quien siga (lotes/<L>.md puede ir viejo).
[[ -f "lotes/$L.md" ]] && python3 herramientas/estado_lote.py "$L" "${fin_anticipado:-vuelta completa}"
herramientas/guardar.sh
grep -qs "LOTE $L TERMINADO" "lotes/$L.md" && fin_anticipado="lote terminado"
case "$fin_anticipado" in
  "lote terminado") touch /tmp/lote-terminado ;;
  "") # Sólo se encadena si esta vuelta trabajó de verdad, no si el jefe murió una y otra vez.
      (( relanzadas < 6 && $(date +%s) - inicio >= 1800 )) && touch /tmp/vuelta-ok ;;
  *)  echo "No encadeno la vuelta siguiente: $fin_anticipado." ;;
esac

# ── resumen de la vuelta, a la página del run ──
{
  echo "### Lote $L · vuelta de $(( ($(date +%s) - inicio) / 60 )) min${fin_anticipado:+ · $fin_anticipado}"
  echo
  echo "**Subido en esta vuelta** (rama \`$rama\`):"
  echo
  subido=$(git log --oneline "$sha_inicio..HEAD" 2>/dev/null | head -40)
  if [[ -n "$subido" ]]; then echo "$subido" | sed 's/^/- /'; else echo "- nada"; fi
  echo
  python3 - <<'PY'
import collections, glob, json, os
por = collections.defaultdict(lambda: [0, 0, 0, 0, 0])
for f in glob.glob(os.path.expanduser("~/.claude/projects/**/*.jsonl"), recursive=True):
    for l in open(f, encoding="utf-8", errors="replace"):
        try:
            d = json.loads(l)
        except Exception:
            continue
        m = d.get("message") or {}
        if d.get("type") != "assistant" or not m.get("model"):
            continue
        u = m.get("usage") or {}
        t = por[m["model"]]
        t[0] += 1
        t[1] += u.get("input_tokens", 0)
        t[2] += u.get("cache_creation_input_tokens", 0)
        t[3] += u.get("cache_read_input_tokens", 0)
        t[4] += u.get("output_tokens", 0)
print("**Consumo de esta vuelta** (todos los agentes de esta máquina):\n")
print("| modelo | respuestas | entrada | caché escrita | caché leída | salida |")
print("|---|---|---|---|---|---|")
for mod, (n, i, cc, cr, o) in sorted(por.items()):
    print(f"| {mod} | {n} | {i:,} | {cc:,} | {cr:,} | {o:,} |")
PY
} | tee -a "$resumen"
