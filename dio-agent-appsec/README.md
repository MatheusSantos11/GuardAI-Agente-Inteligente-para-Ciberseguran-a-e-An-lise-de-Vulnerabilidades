# DIO Agent — Especialização em Cibersegurança (AppSec)

Projeto do desafio DIO, baseado no repositório original [digitalinnovationone/dio-agent](https://github.com/digitalinnovationone/dio-agent). Esta entrega é um **pacote de extensão**: aplique os arquivos sobre uma cópia do repositório original para preservar as demais skills e documentações.

## Objetivo
Transformar o DIO Agent em mentor de segurança de aplicações: antes de responder, ele confirma autorização, pergunta sobre o ambiente, identifica evidências, estima impacto/probabilidade/severidade e ensina correção e validação.

## Arquivos acrescentados
- `skills/vulnerability-analysis/SKILL.md`: processo de análise defensiva.
- `skills/vulnerability-analysis/README.md`: documentação da skill.
- `agent/knowledge/security-basics.md`: CIA, ameaças, riscos, defesa e referências.
- `examples/app.py`: login SQLite intencionalmente vulnerável a SQL Injection.
- `examples/app_fixed.py`: login com query parametrizada.
- `tests/test_login.py`: testes de regressão da versão corrigida.
- `docs/APPSEC-ADDITIONS.md`: instruções exatas para adaptar `AGENTS.md` e `agent/persona.md`.

## Instalação e integração na base
1. Clone `https://github.com/digitalinnovationone/dio-agent.git`.
2. Copie os arquivos deste pacote para as respectivas pastas do clone.
3. Em `AGENTS.md`, adicione a linha da skill e a referência à base de conhecimento conforme `docs/APPSEC-ADDITIONS.md`.
4. Em `agent/persona.md`, adicione a seção AppSec conforme a mesma documentação.
5. Abra o terminal **na raiz do repositório clonado** e execute `hermes` (instale o harness conforme a [documentação oficial](https://hermes-agent.nousresearch.com/docs)). Outros harnesses compatíveis com `AGENTS.md` também podem ser usados.

## Como testar
Requer apenas Python 3.10+ e a biblioteca padrão:

```bash
python -m unittest discover -s tests -v
```

Abra no agente o arquivo `examples/app.py` e peça: "Atue como mentor AppSec. Confirme o escopo, analise a falha no login e me explique seu impacto, probabilidade, severidade, CWE e eventual mapeamento ATT&CK. Depois compare com `examples/app_fixed.py` e proponha validação." Para o segundo cenário: "Tenho um Ubuntu de laboratório potencialmente exposto. Quais informações você precisa antes de propor uma análise?" O comportamento esperado é perguntar o contexto primeiro.

## Melhoria escolhida
**Relatório padronizado de risco** com evidência, CIA, probabilidade, severidade, referências, correção e validação. Isso facilita comparar achados de segurança durante revisões de código e processos DevSecOps.

## Evidências para a entrega
Execute os testes e o harness na sua máquina; salve prints em `images/` mostrando a análise, perguntas de contexto e testes. **Não há prints de execução do Hermes incluídos** porque o harness não foi executado aqui.

## Segurança e limitações
Somente laboratório autorizado. O exemplo vulnerável não deve ser colocado em produção. A versão corrigida demonstra parametrização; autenticação real também requer hashing seguro de senhas, proteção de sessão, controles de acesso e limitação de tentativas. A skill não treina modelo nem executa análise automática: o harness lê instruções em Markdown.

### Instalação automática (alternativa)
Após clonar o repositório base, execute `python integrate.py CAMINHO_PARA_CLONE_DIO_AGENT` a partir deste pacote para copiar os arquivos e atualizar o `AGENTS.md` e a persona **sem apagar outras skills**. O script pode ser executado novamente sem duplicar as linhas.
