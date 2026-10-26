# Fundamentos de segurança para o DIO Agent

- **Vulnerabilidade:** fraqueza de software, configuração ou processo que pode ser aproveitada.
- **Ameaça:** evento ou agente capaz de causar dano ao explorar uma fraqueza.
- **Risco:** combinação contextual de probabilidade e impacto de um evento indesejado.
- **Confidencialidade:** somente pessoas autorizadas acessam os dados.
- **Integridade:** informações e sistemas permanecem corretos e sem alteração não autorizada.
- **Disponibilidade:** serviços e dados permanecem acessíveis quando necessários.

## Classificação qualitativa
Avaliar impacto (baixo/médio/alto) e probabilidade (baixa/média/alta) com justificativa explícita. Criticidade é contextual: nunca inferir CVSS sem métricas suficientes. Identificar nível de exposição, sensibilidade, autenticação, privilégios e mitigadores.

## Boas práticas
Validação de entrada e queries parametrizadas; menor privilégio; gestão segura de credenciais; atualizações; logs sem segredos; backups e testes de restauração; MFA; revisão de código; testes automatizados; segmentação; inventário e resposta a incidentes.

## Referenciais
- CWE-89: SQL Injection: https://cwe.mitre.org/data/definitions/89.html
- OWASP SQL Injection Prevention: https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
- MITRE ATT&CK T1190 (Exploit Public-Facing Application): https://attack.mitre.org/techniques/T1190/ — apenas quando aplicação pública for explorada, não como equivalência universal de SQL Injection.
