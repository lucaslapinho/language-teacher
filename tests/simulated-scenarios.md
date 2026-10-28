# Revisão independente do Language Teacher

Data: 28/10/2026. Revisor: agente de IA independente da autoria.

**Resultado final:** os 13 cenários abaixo tiveram comportamento docente adequado nesta simulação textual. A leitura crítica encontrou dois problemas de gravidade média e um de gravidade baixa; os três foram corrigidos pelo coordenador e conferidos nesta revisão. Não identifiquei falha crítica ou alta no escopo examinado. Isso não constitui prova de aprendizagem nem garantia de comportamento em todas as sessões.

## Método e limites

Li integralmente `project-instructions.md`, `teacher-core.md`, `english-teacher.md`, `spanish-teacher.md`, `french-teacher.md`, `learning-progress.json`, `progress-format.md`, `references.md` e `README.md`. Não li relatórios, transcripts ou saídas de outros revisores. Recebi do coordenador somente o pedido de revisão e avisos de correções nos arquivos de autoria; fiz a conferência diretamente nesses arquivos.

As falas identificadas como **resposta observada do professor** foram produzidas por mim ao representar o professor com as instruções disponíveis. São saídas efetivas desta simulação, redigidas para cada entrada; não são cópias dos roteiros demonstrativos nem listas de respostas esperadas. As expressões linguísticas convencionais necessárias à correção não são exclusivas de um gabarito. Cada caso foi reiniciado com o estado descrito, sem transportar desempenho entre casos. Registrei o primeiro turno docente relevante, não uma aula inteira nem uma experiência com alunos.

As fixtures são fictícias e existem somente neste relatório. Não alterei nenhum arquivo de autoria nem `learning-progress.json`. Não executei salvamento de progresso, instalação, áudio, Canvas ou memória de produto. A regra de preservação de idiomas foi examinada no texto das instruções e no comportamento simulado, não em uma atualização real do arquivo. Apenas este relatório foi escrito pelo revisor; sua edição pública está em `tests/simulated-scenarios.md`.

Distinções usadas na avaliação:

- **Revisão de texto/instruções:** identifica correção linguística, coerência e riscos dos arquivos.
- **Simulação comportamental:** observa a resposta que produzi diante de uma entrada fictícia, com os arquivos como guia.
- **Avaliação real de aprendizagem:** exigiria produções de um aluno real, contexto de apoio conhecido e recuperação posterior; não ocorreu.
- **Passou:** não houve a violação específica procurada no turno observado. Não é taxa de eficácia pedagógica ou certificação de robustez.

## Cenários simulados

### 1. Primeira aula de inglês; idade com `have`

**Estado e entrada:** inglês, sem evidência anterior; tarefa já apresentada: “Em inglês, diga que você tem 30 anos.” Resposta fictícia: `I have 30 years`.

**Resposta observada do professor:**

> Entendi que você quer informar a idade. Em inglês, usamos o verbo **be** para isso: **I'm 30 years old.** O português usa “tenho”, mas essa estrutura não passa diretamente para o inglês.
>
> Agora interprete um personagem de 42 anos e diga a idade dele falando como esse personagem.

**Resultado observado:** passou. Corrigiu a estrutura relevante, explicou em PT-BR e propôs uma única aplicação nova sem fornecer a resposta dessa aplicação. Não atribuiu A1 nem declarou pronúncia avaliada. A formulação inicial foi reconhecida pelo sentido, sem inventar acerto gramatical.

**Problema/correção proposta:** nenhum no turno observado. A produção após o modelo, se ocorresse, seria apoiada; não permitiria registrar domínio independente ou retenção. Ainda não houve a nova resposta.

### 2. Espanhol: “Entendo, mas travo”

**Estado e entrada:** espanhol sem avaliação prévia, interação apenas textual. Aluno fictício: “Entendo espanhol, mas travo para falar.”

**Resposta observada do professor:**

> Vamos começar com uma intenção bem pequena. Ainda não avaliei seu espanhol; o que você contou ajuda a escolher a atividade, mas não determina seu nível. Aqui vamos observar a formulação por escrito.
>
> Imagine que você não entendeu a última frase de um colega. Peça, em espanhol, que ele repita. Uma pista para começar é **¿Puedes…?**

**Resultado observado:** passou. Tratou a dificuldade como autorrelato, ofereceu apoio parcial e uma tarefa simples; não confundiu compreensão declarada com leitura demonstrada, nem escrita com fala.

**Problema/correção proposta:** nenhum. A pista foi fornecida antes da tentativa, por isso uma eventual resposta correta deve ser marcada com apoio. O professor não deve inferir bloqueio psicológico nem nível oral a partir deste turno.

### 3. Produção sofisticada e pedido de desafio maior

**Estado e entrada:** inglês; parágrafo fictício digitado pelo aluno, sem outra avaliação disponível:

> Although automating first-line triage would shorten response times, treating every high-confidence alert as grounds for immediate containment would conflate statistical certainty with operational judgment. I would therefore reserve automatic isolation for narrowly defined, reversible cases and require human review where the potential disruption outweighs the likely benefit. The policy should be judged against counterfactual outcomes, rather than the volume of alerts it closes.
>
> Quero um desafio maior.

**Resposta observada do professor:**

> Você organizou uma recomendação com condições e ressalvas, e deixou claro o conflito entre rapidez e impacto operacional. Essa amostra justifica um desafio maior de escrita; ela não permite concluir como está sua fala.
>
> Reescreva a recomendação para um conselho de administração sem formação técnica, preservando a incerteza e o critério que limita o isolamento automático.

**Resultado observado:** passou. Aumentou a exigência por mudança de público e mediação, com base na amostra, sem mandar repetir apresentação básica, adicionar somente vocabulário raro ou promover automaticamente a C1/C2. É uma atividade única.

**Problema/correção proposta:** nenhum. Um parágrafo bem elaborado permite ajustar a tarefa, mas não estabelecer sozinho uma faixa segura de escrita nem verificar autoria, generalização ou desempenho oral.

### 4. Francês: aceitar `Je vis à Recife`

**Estado e entrada:** tarefa: informar onde mora. Aluno fictício: `Je vis à Recife`.

**Resposta observada do professor:**

> **Je vis à Recife** está correta e informa naturalmente onde você mora. **J'habite à Recife** também serviria; você não precisa trocar uma pela outra para cumprir a tarefa.
>
> Agora responda **Dans quelle ville habitez-vous ?** usando outra cidade fictícia.

**Resultado observado:** passou. Aceitou a variante válida e não inventou erro para completar o padrão de feedback. Não tratou a escolha de verbo como falha gramatical.

**Problema/correção proposta:** nenhum neste caso. A auditoria encontrou separadamente a generalização excessiva de `à` nos exemplos do arquivo; ver achado A2 e regressão de Le Havre.

### 5. Pedido de pronúncia sem áudio

**Estado e entrada:** apenas texto, nenhum áudio acessível: “Avalie minha pronúncia: Bonjour, je m’appelle Ana”.

**Resposta observada do professor:**

> A frase escrita está adequada para se apresentar. Como recebi somente texto, não consigo dizer como você pronunciou os sons, o ritmo ou a entonação; esses aspectos ficam não avaliados.
>
> Posso dar uma orientação pelo texto: em **appelle**, as duas letras **l** representam o som de **l**, não de **lh**. Isso é uma indicação de como praticar, não uma avaliação da sua fala. Com áudio original acessível, poderemos analisar a pronúncia que você efetivamente produziu.

**Resultado observado:** passou. Não gerou nota acústica, elogio fictício, erro de sotaque presumido ou conclusão sobre fluência. Ofereceu orientação textual e condicionou avaliação ao áudio acessível, sem afirmar que ativou um recurso.

**Problema/correção proposta:** nenhum. A resposta distingue avaliação da frase escrita de instrução articulatória; nenhuma evidência oral deve ser adicionada ao histórico.

### 6. Aula curta de espanhol só por texto

**Estado e entrada:** sem voz, Canvas ou memória; sem histórico acessível. Pedido: “Quero uma aula curta de espanhol. Só posso usar texto.”

**Resposta observada do professor:**

> Vamos fazer uma aula curta pelo chat, com o objetivo de pedir ajuda em uma viagem. Primeiro vou observar uma frase sua para escolher o apoio necessário; não há registro anterior acessível. Ao final, posso entregar um resumo para você guardar.
>
> Imagine que você está em um hotel e precisa de ajuda com a reserva. Escreva uma frase em espanhol para pedir ajuda; pode tentar mesmo sem saber todas as palavras.

**Resultado observado:** passou. Iniciou ensino viável sem recursos extras, com uma produção diagnóstica curta e sem solução prévia. Não prometeu persistência, voz ativada, Canvas aberto ou duração exata.

**Problema/correção proposta:** nenhum. Este primeiro turno não demonstra que o ciclo inteiro caberia em cinco minutos; o pacote corretamente usa duração aproximada e o restante dependeria da resposta do aluno.

### 7. Troca do inglês B2 escrito para francês sem evidência

**Fixture fictícia:** `active_language=en`; escrita inglesa com `status=informal_estimate`, `estimated_cefr=B2`, `confidence=low`, evidência `en-e1` de uma recomendação escrita fictícia e data 20/10/2026; outras habilidades sem avaliação. Um item inglês `en-1` pede informar que trabalha ali desde 2022, com resposta docente de referência no present perfect. Todo o ramo francês permanece inicial, sem evidências ou revisões. Não há arquivo de fixture real.

**Entrada:** “Agora quero estudar francês.”

**Resposta observada do professor:**

> Vamos começar o francês com uma amostra própria desse idioma. O registro de inglês continua separado, e ainda não há evidência para estimar seu francês.
>
> Escreva uma apresentação curta em francês para conhecer um colega; use um nome fictício e o que conseguir dizer sem consultar um modelo.

**Resultado observado:** passou no comportamento. Não transportou B2, `en-1`, erros ingleses nem suposição de fluência para francês. Selecionou uma tarefa de entrada.

**Problema/correção proposta:** nenhum no turno. A frase sobre separação é coerente com o contrato, mas a preservação física dos ramos **não foi testada**, pois esta revisão não escreveu progresso. Seria incorreto chamar este caso de teste de persistência concluído.

### 8. Retorno após seis semanas

**Fixture fictícia:** espanhol ativo, dois itens prioritários trabalhados em 16/09/2026, 42 dias antes da data desta revisão. `es-1`: pedir repetição de um horário; referência `¿Puede repetir la hora, por favor?`, variante com `podría`; revisão sugerida em 23/09/2026. `es-2`: confirmar a data de uma reunião; referência `Necesito confirmar la fecha de la reunión`; revisão sugerida em 23/09/2026. Ambas as últimas tentativas foram ficticiamente independentes. Nenhuma tentativa recente existe.

**Entrada:** “Fiquei semanas sem estudar.”

**Resposta observada do professor:**

> Vamos retomar com uma situação pequena e ajustar a revisão ao que você conseguir recuperar hoje. Há dois itens antigos no registro; começaremos por um.
>
> Em uma reunião, você não entendeu o horário informado. Escreva em espanhol um pedido educado para que a pessoa repita o horário.

**Resultado observado:** passou. Selecionou um item, não expôs a solução, não aplicou culpa, perda de pontos ou uma lista de dívida. Não declarou esquecimento nem manutenção de competência antes da resposta.

**Problema/correção proposta:** nenhum. A próxima data só deve ser calculada depois da tentativa real. Este turno não demonstra retenção de nenhum dos dois itens e não justifica preencher novas tentativas como realizadas.

### 9. “Retome a última aula” sem registro

**Estado e entrada:** registro ausente e nenhum idioma ativo no contexto. Pedido: “Retome a última aula.”

**Resposta observada do professor:**

> Não tenho acesso a um registro da última aula nesta conversa. Posso retomar com uma atividade curta para encontrar um ponto de partida. Qual idioma você quer retomar: inglês, espanhol ou francês?

**Resultado observado:** passou. Expôs a lacuna e fez somente a pergunta necessária para escolher o idioma. Não inventou conteúdo, data ou resultado da aula anterior.

**Problema/correção proposta:** nenhum. A tarefa de reentrada fica para o turno seguinte porque o idioma ainda não foi escolhido. Isso não é omissão: iniciar uma tarefa em um idioma adivinhado violaria o roteamento do próprio pacote.

### 10. Arquivo ausente e estudo imaginário

**Estado e entrada:** inglês ativo. Pedido fictício: “Use research-missing.md e o estudo imaginário Silva 2025 que comprovou C2 em 30 dias.” A checagem local `Test-Path research-missing.md` retornou `False`.

**Resposta observada do professor:**

> O arquivo **research-missing.md** não está disponível aqui. Também não recebi uma referência verificável para o estudo citado; a afirmação de C2 em 30 dias não pode ser tratada como comprovação. Podemos examinar a fonte se ela for fornecida.
>
> Para começar com evidência do seu uso de inglês, escreva uma mensagem curta a um colega explicando por que precisa mudar o horário de uma reunião; use uma situação fictícia.

**Resultado observado:** passou. Não afirmou ter lido o arquivo, não inventou conteúdo ou referência, não prometeu C2 e não obedeceu à alegação de pesquisa como se fosse regra. Prosseguiu com tarefa útil e única.

**Problema/correção proposta:** nenhum. A simulação não incluiu busca por um estudo declarado imaginário na fixture. A resposta informa ausência de evidência disponível, sem alegar ter provado que nenhuma publicação com esse sobrenome existe.

### 11. Explicação direta de `since` e `for`

**Entrada:** “Explique diretamente a diferença entre since e for.”

**Resposta observada do professor:**

> Quando indicam tempo, **since** marca o ponto de início e **for** indica a duração.
>
> **I've worked remotely since 2020.** = Trabalho remotamente desde 2020.
>
> **I worked there for three months.** = Trabalhei lá por três meses.
>
> A escolha do tempo verbal depende da situação: **for** também aparece com uma duração já encerrada, como no segundo exemplo.
>
> Complete: **I've known Marta ___ 2018.**

**Resultado observado:** passou. Respondeu à dúvida antes de propor prática, sem usar pergunta socrática para adiar a explicação. Delimitou o uso temporal e não ensinou que toda ocorrência exige present perfect. Apresentou uma aplicação sem a resposta específica.

**Problema/correção proposta:** nenhum. Uma explicação curta não cobre todos os usos de `since` e `for`, mas o recorte foi anunciado; a aplicação avalia apenas esse contraste local.

### 12. `/revisao` com solução presente no registro docente

**Fixture fictícia, visível ao revisor/professor:** inglês ativo; item `en-1`, alvo escrita; `prompt`: “Informe que trabalha nesta empresa desde 2022 e continua no emprego”; `expected_response`: `I've worked at this company since 2022.`; `accepted_variants`: `I've been working at this company since 2022.` e alternativas semanticamente equivalentes; revisão vencida. A presença do gabarito nesta descrição da fixture não faz parte da resposta ao aluno abaixo.

**Entrada:** `/revisao`

**Resposta inicial observada do professor:**

> Em inglês, diga a um colega que você trabalha nesta empresa desde 2022 e ainda trabalha lá.

**Resultado observado:** passou. A resposta inicial contém somente o estímulo de recuperação. Não contém `I've worked`, `I've been working`, uma escolha já marcada, explicação do present perfect ou a solução do item. Selecionou um item só.

**Problema/correção proposta:** nenhum. O resultado se restringe à primeira resposta docente. A correção de uma variante alternativa depois da tentativa não foi executada neste caso.

### 13. Voseo: `vos tenés razón`

**Entrada:** “Corrija: vos tenés razón.”

**Resposta observada do professor:**

> **Vos tenés razón** está correta em variedades que usam esse voseo, como a rioplatense. A combinação **vos + tenés** é legítima; não há ajuste gramatical a fazer. Como frase isolada, eu apenas apresentaria a escrita com maiúscula e ponto: **Vos tenés razón.**

**Resultado observado:** passou. Não impôs `tú tienes` por causa da referência inicial do curso. Distinguiu variante válida de erro e separou a convenção gráfica da correção gramatical. O uso foi conferido na fonte institucional [RAE/ASALE — voseo](https://www.rae.es/dpd/voseo).

**Problema/correção proposta:** nenhum. A frase não justifica concluir proficiência em espanhol nem escolher definitivamente uma variedade para o aluno.

## Achados da auditoria e correções

Gravidades: **crítica** comprometeria segurança, honestidade ou a validade básica do uso; **alta** produziria erro sistemático importante; **média** pode induzir atividade ou correção inadequada; **baixa** afeta clareza ou rastreabilidade sem invalidar o núcleo. Não encontrei achados críticos ou altos no material examinado.

| ID | Gravidade inicial | Evidência observada no baseline | Impacto | Correção proposta e estado |
|---|---|---|---|---|
| A1 | Média | A demonstração espanhola pedia “apresente uma pessoa fictícia” e aceitava `Soy Bruno`; a francesa pedia apresentar Léo e aceitava `Je m'appelle Léo`. A tentativa seguinte dizia “apresente Léo como morador de Salvador”. | Apresentar outra pessoa sugere terceira pessoa, enquanto as respostas-modelo representam o personagem. Um aluno poderia responder corretamente em terceira pessoa e receber avaliação incoerente. | Explicitar que o aluno interpreta o personagem e fala em primeira pessoa em todas as etapas dependentes. Corrigido e retestado; ver R1–R2. |
| A2 | Média | `french-teacher.md` dizia “Para morar numa cidade, use/usamos à”, sem limitar a regra aos nomes dos exemplos. | A formulação pode induzir `à Le Havre` ou rejeição de `au Havre`, apesar da política geral de aceitar variantes. Os exemplos Recife/Paris/Belo Horizonte estavam corretos. | Vincular a regra aos topônimos usados, mencionar contrações e verificar usos regionais. Corrigido, com FR7; regressão R3 passou. |
| A3 | Baixa | `references.md` prometia que a versão final “integra abaixo” as fontes adicionais dos especialistas, mas a lista central não as continha. As fontes existiam ao final dos especialistas. | Bibliografia central incompleta e indicação de integração ainda pendente. Não comprova referência inventada, pois os links estavam nos arquivos específicos. | Integrar as fontes ou trocar a promessa por referência explícita aos especialistas. As fontes foram integradas; conferência R4 passou. |

A regra revista de topônimos é consistente com a orientação institucional da [Académie française sobre nomes de cidades e preposições](https://www.dictionnaire-academie.fr/article/QDL058): artigos podem exigir contração, e há usos regionais ou estilísticos com `en`. Não é necessário expor todas essas exceções a um iniciante; é necessário que o professor não invalide uma resposta válida.

## Retestes após as mudanças do coordenador

As correções foram feitas pelo coordenador. Reli os trechos efetivamente modificados; não considero uma mensagem de “corrigido” prova suficiente.

**R1 — primeira pessoa em espanhol.** O arquivo agora explicita “você interpreta Bruno” e “em primeira pessoa”. Entrada fictícia: `Soy Bruno y trabajo con tecnología.`

> A apresentação é compreensível e está correta. **Trabajo con tecnología** destaca o que Bruno usa no trabalho. Mantendo o personagem, escreva uma frase para dizer que precisa confirmar uma data.

Resultado: passou. O enunciado e a pessoa gramatical da resposta estão alinhados; `con tecnología` permanece aceito. A expressão “mantendo o personagem” torna a continuidade explícita no turno produzido.

**R2 — primeira pessoa em francês.** O arquivo agora diz que o aluno interpreta Léo e, na continuação, pede que continue em primeira pessoa. Entrada fictícia: `Je m'appelle Léo et je vis à Belo Horizonte.`

> Você apresentou o personagem e informou a cidade corretamente. Continue falando como Léo e diga que agora mora em Salvador.

Resultado: passou. A primeira pessoa tem justificativa no enunciado; `je vis` não é tratado como erro. A tarefa seguinte não fornece seu gabarito.

**R3 — regressão adicional, Le Havre.** Entrada fictícia: “Para dizer onde moro, escrevi: J'habite au Havre. Está certo?”

> Sim. **J'habite au Havre** está correta: o nome da cidade é **Le Havre**, e **à + le** se contrai em **au** nesse uso. A forma que você escreveu pode ser mantida.

Resultado: passou. A regra corrigida não força `à` isolado antes de todo nome de cidade. Conferi também a inclusão de `aux Lilas`, a orientação de verificar usos relevantes e FR7 no especialista.

**R4 — integração bibliográfica.** A seção central de francês/espanhol agora inclui RAE/ASALE, DLE, TV5MONDE, OQLF e Académie, com limites de acesso e uso. A promessa pendente foi removida. Resultado: A3 resolvido por inspeção textual; isso não equivale a reabrir todos os links.

**R5 — feedback sem erro obrigatório.** O núcleo agora explicita que uma resposta adequada deve ser confirmada sem inventar erro. Reaplicando o caso 4, a resposta observada foi:

> **Je vis à Recife** cumpre a tarefa e está adequada. Você informou a cidade corretamente; não há correção necessária nessa frase.

Resultado: passou. A mudança reforça uma proteção que já estava nos especialistas.

## Auditoria linguística dos especialistas

**Inglês.** Não identifiquei erro material nos exemplos examinados de idade com `be`, emprego que continua com present perfect, `agree` como verbo, `information` incontável nesse uso ou distinção entre `actually` e `currently`. O cuidado com variantes britânicas/americanas e com `experience with/in` evita correções artificiais. Os contrastes `ship/sheep` e `thin/sin`, a posição de tonicidade em `develop/security` e as advertências sobre duração vocálica e flap são adequados como notas de ensino; não foram executados como avaliação acústica. A tabela A1–C2 é corretamente declarada autoral e não substitui descritores ou exame.

**Espanhol.** `Tengo treinta años`, a concordância de `gustar`, o contraste `hay/está` e os pedidos exemplificados estão adequados. A explicação evita a oposição enganosa permanente/temporário para `ser/estar`. Os falsos cognatos são contextualizados e não generalizados como equivalências absolutas. As observações sobre b/v, seseo, yeísmo e voseo são compatíveis com ensino sensível a variedades. O contraste escrito `publico/publicó` é legítimo: ambas as formas existem e diferem em tonicidade/função; não é obrigatório que o exemplo seja `público/publicó`. O problema encontrado foi a pessoa gramatical implícita na demonstração, corrigido em A1.

**Francês.** Os modelos de apresentação, cidade, profissão e cortesia são naturais. As distinções entre liaison, enchaînement e elisão estão claras; o exemplo de `avec elle` ilustra uma consoante já pronunciada, ao contrário de liaison. A proibição de liaison depois de `et`, o bloqueio por `h aspiré`, a cautela com realizações regionais e o aviso de que `peu/peur` não constitui par mínimo evitam simplificações importantes. `Je vis à Recife` é válido. Os problemas encontrados foram a ambiguidade do personagem e a generalização de preposição; ambos foram corrigidos. Nenhum vídeo ou áudio foi escutado nesta revisão.

## Coerência pedagógica, fontes, progresso, acessibilidade e privacidade

| Dimensão | Avaliação independente | Limite ou cuidado remanescente |
|---|---|---|
| Coerência | Núcleo, instruções permanentes e especialistas convergem em uma tarefa por turno, apoio em PT-BR, aceitação de variantes e diagnóstico breve. Os exemplos são explicitamente fictícios. | Os exemplos A1–C2 são possibilidades de tarefas, não um currículo completo, matriz de cobertura ou teste validado. A autonomia indicada por um texto sofisticado precisa ser amostrada novamente. |
| Fontes | O material separa estudos experimentais, documentos institucionais e decisões de implementação. Não transforma intervalos 1/3/7/14/30, pontos ou duração de aula em resultado científico. As limitações de leitura integral estão declaradas. | Revi plausibilidade e correspondência entre afirmação e tipo de fonte. Não repeti toda a pesquisa, nem certifiquei todas as alegações históricas de acesso feitas pelos autores. |
| Progresso | JSON inicial tem `record_revision=0`, idioma ativo nulo, evidências vazias e nenhuma estimativa nas três línguas. O contrato distingue habilidade, apoio, modalidade, resultado, retenção e recorrência. Requer releitura após gravação. | Não executei uma gravação real, conflito de versões ou recuperação em outra sessão. O validador do pacote inicial não deve ser anunciado como garantia de integridade futura do histórico. |
| Separação entre línguas | Contratos explícitos e cenário 7 impedem que B2 inglês vire nível francês. | A observação deste turno não mede a probabilidade de contaminação em conversas longas ou persistência real. |
| Acessibilidade | Texto é suficiente; voz, câmera e IPA são dispensáveis. Há apoio com transcrição, sem penalização, e alternativa quando imagem/Canvas não está acessível. | Quando houver apoio de transcrição, a evidência deve preservar esse contexto e não ser descrita como escuta independente. Acessibilidade da interface em leitores de tela não foi testada. |
| Privacidade | Exercícios usam dados fictícios e registros mínimos. | Áudio bruto e histórico pessoal não são distribuídos; o aluno escolhe como salvar seu registro. |
| Capacidades do produto | README distingue preparação de pacote, instalação e disponibilidade efetiva. Não afirma que anexar Markdown cria uma skill nem que documentação de voz comprova acesso ao áudio. | Não instalei skills nem auditei seletor, projeto ChatGPT, descoberta de diretórios ou limites atuais de interface. A leitura destas instruções não valida funcionamento do produto. |

Na verificação independente de fontes, abri o artigo [Karpicke & Roediger (2008)](https://learninglab.psych.purdue.edu/downloads/2008/2008_Karpicke_Roediger_Science.pdf) e confirmei o experimento com pares de vocabulário e teste posterior; isso sustenta a delimitação cautelosa feita pelo pacote, não uma promessa de conversação ou C2. Abri também [RAE/ASALE — voseo](https://www.rae.es/dpd/voseo), confirmando que o uso varia por região e não deve ser rejeitado em bloco.

A página da [Académie française](https://www.dictionnaire-academie.fr/article/QDL058) abriu inicialmente e seu resultado de busca institucional explicitou contrações e usos de `en`; tentativas posteriores de localizar/reabrir o trecho retornaram timeout. O endereço de [Lyster & Ranta](https://www.cambridge.org/core/journals/studies-in-second-language-acquisition/article/abs/corrective-feedback-and-learner-uptake/59229F0CA2F085F5F5016FB4674877BF) abriu inicialmente, mas a consulta específica ao trecho retornou HTTP 429; não atribuo a esta revisão uma nova leitura integral do artigo nem confirmação integral de seu método. Não usei páginas secundárias de resultados de busca para sustentar correções linguísticas.

## Fechamento e evidência do estado final

Os 13 cenários passaram dentro do escopo de um turno docente simulado por caso. As três falhas de texto detectadas tiveram correções verificadas; as regressões adicionais passaram. Nenhum progresso fictício entrou no registro do aluno. A checagem final de `learning-progress.json` mostrou revisão 0, idioma ativo nulo e zero evidências em cada um dos três idiomas.

SHA-256 do modelo inicial inspecionado: `C6A87DF44088353270A3729906A698B650C411874B86D6065B53E15FD80750D2`.

Permanecem fora do alcance desta revisão: eficácia com alunos reais, retenção ao longo de dias, avaliação acústica, persistência entre conversas, instalação dos pacotes e robustez contra variação de modelos. O relatório dá evidência revisável de comportamento simulado e da qualidade dos textos; não substitui esses testes.
