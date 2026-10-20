"""Verifica os vínculos mínimos da especialização sem depender do Hermes."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "AGENTS.md", "agent/persona.md",
    "agent/knowledge/security-basics.md",
    "skills/vulnerability-analysis/SKILL.md",
    "skills/vulnerability-analysis/README.md",
    "templates/relatorio-vulnerabilidade.md", "app.py",
    "examples/app_vulneravel.py", "tests/test_login.py",
    "tools/validar_lab.py", "docs/hermes-appsec.md",
    "docs/cenarios-appsec.md", "docs/analise-sqli.md",
    "prompts/01-contexto-servidor.txt", "prompts/02-revisao-sqli.txt",
    "prompts/03-reteste.txt", "evidencias/README.md", "ENTREGA-DIO.md",
]


def main():
    for name in REQUIRED:
        assert (ROOT / name).is_file(), f"Arquivo ausente: {name}"
        assert (ROOT / name).read_text(encoding="utf-8").strip(), f"Arquivo vazio: {name}"
    skill = (ROOT / "skills/vulnerability-analysis/SKILL.md").read_text(encoding="utf-8")
    assert skill.startswith("---\n")
    frontmatter = skill.split("---", 2)[1]
    assert re.search(r"^name: vulnerability-analysis$", frontmatter, re.M)
    assert re.search(r"^description: .+", frontmatter, re.M)
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    assert "skills/vulnerability-analysis/SKILL.md" in agents
    assert "security-basics.md" in agents
    assert "AppSec" in (ROOT / "agent/persona.md").read_text(encoding="utf-8")
    assert "vulnerability-analysis" in (ROOT / "skills/README.md").read_text(encoding="utf-8")
    print(f"OK: {len(REQUIRED)} arquivos não vazios; frontmatter, conhecimento, persona e registro conferidos.")


if __name__ == "__main__":
    main()

