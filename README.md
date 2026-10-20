# DIO Agent — mentor de AppSec

Especialização em análise defensiva de vulnerabilidades, desenvolvida a partir de [digitalinnovationone/dio-agent](https://github.com/digitalinnovationone/dio-agent). O objetivo é aprender a investigar contexto e evidências antes de concluir que existe uma falha ou propor ações.

## O que mudou
- [Skill de análise](skills/vulnerability-analysis/SKILL.md) e [explicação](skills/vulnerability-analysis/README.md): contexto, escopo, identificação, avaliação de risco, correção e reteste.
- [Conhecimento de segurança](agent/knowledge/security-basics.md): vulnerabilidade, ameaça, risco, tríade CIA e boas práticas.
- [Persona](agent/persona.md) e [AGENTS.md](AGENTS.md): especialização e encaminhamento para a nova skill.
- [Template de relatório](templates/relatorio-vulnerabilidade.md): melhoria escolhida para comparar casos em um formato consistente.
- [Exemplo vulnerável](examples/app_vulneravel.py), [correção](app.py) e [testes](tests/test_login.py): laboratório SQLite em memória, sem servidor.
- [Análise documentada](docs/analise-sqli.md), [critérios de avaliação](docs/cenarios-appsec.md) e [prompts](prompts/01-contexto-servidor.txt).

A especialização usa instruções em Markdown; não treina nem ajusta pesos de um modelo. Arquivos e contribuições anteriores foram preservados abaixo e no histórico.

## Executar o laboratório
Use Python 3.10 ou superior. O laboratório utiliza somente a biblioteca padrão, sem instalação de pacotes.

```bash
git clone https://github.com/1giordani/dio-agent.git
cd dio-agent
python app.py
python -m unittest discover -v
python -m tools.validar_lab
python -m tools.validar_estrutura
```

No Windows, se necessário, substitua python por py. Os bancos são criados em memória e descartados ao encerrar. O exemplo inseguro é isolado para comparação didática; app.py contém a implementação corrigida.

## Executar o agente
Siga o [guia do Hermes](docs/hermes-appsec.md). Configure o harness e o provedor conforme a documentação oficial e rode hermes **na raiz deste repositório**. Solicite a leitura de AGENTS.md, da persona e da skill. Ter arquivos em skills/ não garante sua instalação no catálogo nativo do harness.

Os [prompts](prompts/02-revisao-sqli.txt) permitem revisar o laboratório. Para o cenário Ubuntu, o agente deve perguntar sobre o contexto ausente antes de sugerir comandos. Não é necessário escanear servidores para usar este projeto.

## Validação e evidências
Os testes locais verificam a reprodução da falha no exemplo e a rejeição das mesmas entradas no código corrigido, preservando login válido e nomes com apóstrofos. [Resultados](evidencias/README.md) registram a execução real. A conferência de estrutura verifica arquivos, frontmatter e registros da skill.

**O Hermes não foi executado nesta preparação.** Não há capturas ou respostas de agente fabricadas. Os testes Python não comprovam que um modelo seguirá a skill; esse comportamento tem um [roteiro de avaliação](docs/cenarios-appsec.md) próprio. O código didático também não substitui um sistema completo de autenticação.

## Entrega
Use a raiz pública https://github.com/1giordani/dio-agent. Uma descrição curta está em [ENTREGA-DIO.md](ENTREGA-DIO.md). Assista às aulas e realize a avaliação no Hermes antes de declarar essas etapas concluídas.

## Documentação original e contribuições anteriores

# 🤖 DIO Agent

> Seu mentor de Inteligência Artificial para aprender mais e melhor na [DIO](https://dio.me).

O **DIO Agent** é um agente de IA que acompanha você na sua jornada de estudos. Ele conhece as experiências da DIO (Bootcamps, Formações, Cursos, Desafios e muito mais) e ajuda você a estudar com mais clareza, destravar desafios e entender qualquer conceito.

E você não precisa instalar nada complicado. Em **3 passos simples**, o seu mentor de IA estará pronto para usar.

---

## ✨ Antes de começar: dois conceitos rápidos

Para usar o DIO Agent, basta entender duas palavras. As duas estão no [Glossário completo](docs/glossary.md), mas aqui vai a versão rápida:

- 🧠 **Agente de IA:** um chatbot comum responde perguntas, como um buscador mais esperto. Um *agente* de IA vai além: ele lê, planeja e executa passos para te ajudar a alcançar um objetivo. É a diferença entre alguém que te explica o caminho e alguém que caminha junto com você. O DIO Agent é um agente desse tipo: um tutor particular que acompanha a sua evolução.

- 🖥️ **Harness:** é o programa onde a conversa com o agente acontece. Vale a comparação: o agente é o professor, e o harness é a sala de aula. O mesmo professor pode dar aula em salas diferentes. Por isso o DIO Agent funciona em qualquer harness: você escolhe a "sala" no Passo 1, e o seu mentor continua o mesmo.

Pronto. Com isso já dá para começar.

---

## 🎯 O que o DIO Agent faz por você

| Você precisa de... | O DIO Agent... |
|--------------------|----------------|
| Saber por onde começar | Monta um plano de estudos no seu ritmo |
| Destravar um desafio | Te guia até a solução, sem entregar a resposta pronta |
| Entender um conceito | Explica de forma simples, com analogias e exemplos |

Ele conhece os formatos da DIO: Bootcamps, Formações, Acelerações, Cursos, English4Tech, Desafios de Código, Desafios de Projeto, Desafios Criativos, Lives e Mentorias. Assim, as recomendações sempre apontam para algo que você já tem na plataforma.

---

## 🚀 Comece em 3 passos

### 1️⃣ Instale um Harness

O harness é o programa que dá vida ao agente. Recomendamos o **Google Antigravity**, que tem limites de uso mais generosos para quem está começando. Mas qualquer harness moderno funciona.

| Harness | Documentação oficial |
|---------|----------------------|
| Google Antigravity (recomendado) | https://antigravity.google/docs |
| Claude Code | https://docs.claude.com/en/docs/claude-code |
| Codex | https://developers.openai.com/codex |
| OpenCode | https://opencode.ai/docs |
| Hermes | https://hermes-agent.nousresearch.com/docs |

Escolha um e siga o passo a passo da documentação oficial dele. Cada documentação já traz tudo certinho para o seu sistema, então a instalação é tranquila.

### 2️⃣ Configure o DIO Agent

Agora você vai baixar este repositório para o seu computador. Escolha a forma mais simples para você:

**Opção A: com Git** (se você já usa Git)

```bash
git clone https://github.com/digitalinnovationone/dio-agent.git
```

**Opção B: baixando o .zip** (se você não usa Git)

Na página do repositório no GitHub, clique no botão verde **Code** e depois em **Download ZIP**. Em seguida, extraia a pasta em um lugar fácil de encontrar.

Com o repositório baixado, abra a pasta `dio-agent` no harness que você instalou. Cada harness tem o seu jeito de abrir uma pasta de projeto, e a documentação dele mostra como fazer isso.

E é só isso! O harness lê automaticamente o arquivo `AGENTS.md` e o agente já sabe quem é: o seu mentor de estudos da DIO.

> 🔄 **Fique de olho nas atualizações.** Não importa se você usou o Git ou o .zip: o repositório do DIO Agent evolui com o tempo. De tempos em tempos, vale voltar aqui e pegar a versão mais recente. Quem usou Git pode rodar `git pull` (ou pedir pro próprio DIO Agent rodar); quem baixou o .zip pode baixar de novo. Assim o seu mentor está sempre com o melhor que a gente tem a oferecer.

### 3️⃣ Hands On!

Agora é só conversar. Você pode falar naturalmente, com as suas palavras. Mas, principalmente nas primeiras vezes, vale usar um modelo de prompt pronto: é só copiar e preencher os campos entre colchetes. Quanto mais contexto você dá, melhor o agente ajuda.

**🗺️ Plano de estudos**

```
Quero montar um plano de estudos (se possível, com materiais complementares).
- Meu objetivo: [ex: aprender mais sobre IA, ser dev back-end, concluir um bootcamp]
- Experiência ou carreira da DIO: [URL ou nome do bootcamp/formação, ou de uma carreira da DIO]
- Meu nível hoje: [iniciante, intermediário, avançado]
- Tempo disponível: [ex: 1 hora por dia, de segunda a sexta]
```

**🔓 Destravar desafio**

```
Estou travado em um Desafio de [Código, Projeto ou Criativo] da DIO.
- O que o desafio pede: [cole o enunciado ou descreva]
- Onde eu travei: [explique o ponto da dificuldade]
- Meu código atual: [cole aqui, se for Desafio de Código]
- Link do repositório base: [cole aqui, se for Desafio de Projeto]
Me ajuda a destravar sem dar a resposta pronta.
```

**💡 Explicar conceito**

```
Me explica o conceito de [ex: API, laço de repetição, herança].
- Meu nível: [nunca vi, já ouvi falar, quero aprofundar]
- Onde apareceu: [ex: no curso X de um bootcamp] (opcional)
```

Não precisa de comando especial nem de formato perfeito: o agente conduz a conversa a partir daí e pede mais detalhes se precisar.

---

## 🧩 As skills do agente

Uma **skill** é uma habilidade do agente, descrita em um guia passo a passo. O DIO Agent vem com três:

| Skill | Para que serve |
|-------|----------------|
| [Plano de estudos](skills/study-plan/SKILL.md) | Organiza o que estudar, em que ordem e em quanto tempo |
| [Destravar desafio](skills/unblock-challenge/SKILL.md) | Conduz você até a solução de um desafio, sem dar a resposta pronta |
| [Explicar conceito](skills/explain-concept/SKILL.md) | Explica conceitos de forma didática, com analogias e exemplos |

Você não precisa "chamar" uma skill. O agente percebe o que você precisa e usa a skill certa sozinho.

---

## 🗂️ Estrutura do repositório

```
dio-agent/
├── README.md                        Este guia
├── AGENTS.md                        Definição do agente (lida por qualquer harness)
├── CLAUDE.md                        Atalho para o Claude Code
│
├── agent/
│   ├── persona.md                   A personalidade e o tom do agente
│   └── knowledge/
│       ├── dio-platform.md          O que é a DIO
│       └── learning-experiences.md  Os formatos de aprendizado da DIO
│
├── skills/
│   ├── README.md                    O que são skills
│   ├── study-plan/                  Skill: plano de estudos
│   ├── unblock-challenge/           Skill: destravar desafio
│   └── explain-concept/             Skill: explicar conceito
│
└── docs/
    └── glossary.md                  Glossário de termos
```

> 🔍 **Por que funciona em qualquer harness?** O coração do projeto é o arquivo `AGENTS.md`, um padrão aberto que harnesses modernos sabem ler. O `CLAUDE.md` apenas aponta para ele, então você pode usar o harness que preferir.

---

## 📖 Glossário rápido

Termos como *agente*, *harness*, *skill* e *prompt* estão explicados com analogias simples no **[Glossário completo](docs/glossary.md)**. Se algum termo soar estranho, comece por lá.

---

## 💬 Sobre este projeto

O DIO Agent foi criado para acompanhar você desde o início dos Bootcamps e Formações da DIO. A ideia é simples: aprender na era da IA fica mais fácil quando você tem um mentor disponível a qualquer hora.

Bons estudos, e vem com a gente. 🚀

---

## 📚 Minha experiência no desafio

Este fork foi criado por **Giordani Martins Silva** durante a **Formação GitHub Certification**, da DIO, com o objetivo de praticar colaboração e documentação usando GitHub e Markdown.

### Objetivos praticados

- Criar um fork mantendo a referência ao projeto original;
- Utilizar títulos, listas, links, tabelas e blocos de código em Markdown;
- Registrar alterações com commits claros;
- Trabalhar com issues, branches e pull requests;
- Desenvolver um portfólio público de aprendizagem.

### Fluxo de colaboração

```text
Fork → Branch → Alteração → Commit → Pull Request → Merge
```

### Checklist

- [x] Criar o fork do repositório;
- [x] Personalizar o README;
- [x] Abrir uma issue de melhoria;
- [x] Criar uma branch;
- [x] Abrir e concluir um pull request;
- [ ] Entregar o projeto na plataforma DIO.

> Este projeto representa uma etapa prática da minha evolução em Git, GitHub e colaboração em projetos de tecnologia.

### Autor

**Giordani Martins Silva**

- GitHub: [@1giordani](https://github.com/1giordani)
- Repositório original: [digitalinnovationone/dio-agent](https://github.com/digitalinnovationone/dio-agent)

