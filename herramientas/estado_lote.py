"""Deja al final de lotes/<L>.md un bloque «Para quien siga» con el estado real
en disco (siguiente.py), sustituyendo el de la vez anterior. Lo corre el motor
de GitHub al cerrar cada vuelta.

    python3 herramientas/estado_lote.py G "vuelta completa"
"""
import datetime
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def main():
    L = sys.argv[1].upper()
    motivo = sys.argv[2] if len(sys.argv) > 2 else "vuelta completa"
    p = RAIZ / "lotes" / f"{L}.md"
    t = p.read_text(encoding="utf-8")
    cola = subprocess.run([sys.executable, str(RAIZ / "herramientas" / "siguiente.py"), "6", "--lote", L],
                          capture_output=True, text=True).stdout.strip()
    hora = datetime.datetime.now(datetime.timezone.utc).strftime("%d-%m-%Y %H:%M")
    bloque = (f"<!-- motor -->\n### Para quien siga (motor de GitHub, {hora} UTC, {motivo})\n\n"
              f"Estado real en disco al cerrar la vuelta, según `siguiente.py 6 --lote {L}` "
              f"(lo de arriba puede estar viejo):\n\n```\n{cola}\n```\n<!-- /motor -->")
    if "<!-- motor -->" in t:
        t = re.sub(r"<!-- motor -->.*?<!-- /motor -->", lambda m: bloque, t, flags=re.S)
    else:
        t = t.rstrip("\n") + "\n\n" + bloque + "\n"
    p.write_text(t, encoding="utf-8")
    print(f"lotes/{L}.md: bloque «Para quien siga» al día")


if __name__ == "__main__":
    main()
