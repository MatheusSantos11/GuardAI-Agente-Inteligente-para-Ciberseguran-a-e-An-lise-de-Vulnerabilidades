"""Integra a extensão ao clone original, preservando outras skills e documentos."""
from pathlib import Path
import shutil
import sys

source = Path(__file__).resolve().parent
if len(sys.argv) != 2:
    raise SystemExit('Uso: python integrate.py CAMINHO_PARA_CLONE_DIO_AGENT')
target = Path(sys.argv[1]).resolve()
if not (target / 'AGENTS.md').is_file() or not (target / 'agent/persona.md').is_file():
    raise SystemExit('Destino inválido: esperado clone original com AGENTS.md e agent/persona.md')
for rel in ['skills/vulnerability-analysis/SKILL.md', 'skills/vulnerability-analysis/README.md', 'agent/knowledge/security-basics.md', 'examples/app.py', 'examples/app_fixed.py', 'tests/test_login.py', 'docs/APPSEC-ADDITIONS.md']:
    dst = target / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source / rel, dst)
agents = target / 'AGENTS.md'
body = agents.read_text(encoding='utf-8')
knowledge = '- `agent/knowledge/security-basics.md`: fundamentos de segurança e classificação de riscos.\n'
row = '| Análise de vulnerabilidades | precisa avaliar, classificar, corrigir ou validar riscos em código/infraestrutura autorizados | `skills/vulnerability-analysis/SKILL.md` |\n'
if knowledge not in body:
    needle = 'Leia o arquivo relevante sempre que a conversa envolver o conteúdo dele.'
    if needle not in body: raise SystemExit('Não encontrei a âncora da seção conhecimento do AGENTS.md')
    body = body.replace(needle, knowledge + '\n' + needle, 1)
if row not in body:
    needle = 'Se nenhuma skill se aplicar, ajude mesmo assim, usando os mesmos princípios deste arquivo.'
    if needle not in body: raise SystemExit('Não encontrei a âncora da tabela skills do AGENTS.md')
    body = body.replace(needle, row + '\n' + needle, 1)
agents.write_text(body, encoding='utf-8')
persona = target / 'agent/persona.md'
body = persona.read_text(encoding='utf-8')
section = '## Mentor de segurança (AppSec)\n\nQuando o assunto for cibersegurança, o DIO Agent age como um mentor defensivo: verifica escopo e autorização, faz perguntas de contexto antes de sugerir ações, distingue evidência de hipótese, explica riscos com linguagem acessível, prioriza mitigação e ensina a validar a correção. Jamais presume permissões nem incentiva ações contra terceiros.\n'
if '## Mentor de segurança (AppSec)' not in body:
    persona.write_text(body.rstrip() + '\n\n' + section, encoding='utf-8')
print('Extensão AppSec integrada em:', target)
