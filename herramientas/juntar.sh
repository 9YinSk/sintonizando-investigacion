#!/usr/bin/env bash
# Junta en la rama actual el trabajo de todas las cuentas (todas las ramas claude/*).
# Cada biblia vive en su carpeta, así que no chocan. Con --marcar (sólo la central)
# marca además en TANDAS.md las biblias que revisar.py da por COMPLETAS.
#   herramientas/juntar.sh
#   herramientas/juntar.sh --marcar
set -uo pipefail
cd "$(dirname "$0")/.."
rama="$(git rev-parse --abbrev-ref HEAD)"
git fetch -q origin '+refs/heads/claude/*:refs/remotes/origin/claude/*' 2>/dev/null || git fetch -q origin
for r in $(git for-each-ref --format='%(refname:short)' refs/remotes/origin/claude/); do
  [[ "$r" == "origin/$rama" ]] && continue
  git merge-base --is-ancestor "$r" HEAD && continue
  if git merge -q --no-edit -m "Juntar: $r" "$r" >/dev/null 2>&1; then
    echo "juntada: $r"
  else
    echo "CHOQUE con $r en: $(git diff --name-only --diff-filter=U | tr '\n' ' ')"; git merge --abort
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
fi
git push -q -u origin "$rama" 2>/dev/null && echo "subido a $rama"
