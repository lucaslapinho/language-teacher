# Instalação e primeira aula

## ChatGPT: plugin

1. Abra a [última versão publicada](https://github.com/lucaslapinho/language-teacher/releases/latest).
2. Baixe o arquivo **Language-Teacher-Plugin.zip** na lista de assets da versão.
3. Na interface que oferece adicionar/importar plugin, selecione esse ZIP, sem extrair.
4. Confirme que Language Teacher aparece com três skills: inglês, francês e espanhol.
5. Selecione o plugin em uma conversa e envie: “Quero uma aula de inglês de 15 minutos.”

O plugin oferece instruções e materiais; não conecta serviços externos nem inclui MCP ou executáveis. A disponibilidade da importação depende da interface e da conta. Esta publicação no GitHub não instala automaticamente o plugin.

Use o asset preparado da versão. O ZIP automático “Source code” do GitHub é o código completo do repositório; o ZIP **Language-Teacher-Project.zip** contém materiais para configuração manual. Eles têm finalidades diferentes do plugin importável.

## ChatGPT: arquivos de projeto

Se preferir usar instruções e arquivos:

1. Baixe **Language-Teacher-Project.zip** e extraia.
2. Crie ou abra um projeto Language Teacher.
3. Cole `project-instructions.md` nas instruções do projeto.
4. Adicione `teacher-core.md`, os três arquivos de professor, `learning-progress.json`, `progress-format.md` e `references.md` como fontes acessíveis ao chat.
5. Peça que o professor use os arquivos e inicie uma aula no idioma escolhido.

As instruções permanentes estão abaixo de 7.500 caracteres. Se houver limite de anexos, use o núcleo, o especialista do idioma e o registro. Um arquivo anexado não se torna automaticamente uma skill instalada.

## Codex: skills individuais

As pastas em `skills/` são independentes. Copie a pasta do professor desejado para uma localização de skills reconhecida pela sua instalação, preservando `SKILL.md`, `agents/`, `references/` e `assets/`. Consulte a [documentação oficial](https://learn.chatgpt.com/docs/build-skills) para as localizações e a interface da sua versão.

Confirme que a skill aparece no seletor. Quando a interface suportar menções por nome, use `$language-english-teacher`, `$language-spanish-teacher` ou `$language-french-teacher`. Esses identificadores são diferentes dos atalhos textuais de aula.

## Atualização e retomada

Guarde seu progresso fora do repositório e dos modelos de distribuição. Ao atualizar uma skill, preserve o registro pessoal. No retorno, anexe a versão recente e peça: “Continue meu espanhol usando este registro.” Sem registro, o professor deve declarar a lacuna e oferecer uma pequena tarefa de reentrada.

## Se aparecer erro na importação

Confirme que selecionou **Language-Teacher-Plugin.zip** dos assets da versão. O pacote deve conter uma única raiz `language-teacher/`, manifestos, `skills/` e `assets/`. Não remova pastas ocultas nem compacte apenas os arquivos Markdown.

Se o erro continuar, registre a versão do pacote e os detalhes exibidos pela interface. Os validadores locais conferem regras de embalagem; não reproduzem permissões da conta ou a validação remota. Referências: [empacotamento oficial](https://developers.openai.com/plugins/build/plugins) e [erros de submissão](https://developers.openai.com/plugins/deploy/submission-errors).
