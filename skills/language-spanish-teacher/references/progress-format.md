# Contrato do registro portátil — versão 1.0

`learning-progress.json` contém somente estado inicial. O arquivo não executa revisão, não envia notificações nem cria memória automática. Dados novos devem vir de interações reais e de uma gravação confirmada ou de uma versão entregue ao aluno para salvar.

## Campos e tipos

- `schema_version`: texto `1.0`; `record_revision`: inteiro, inicialmente 0, incrementado a cada atualização real.
- `updated_at`: data/hora ISO 8601 com fuso, ou `null` antes da primeira atualização. Use data real conhecida. Se a hora exata não for conhecida, registre data `AAAA-MM-DD` e explicite essa precisão; nunca fabrique horário.
- `timezone`: fuso do aluno; inicial `America/Sao_Paulo`. `active_language`: `en`, `es`, `fr` ou `null`.
- `learner.preferences_from_request`: preferências fornecidas pelo usuário; não são evidências de proficiência. `additional_preferences`: objeto para preferências posteriores explícitas.
- `languages`: três objetos independentes `en`, `es`, `fr`. A edição de um não altera os demais.
- `settings`: variante de referência, origem dessa escolha e modo de correção. As referências espanhol/francês são decisões didáticas iniciais, não preferências atribuídas ao aluno.
- `skills`: `listening`, `speaking`, `reading`, `writing`, `pronunciation`, `mediation`. Cada uma contém `status` (`not_assessed`, `insufficient_evidence`, `informal_estimate`), `estimated_cefr` (`null`, `A1`…`C2` ou faixa adjacente como `A2–B1`), `confidence` (`null`, `low`, `medium`), `evidence_ids` (lista), `last_assessed_at` (data ou `null`) e `limitations` (lista). Não usar `high` para inferir confiança de exame formal a partir de conversa.
- `objectives`: itens com `id`, `description`, `status` (`planned`, `practiced`, `demonstrated`, `retained`), `evidence_ids`. `retained` requer evidência independente em ocasião posterior; o professor pode avançar uma tarefa enquanto retenção está pendente.
- `practiced_content`: itens com `description`, `session_id`, `evidence_ids`.
- `recurrent_errors`: itens com `pattern`, `examples`, `evidence_ids`, `last_seen_at`, `status`. Só marcar recorrência com mais de uma ocorrência; uma hipótese fica em observação da sessão.
- `vocabulary`: itens com `expression`, `meaning_pt_br`, `context`, `accepted_variants`, `evidence_ids`. Registrar frases e combinações úteis realmente praticadas.
- `evidence`: itens com `id`, `language`, `observed_at`, `target_skill`, `task`, `modality`, `audio_access`, `support`, `sample`, `result`, `limitations`. `modality`: `text`, `audio`, `image_and_text`, `audio_and_text`. `audio_access`: `none`, `transcript_only`, `original`. `support`: `none`, `hint`, `model`, `translation`, `transcript`, `mixed`. A amostra é trecho mínimo relevante, sem dados confidenciais.
- `sessions`: itens com `id`, `language`, `date`, `objective_ids`, `evidence_ids`, `summary`, `next_step`. Duração é opcional, apenas observada/fornecida; não preencher com a duração anunciada da aula como se fosse medição.
- `next_step`: descrição curta ou `null`.
- `gamification`: `enabled` booleano; `points` inteiro não negativo; `events` e `achievements` listas. Pontos iniciais 0 significam estado vazio. Eventos reais devem informar `session_id`, `objective_id`, `category`, `points`, `evidence_ids`; seguir teto e categorias do núcleo.

## Item de revisão

Cada objeto de `review_items` tem os campos abaixo. Este é um contrato de formato, não uma revisão já realizada.

| Campo | Tipo e uso |
|---|---|
| `id` | Texto único dentro do idioma, prefixado por `en-`, `es-` ou `fr-`. |
| `language` | Código igual ao ramo que contém o item. |
| `prompt` | Estímulo sem gabarito embutido. |
| `expected_response` | Resposta de referência para o professor; não única formulação aceitável. |
| `accepted_variants` | Lista de respostas/condições semanticamente válidas. |
| `context` | Situação e intenção comunicativa. |
| `target_skill` | Habilidade efetivamente trabalhada. |
| `last_attempt_at` | Data da última tentativa real ou `null`. |
| `last_result` | `independent`, `with_hint`, `after_model`, `incorrect`, `not_attempted` ou `null`. |
| `next_review_suggested` | Data `AAAA-MM-DD` ou `null`; sem data confiável, usar intervalo relativo em nota. |
| `interval_days` | Inteiro não negativo ou `null`; sugestão, não prazo garantido. |
| `attempts` | Lista com `attempted_at`, `observed_response`, `support`, `result`, `evidence_id`. |
| `scheduling_note` | Justificativa breve para intervalo e contexto, sem prometer algoritmo SRS implementado. |

Uma tentativa com transcrição pode sustentar comentário lexical, mas não pronúncia. Evidência de escuta descreve o áudio apresentado, acesso e apoio; evidência de fala descreve o áudio do aluno acessível. Não confundir os dois.

## Atualização segura e portabilidade

Leia a versão disponível antes de editar. Acrescente evidências/tentativas em vez de reescrever o passado. Preserve estimativas anteriores nas observações de sessão ao revisar a faixa. Para conflitos de versões, preserve ambas até esclarecer. Não cole demonstrações em listas reais.

O validador em `scripts/validate.py` verifica a integridade inicial e separação dos idiomas. Não é um banco de dados nem garante a qualidade de futuras avaliações. Ao manter histórico real, valide também as novas referências entre IDs e as condições descritas neste contrato; mantenha uma cópia anterior antes de substituir arquivos.
