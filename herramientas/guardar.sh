#!/usr/bin/env bash
# Guarda A MEDIAS el trabajo de los ayudantes en curso, por si se corta la
# sesión: commit y push de biblia.md / informe.md, referencias.json /
# recursos.json y hojas/ (JPEG de menos de 3 MB) de cada carpeta con cambios.
# NO marca casillas en TANDAS.md: eso lo hace herramientas/subir.sh al terminar.
#   herramientas/guardar.sh            # una vez
#   herramientas/guardar.sh --cada 600 # en bucle, cada 10 minutos
set -uo pipefail
cd "$(dirname "$0")/.."

guardar() {
  exec 9>"${TMPDIR:-/tmp}/subir-sintonizando.lock"
  flock 9
  local rama; rama="$(git rev-parse --abbrev-ref HEAD)"
  local dirs
  dirs=$(git status --porcelain --untracked-files=all -- biblias investigaciones \
    | sed -E 's/^.. //' | cut -d/ -f1-2 | sort -u)
  local n=0
  for d in $dirs; do
    [[ -d "$d" ]] || continue
    for f in "$d"/biblia.md "$d"/informe.md "$d"/referencias.json "$d"/recursos.json; do
      [[ -f "$f" ]] && git add -- "$f" && n=$((n+1))
    done
    if [[ -d "$d/partes" ]]; then
      while IFS= read -r -d '' p; do git add -- "$p"; done \
        < <(find "$d/partes" -type f \( -name '*.md' -o -name '*.json' \) -size -3M -print0)
    fi
    if [[ -d "$d/hojas" ]]; then
      while IFS= read -r -d '' h; do git add -- "$h"; done \
        < <(find "$d/hojas" -type f -iname '*.jpg' -size -3M -print0)
    fi
  done
  if git diff --cached --quiet; then
    flock -u 9; return 0
  fi
  local lista; lista=$(git diff --cached --name-only | cut -d/ -f2 | sort -u | tr '\n' ' ')
  git commit -q -m "Guardado a medias: ${lista% }" -m "Trabajo sin terminar de los ayudantes, guardado por si se corta la sesion. Las casillas de TANDAS.md siguen sin marcar.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01U6fqU42CgJnv7MUVUDWeSF"
  for espera in 0 2 4 8 16; do
    sleep "$espera"
    if git push -q -u origin "$rama" 2>/dev/null; then
      echo "$(date -u +%H:%M) guardado: ${lista% }"; flock -u 9; return 0
    fi
  done
  echo "$(date -u +%H:%M) ERROR: el push falló 5 veces (commit hecho en local)"
  flock -u 9; return 1
}

if [[ "${1:-}" == "--cada" ]]; then
  while true; do sleep "${2:-600}"; guardar; done
else
  guardar
fi
