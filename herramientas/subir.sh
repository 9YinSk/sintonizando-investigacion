#!/usr/bin/env bash
# Sube el trabajo de UN ayudante: comprueba su carpeta, marca su casilla en
# TANDAS.md, hace commit sólo de esa carpeta y de TANDAS.md, y hace push.
#   herramientas/subir.sh 31-demon-slayer-kimetsu-no-yaiba
#   herramientas/subir.sh 01-one-piece repaso
#   herramientas/subir.sh A01-texturas
set -euo pipefail
cd "$(dirname "$0")/.."

id="${1:?falta el id del encargo}"
modo="${2:-}"
rama="$(git rev-parse --abbrev-ref HEAD)"

if [[ "$id" =~ ^[A-P][0-9]{2}- ]]; then
  dir="investigaciones/$id"; doc="$dir/informe.md"; datos="$dir/recursos.json"
else
  dir="biblias/$id"; doc="$dir/biblia.md"; datos="$dir/referencias.json"
fi

exec 9>"${TMPDIR:-/tmp}/subir-sintonizando.lock"
flock 9

# ── comprobaciones ──
[[ -f "$doc" ]] || { echo "ERROR: falta $doc"; exit 1; }
lineas=$(wc -l < "$doc")
(( lineas >= 300 )) || { echo "ERROR: $doc sólo tiene $lineas líneas"; exit 1; }
if [[ -f "$datos" ]]; then
  python3 -c "import json,sys; d=json.load(open(sys.argv[1])); assert isinstance(d,list) and d" "$datos" \
    || { echo "ERROR: $datos no es una lista JSON"; exit 1; }
  nref=$(python3 -c "import json,sys; print(len(json.load(open(sys.argv[1]))))" "$datos")
else
  echo "AVISO: falta $datos"; nref=0
fi
grandes=$(find "$dir" -type f -size +3M | wc -l)
(( grandes == 0 )) || { echo "ERROR: hay archivos de más de 3 MB:"; find "$dir" -type f -size +3M; exit 1; }
nhojas=0
if [[ -d "$dir/hojas" ]]; then
  nhojas=$(find "$dir/hojas" -type f | wc -l)
  (( nhojas <= 3 )) || { echo "ERROR: $nhojas archivos en hojas/ (máximo 3)"; exit 1; }
fi
otros=$(find "$dir" -type f ! -path "$dir/hojas/*" ! -path "$dir/partes/*" ! -name "$(basename "$doc")" ! -name "$(basename "$datos")" | wc -l)
(( otros == 0 )) || { echo "AVISO: archivos de más en $dir:"; find "$dir" -type f ! -path "$dir/hojas/*" ! -path "$dir/partes/*" ! -name "$(basename "$doc")" ! -name "$(basename "$datos")"; }

if [[ "$dir" == biblias/* ]]; then
  rev=$(python3 herramientas/revisar.py "$id")
  if [[ "$rev" != *COMPLETA* && "${FORZAR:-}" != 1 ]]; then
    echo "ERROR: revisar.py dice que no está completa (FORZAR=1 para subir igual):"; echo "$rev"; exit 1
  fi
fi

# ── casilla en TANDAS.md y mensaje del commit ──
if [[ "$modo" == "repaso" ]]; then
  casilla="- [ ] repaso $id"
else
  casilla="- [ ] $id"
fi
lote="$(cat .lote 2>/dev/null || true)"
if [[ -n "$lote" ]]; then
  echo "Lote $lote: no marco TANDAS.md (lo marca la central con juntar.sh --marcar)"
elif grep -qxF -- "$casilla" TANDAS.md; then
  python3 - "$casilla" <<'PY'
import sys
c = sys.argv[1]
t = open("TANDAS.md", encoding="utf-8").read().split("\n")
t = [l.replace("- [ ]", "- [x]", 1) if l == c else l for l in t]
open("TANDAS.md", "w", encoding="utf-8").write("\n".join(t))
PY
else
  echo "AVISO: no encontré la casilla «$casilla» (¿ya marcada?)"
fi

if [[ "$modo" == "repaso" ]]; then
  msg="Segunda pasada: repaso $id"
  quedan=$(grep -c -- "^- \[ \] repaso " TANDAS.md || true)
  resumen="repasos pendientes: $quedan"
else
  tanda=$(awk -v id="$id" '/^## Tanda /{t=$3} $0 ~ "^- \\[.\\] "id"$"{print t; exit}' TANDAS.md)
  pend=$(awk -v t="$tanda" '/^## Tanda /{f=($3==t)} f && /^- \[ \] /' TANDAS.md | wc -l)
  if (( pend == 0 )); then msg="Tanda $tanda: $id"; else msg="Tanda $tanda (parcial): $id"; fi
  resumen="pendientes en tanda: $pend"
fi
hechas=$(grep -E -c -- "^- \[x\] [^r]|^- \[x\] r[^e]" TANDAS.md || true)
repasos=$(grep -c -- "^- \[x\] repaso " TANDAS.md || true)

git add -- "$dir" TANDAS.md lotes 2>/dev/null || git add -- "$dir"
if git diff --cached --quiet; then
  echo "Nada nuevo que subir en $dir"; exit 0
fi
git commit -q -m "$msg" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01PTjYZQejJbQf4MSwH4sQbi"

for espera in 0 2 4 8 16; do
  sleep "$espera"
  if git push -q -u origin "$rama" 2>/dev/null; then
    echo "OK: $msg · $lineas lineas · $nref referencias · $nhojas hojas · $resumen · hechas $hechas de 227 · repasos $repasos de $(grep -c -- "^- \[.\] repaso " TANDAS.md)"
    exit 0
  fi
done
echo "ERROR: el push falló 5 veces (commit hecho en local)"; exit 1
