#!/usr/bin/env bash
# Trozos que comparten guardar.sh, subir.sh y juntar.sh (se hace `source`).

# Pie de los commits: sin enlaces de sesiones ajenas. Si la sesión tiene enlace,
# que lo ponga en CLAUDE_SESSION_URL.
pie_commit() {
  local pie="Co-Authored-By: Claude <noreply@anthropic.com>"
  [[ -n "${CLAUDE_SESSION_URL:-}" ]] && pie+=$'\n'"Claude-Session: $CLAUDE_SESSION_URL"
  printf '%s' "$pie"
}

# Push con reintentos. Si la rama remota avanzó (otra máquina en la misma rama),
# la trae y vuelve a probar; si no hay manera, deja el trabajo en una rama
# salvavidas claude/<rama>-salvavidas-<run>, que juntar.sh recoge después.
empujar() {
  local rama="$1" espera
  for espera in 0 2 4 8 16; do
    sleep "$espera"
    git push -q -u origin "$rama" 2>/dev/null && return 0
    if git fetch -q origin "$rama" 2>/dev/null; then
      git merge -q --no-edit "origin/$rama" >/dev/null 2>&1 || true
    fi
  done
  local salva="$rama-salvavidas-${GITHUB_RUN_ID:-$(date +%s)}"
  if git push -q origin "HEAD:refs/heads/$salva" 2>/dev/null; then
    echo "AVISO: no pude subir a $rama; el trabajo queda en $salva (juntar.sh lo recoge)"
    return 0
  fi
  echo "ERROR: el push a $rama falló 5 veces y tampoco pude dejar la rama salvavidas (commit hecho en local)"
  return 1
}
