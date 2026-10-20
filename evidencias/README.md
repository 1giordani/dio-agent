# Evidências

- validacao-local.json: saída real de python -m tools.validar_lab; cada booleano indica se a expectativa foi atendida, incluindo a reprodução da falha no exemplo inseguro.
- testes.txt: saída real de python -m unittest discover -v.
- estrutura.txt: resultado da conferência dos arquivos e registros da skill.

Não houve execução do Hermes, comparação com chat genérico ou teste de servidor. Não há prints fabricados. docs/cenarios-appsec.md e prompts/ contêm roteiros de avaliação, não resultados. Após executar o Hermes, acrescente capturas reais em images/ se desejar; remova informações sensíveis antes de publicar.

