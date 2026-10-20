# Análise do laboratório de SQL Injection

## Contexto e evidência
Código de estudo próprio, com usuário fictício e SQLite em memória. Não há HTTP, persistência em disco nem serviço acessível. examples/app_vulneravel.py concatena username e password na consulta. O valor de usuário `aluno' --`, com senha errada, fecha a string e comenta a verificação de senha. O teste local demonstra autenticação indevida nessa função; não demonstra acesso a nenhum sistema real.

Classificação: **CWE-89 — SQL Injection**. [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/) descreve exploração de aplicação pública para acesso inicial. Pode ser discutida se esse padrão existir em um login público, mas **não é uma técnica executada neste experimento em memória**. Não foi atribuído CVE.

## Impacto, probabilidade e severidade
No exemplo, o impacto observado é a quebra da decisão de autenticação, relacionada à integridade. Divulgação de registros, alteração de dados e interrupção de serviço são impactos potenciais dependentes de permissões, consultas e implantação; não foram comprovados aqui.

A reprodução no cenário didático é direta, sem pré-requisitos além da chamada da função com entradas controladas. Na matriz educacional da skill: impacto 1 (somente dados fictícios descartáveis), probabilidade 3 (reproduzível), produto 3, severidade **moderada para este laboratório**. Essa avaliação limitada não estima risco de uma aplicação real, nem equivale a CVSS. Um sistema público requer contexto adicional para ser classificado.

## Correção
app.py mantém a instrução SQL constante e passa username como parâmetro SQLite. A senha é verificada em Python por hash PBKDF2-HMAC-SHA256 com salt aleatório e comparação por hmac.compare_digest. A senha fictícia da demonstração não deve ser reutilizada. A parametrização corrige o vetor; o hashing é uma melhoria adicional de armazenamento. Valores podem ser parametrizados; identificadores dinâmicos exigem projeto apropriado e allowlist.

## Reteste e limites
Consulte os resultados executados em ../evidencias/validacao-local.json e ../evidencias/testes.txt. Os testes verificam login válido, senha incorreta, usuário inexistente, entradas de injeção, apóstrofo legítimo, salts diferentes e integridade da tabela.

O código é uma demonstração, não um produto completo de autenticação: não implementa sessões, MFA, recuperação de conta, limitação de tentativas, TLS, auditoria ou gestão de segredos. O sucesso dos testes comprova os casos cobertos, não ausência de todas as falhas. A avaliação do comportamento do agente no Hermes permanece pendente.

## Fontes
- [Python sqlite3: placeholders](https://docs.python.org/3/library/sqlite3.html).
- [CWE-89](https://cwe.mitre.org/data/definitions/89.html).
- [OWASP: prevenção de SQL Injection](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html).
- [OWASP: armazenamento de senhas](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html).

Pergunta de reflexão: por que permitir um apóstrofo em um nome legítimo e impedir que ele altere uma instrução são requisitos compatíveis?

