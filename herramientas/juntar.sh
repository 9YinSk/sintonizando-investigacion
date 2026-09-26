#!/usr/bin/env bash
# Junta en la rama actual el trabajo de todas las cuentas (todas las ramas claude/*).
# Cada biblia vive en su carpeta, así que no chocan. Con --marcar (sólo la central)
# marca además en TANDAS.md las biblias que revisar.py da por COMPLETAS, copia lo de
# lotes/*.md a ESTADO.md, DECISIONES.md y COSTOS.md (juntar_lotes.py) y hace commit.
#   herramientas/juntar.sh
#   herramientas/juntar.sh --marcar
set -uo pipefail
cd "$(dirname "$0")/.."
source herramientas/comun.sh
rama="$(git rev-parse --abbrev-ref HEAD)"
# el mismo candado que guardar.sh: que no se mezcle mientras se hace un commit
exec 9>"${TMPDIR:-/tmp}/subir-sintonizando.lock"
flock 9
git fetch -q origin '+refs/heads/claude/*:refs/remotes/origin/claude/*' 2>/dev/null || git fetch -q origin
for r in $(git for-each-ref --format='%(refname:short)' refs/remotes/origin/claude/); do
  [[ "$r" == "origin/$rama" ]] && continue
  git merge-base --is-ancestor "$r" HEAD && continue
  if git merge -q --no-edit -m "Juntar: $r" "$r" >/dev/null 2>&1; then
    echo "juntada: $r"
  else
    en_choque=$(git diff --name-only --diff-filter=U | tr '\n' ' ')
    echo "::warning::juntar.sh: no pude juntar $r: ${en_choque:+choque en: $en_choque}${en_choque:-cambios locales sin guardar en el árbol (o error de git)} (esa rama queda sin juntar)"
    git merge --abort >/dev/null 2>&1 || true
  fi
done
if [[ "${1:-}" == "--marcar" ]]; then
  python3 - <<'PY'
import sys
sys.path.insert(0, "herramientas")
from revisar import revisar
import os
t = open("TANDAS.md", encoding="utf-8").read().split("\n")
n = 0
for i, l in enumerate(t):
    for pref in ("- [ ] repaso ", "- [ ] "):
        if l.startswith(pref):
            id = l[len(pref):].strip()
            if os.path.exists(f"biblias/{id}/biblia.md") and not revisar(id, solo_falta=True):
                if pref == "- [ ] " or "Segunda pasada · qué cambió" in open(f"biblias/{id}/biblia.md", encoding="utf-8").read():
                    t[i] = l.replace("- [ ]", "- [x]", 1); n += 1
            break
open("TANDAS.md", "w", encoding="utf-8").write("\n".join(t))
print(f"marcadas: {n}")
PY
  python3 herramientas/juntar_lotes.py
  git add TANDAS.md ESTADO.md DECISIONES.md COSTOS.md
  git diff --cached --quiet || git commit -q -m "Central: TANDAS marcadas y lotes copiados a ESTADO, DECISIONES y COSTOS" -m "$(pie_commit)"
fi
flock -u 9
empujar "$rama" && echo "subido a $rama"
