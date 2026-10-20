# Executando a especialização no Hermes

## Preparação
Instale e configure o Hermes seguindo a [documentação oficial](https://hermes-agent.nousresearch.com/docs/). A configuração do provedor de modelo e suas credenciais é feita localmente; nunca publique chaves no repositório.

```bash
git clone https://github.com/1giordani/dio-agent.git
cd dio-agent
hermes
```

Abra o terminal na raiz que contém AGENTS.md, agent/ e skills/. Na conversa, peça explicitamente: “Leia AGENTS.md, agent/persona.md e skills/vulnerability-analysis/SKILL.md; use esse roteiro nesta sessão.” Se o harness não carregar algum arquivo automaticamente, solicite sua leitura. A pasta skills/ deste projeto não implica instalação automática no catálogo nativo do Hermes. Não é treinamento do modelo.

A [CLI oficial](https://hermes-agent.nousresearch.com/docs/user-guide/cli/) também permite executar um prompt de arquivo, após configurar o provedor:

```bash
hermes chat --query-file prompts/01-contexto-servidor.txt
hermes chat --query-file prompts/02-revisao-sqli.txt
hermes chat --query-file prompts/03-reteste.txt
```

Cada comando pode iniciar uma sessão distinta; os prompts referenciam os arquivos necessários. Consulte a documentação da sua versão caso a CLI tenha mudado. Para descoberta nativa de skills e diretórios confiáveis, consulte [Skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/); não copie configurações de confiança sem revisar o conteúdo.

## Verificação prática
1. Use o primeiro prompt. O agente deve perguntar sobre os serviços, o objetivo e o escopo ausentes antes de sugerir comandos. “Ubuntu exposto” não revela portas, versões ou vulnerabilidades.
2. Use o segundo. Confirme que separa o exemplo vulnerável da correção e descreve CWE-89. ATT&CK T1190 só é pertinente ao cenário hipotético de exploração de aplicação pública, não uma técnica executada neste laboratório sem rede.
3. Use o terceiro. Confira resultados reais dos testes, limitações e riscos residuais. As consultas parametrizadas tratam valores como dados; não tornam todo um sistema seguro.
4. Compare o relatório com templates/relatorio-vulnerabilidade.md e os critérios de docs/cenarios-appsec.md.

## Estado das evidências
O Hermes **não foi executado** durante a preparação desta entrega. As respostas do modelo, seu seguimento de contexto e capturas de tela precisam ser verificados na sua sessão. Os testes Python e os arquivos em evidencias/ validam apenas o código local e a estrutura publicada.

Ao registrar a sessão, remova tokens, credenciais e dados pessoais. Registre a versão do Hermes, data, prompt utilizado e saída observada. Não apresente respostas esperadas como evidência executada.

