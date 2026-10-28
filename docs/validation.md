# Validação e limites

O pacote passou por autoria especializada, integração e revisão por um agente de IA independente da autoria. Isso é uma revisão de instruções e respostas simuladas, não uma avaliação com alunos reais.

## Comportamentos simulados

Foram executados 13 cenários: iniciante com erro; compreensão declarada com dificuldade produtiva; demanda avançada; resposta diferente do modelo; pronúncia sem áudio; uso apenas textual; troca de idioma; retorno após semanas; retomada sem registro; fonte ausente; explicação direta; revisão sem revelar resposta; variante regional válida.

Dois achados médios e um baixo foram corrigidos: ambiguidade de primeira/terceira pessoa nas demonstrações, generalização excessiva de preposição com cidades francesas e integração bibliográfica incompleta. Cinco retestes/conferências foram registrados. Os transcripts e seus limites estão em [tests/simulated-scenarios.md](../tests/simulated-scenarios.md).

## Importação e empacotamento

A primeira distribuição reunia materiais sem manifesto de plugin e não atendia à importação. A versão 1.0.1 corrigiu essa estrutura. O usuário enviou uma captura do plugin importado e as três skills passaram a aparecer no ambiente conectado; a imagem está no README. Isso confirma a importação daquela versão nesse ambiente, sem demonstrar funcionamento universal.

A versão 1.0.2 mantém os professores, atualiza os metadados de autoria/repositório e prepara a distribuição pública. Passou por **35 verificações locais**, incluindo as 25 verificações de empacotamento usadas na versão anterior, consistência das cópias, links/imagens da documentação, limites de instruções e ausência de caminhos pessoais. O resultado da execução fica em `dist/validation-report.json`, gerado localmente. Os três cabeçalhos de skills também foram conferidos pelo validador do Skill Creator durante a preparação original e a edição pública.

## O que não foi demonstrado

Não houve estudo longitudinal de aprendizagem, avaliação acústica, certificação CEFR, teste de todos os planos/interfaces do ChatGPT ou garantia de memória entre conversas. A validação local não executa o parser do servidor. Revisão espaçada sugerida não cria notificações por conta própria.

Para reproduzir as verificações:

```bash
python scripts/build.py
python scripts/validate.py
```

O registro de progresso distribuído permanece inicial e vazio. Dados de aprendizagem reais devem ser mantidos fora do repositório.
