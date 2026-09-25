#!/usr/bin/env bash
# Una vuelta del jefe de un lote en una máquina de GitHub Actions (la lanza
# .github/workflows/lote.yml). Trabaja ~5 h 20, lo deja todo guardado y la
# vuelta siguiente sigue desde lotes/<L>.md.
#   herramientas/motor_github.sh G
#
# El jefe va en una terminal virtual (tmux) y no con `claude -p`: lanza a sus
# ayudantes en segundo plano y espera sus avisos, como en la caja de la PC.
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
echo "Lote $L en $rama (desde $desde)"

herramientas/guardar.sh --cada 300 &
guardador=$!

msg="Eres el jefe del lote $L, en una máquina de GitHub Actions (Ubuntu) que va con MWAPI. Esta vuelta dura unas 5 horas; al acabar se guarda todo y otra máquina sigue desde lo que haya en GitHub.
1. Ya estás en la rama $rama. Corre herramientas/juntar.sh (el .lote ya dice $L).
2. Lee REPARTO.md y lotes/$L.md y sigue con la skill serie-en-equipo sólo con tu lote (python3 herramientas/siguiente.py 5 --lote $L), en cadena, desde lo que dice lotes/$L.md. Relanza primero lo que quedó cortado (partes con «Sigue:» o a medias, redactores sin cerrar).
Aquí las herramientas ya están instaladas y herramientas/guardar.sh --cada 300 ya corre: no instales nada ni lo lances otra vez. No hay send_later ni enlace de sesión: sáltate esos pasos. /home/user/sintonizando-investigacion apunta a este repo. Apunta en lotes/$L.md el estado, los avisos y los tokens de cada agente al cerrar cada serie. No escribas correos de cuentas en ningún archivo. No toques ESTADO.md, DECISIONES.md, COSTOS.md ni TANDAS.md."

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

lanzar "$msg"
atender_dialogos
inicio=$(date +%s); ultima_foto=0; relanzadas=0
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
    ultima_foto=$(date +%s)
    echo "── $(date -u +%H:%M) pantalla del jefe ──"
    tmux capture-pane -p -t jefe 2>/dev/null | grep -v '^[[:space:]]*$' | tail -25
  fi
done

echo "── fin de la vuelta: guardo ──"
tmux kill-session -t jefe 2>/dev/null
kill "$guardador" 2>/dev/null
sleep 3
herramientas/guardar.sh
# Sólo se encadena la vuelta siguiente si ésta trabajó de verdad: con la llave
# mal puesta el jefe muere enseguida y no hay que encadenar vueltas vacías.
(( $(date +%s) - inicio >= 1800 )) && touch /tmp/vuelta-ok

# ── consumo de la vuelta, a la página del run ──
python3 - <<'PY' | tee -a "${GITHUB_STEP_SUMMARY:-/dev/null}"
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
print("### Consumo de esta vuelta\n")
print("| modelo | respuestas | entrada | caché escrita | caché leída | salida |")
print("|---|---|---|---|---|---|")
for mod, (n, i, cc, cr, o) in sorted(por.items()):
    print(f"| {mod} | {n} | {i:,} | {cc:,} | {cr:,} | {o:,} |")
PY
