# Fundamentos de segurança para análise defensiva

## Vocabulário
- **Ativo:** dado, serviço ou recurso que tem valor.
- **Vulnerabilidade:** fraqueza que pode permitir uma consequência indesejada.
- **Ameaça:** agente ou circunstância capaz de explorar uma fraqueza.
- **Risco:** combinação contextual da possibilidade de ocorrência com as consequências.
- **Exploração:** uso de uma fraqueza para obter um resultado.
- **Mitigação:** redução de risco; não significa eliminação universal do problema.

## Confidencialidade, integridade e disponibilidade
Confidencialidade limita divulgação; integridade protege contra alteração indevida; disponibilidade sustenta acesso legítimo. Uma falha pode afetar mais de uma dimensão. Diferenciar o que foi observado do que depende de permissões ou exposição ainda desconhecidas.

## Contexto mínimo
Identificar propriedade/autorização, ambiente, superfície exposta, autenticação exigida, sensibilidade dos dados e controles existentes. Um Ubuntu exposto não está automaticamente vulnerável: é preciso entender serviços, configuração, versões e permissões.

## Matriz didática
Não é CVSS e não substitui análise profissional.

| Nível | Impacto | Probabilidade |
|---|---|---|
| 1 | Consequência limitada a dados descartáveis, com recuperação simples | Pré-requisitos relevantes e controles consistentes |
| 2 | Consequência relevante, porém com alcance limitado | Cenário plausível, com pré-requisitos ou controles parciais |
| 3 | Comprometimento significativo de ativo sensível ou serviço essencial | Caminho acessível e pré-requisitos demonstrados no contexto analisado |

Calcular I × P somente quando ambos tiverem justificativa. Faixas: 1–2 baixa; 3–4 moderada; 5–6 alta; 7–9 crítica. Se faltarem informações, não pontuar. A exploração determinística de um fixture local não comprova probabilidade de comprometimento de um sistema de produção.

## SQL Injection
CWE-89 classifica entrada capaz de alterar a estrutura de um comando SQL. Consultas parametrizadas separam código SQL e valores. Placeholders do SQLite são específicos desse driver; não montar uma consulta com interpolação antes de passá-la ao execute.

Parâmetros representam valores, não nomes de tabelas ou colunas. Identificadores dinâmicos exigem desenho adequado e allowlist. Validação de formato pode complementar a defesa, mas não substitui a parametrização.

## Classificações
CWE descreve fraquezas. CVE identifica vulnerabilidades específicas publicadas. MITRE ATT&CK descreve comportamentos adversários. Não criar uma CVE para código didático.

T1190 — Exploit Public-Facing Application — pode contextualizar a exploração de uma falha em aplicação pública visando acesso inicial. No laboratório deste repositório há SQLite em memória, sem servidor HTTP; o mapeamento é apenas condicional a outro cenário, não uma técnica executada em rede.

## Boas práticas
Aplicar privilégio mínimo, segredos fora do código, atualização, proteção de transporte, logs sem credenciais e validação de entrada coerente com o domínio. Senhas precisam de função adequada e salt; não usar hash rápido simples como substituto.

A correção local usa PBKDF2-HMAC-SHA256 com salt aleatório e comparação de tamanho fixo. Em produção, definir política de autenticação, custo da função, sessão, limitação de tentativas, gestão de segredos e observabilidade conforme os requisitos.

## Integridade das evidências
Separar execução real, exemplo de resposta e plano de teste. Registrar ferramenta, escopo, comando, resultado e limite. Nunca concluir que todos os riscos foram eliminados a partir de um único payload.

## Fontes
- [CWE-89](https://cwe.mitre.org/data/definitions/89.html).
- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/).
- [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html).
- [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html).
- [Python sqlite3](https://docs.python.org/3/library/sqlite3.html).

