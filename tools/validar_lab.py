"""Imprime evidência reproduzível. Não acessa rede nem arquivos do usuário."""
import json
import platform
from datetime import datetime, timezone
import app
from examples import app_vulneravel


def main():
    vulnerable = app_vulneravel.create_lab_db()
    corrected = app.create_lab_db()
    try:
        checks = {
            "baseline_login_valido": app_vulneravel.authenticate(vulnerable, app.LAB_USER, app.LAB_PASSWORD),
            "baseline_senha_errada_rejeitada": not app_vulneravel.authenticate(vulnerable, app.LAB_USER, "errada"),
            "baseline_bypass_reproduzido": app_vulneravel.authenticate(vulnerable, "aluno' --", "errada"),
            "corrigido_login_valido": app.authenticate(corrected, app.LAB_USER, app.LAB_PASSWORD),
            "corrigido_senha_errada_rejeitada": not app.authenticate(corrected, app.LAB_USER, "errada"),
            "corrigido_payload_usuario_rejeitado": not app.authenticate(corrected, "aluno' --", "errada"),
            "corrigido_payload_senha_rejeitado": not app.authenticate(corrected, app.LAB_USER, "' OR '1'='1"),
        }
        print(json.dumps({
            "executado_em_utc": datetime.now(timezone.utc).isoformat(),
            "python": platform.python_version(),
            "ambiente": "SQLite em memória; sem HTTP, rede ou banco externo",
            "verificacoes": checks,
            "todas_passaram": all(checks.values()),
            "hermes_executado": False,
        }, ensure_ascii=False, indent=2))
        return 0 if all(checks.values()) else 1
    finally:
        vulnerable.close()
        corrected.close()


if __name__ == "__main__":
    raise SystemExit(main())

