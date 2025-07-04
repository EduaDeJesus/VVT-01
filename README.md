# 👥 Membros da Equipe

| Nome                               |
|------------------------------------|
| Ronald Ferreira Mendes             |
| Emerson Oliveira Dos Santos        |
| Eduã De Jesus Sorino Da Silva      |

# 📦 GERÊNCIA DE CONFIGURAÇÃO DE SOFTWARE

## 📌 Release e Tag

Para criar uma nova tag e publicar uma release no GitHub, siga os passos abaixo:

### 1️⃣ Criar uma tag localmente
```bash
git tag v1.0.0
```
> Substitua `v1.0.0` pela versão desejada seguindo o versionamento semântico.

### 2️⃣ Enviar a tag para o repositório remoto
```bash
git push origin v1.0.0
```

### 3️⃣ Criar a release no GitHub
1. Vá até a aba **Releases** do repositório no GitHub.
2. Clique em **Draft a new release**.
3. Selecione a tag criada (ex.: `v1.0.0`).
4. Preencha o título e a descrição do release (ex.: changelog resumido).
5. Clique em **Publish release**.

### 📃 Gerar changelog (opcional)
Utilize ferramentas como [git-changelog](https://github.com/github-changelog-generator/github-changelog-generator) ou crie manualmente um arquivo `CHANGELOG.md` com as mudanças.

---

## 🎯 Objetivo

Este projeto tem como objetivo aplicar os conceitos de Gerência de Configuração de Software, com foco em duas atividades principais:

- **Gerenciamento de Mudanças**
- **Controle de Versões**

A avaliação será feita com base na execução e documentação das atividades descritas abaixo, totalizando **nota 10**. A média será composta pelas entregas em cada uma das seções.

---

## 📝 GERENCIAMENTO DE MUDANÇAS – (10 pontos)

### 🔹 Atividade da Equipe
**Modelo de Severidade e/ou Prioridade (3 pontos)**

A equipe deverá discutir, escolher e justificar o modelo que será adotado no projeto. Esse modelo será utilizado para classificar e priorizar as issues ao longo do trabalho.

⚠️ **Importante:** A ausência de uso efetivo do modelo reduzirá a nota da atividade pela metade.

---

### 🔹 Atividades Individuais

Cada integrante deverá:

- Criar **6 Issues com boas práticas (2 pontos)**  
  > Use títulos claros, descrições objetivas e etiquetas apropriadas.

- **Foco em Solução – Comentar uma issue de outro colega (1 ponto)**  
  > O comentário deve conter sugestões úteis para a solução, com possível referência técnica.

- **Foco em Revisão – Revisar uma issue *closed* de outro colega (1 ponto)**  
  > Avaliar se a solução realmente resolve a issue.

- **Foco em Revisão – Comentar com sugestões de ajustes (3 pontos)**  
  > Cada issue deve receber comentários técnicos de dois revisores distintos.

  ⚠️ Comentários genéricos como “concordo” ou “ok” não serão aceitos.

---

## 🔀 CONTROLE DE VERSÕES – (10 pontos)

### 🔹 Modelo de Branching (1,5 pontos)
A equipe deverá discutir e definir um modelo de ramificações, apresentando a estrutura adotada. Exemplos possíveis:

- Git Flow
- GitHub Flow
- Trunk Based Development

---

### 🔹 Commits Semânticos (3 pontos)
A equipe deve seguir as diretrizes de [Commits Semânticos](https://www.conventionalcommits.org/en/v1.0.0/).

**Exemplo de commit válido:**
```
feat: adiciona validação de formulário na tela de login
fix: corrige erro de autenticação com token expirado
```

> Evidências de uso correto deverão ser apresentadas (ex.: `git log --graph`).

---

### 🔹 Atividades Individuais

Cada integrante deverá:

- Criar um novo arquivo no projeto (**0,5 pontos**)
- Alterar um arquivo existente no projeto (**0,5 pontos**)
- Revisar e aprovar um Pull Request de outro colega (**0,5 pontos**)
- Resolver duas issues de outro membro com um único commit/PR (**2 pontos**)
- Resolver pelo menos dois conflitos de merge (**2 pontos**)
  > Documentar brevemente no PR ou em um arquivo `.log` como o conflito foi resolvido.

---

## 📁 EVIDÊNCIAS E ENTREGA

Todas as evidências deverão ser organizadas e entregues em um único arquivo PDF.

No PDF, especifique claramente o responsável por cada tarefa.

Inclua capturas de tela, links diretos para issues, commits, pull requests e logs, se necessário.

---

## 🔒 REPOSITÓRIO

- Criar um repositório privado no GitHub.
- Incluir todos os membros da equipe e o professor como colaboradores.
- **Projeto base:** pode ser um projeto open source ou de disciplinas anteriores.
- **Não utilizar fork.** Faça o download do projeto e suba manualmente no repositório privado.

---

## 🛠️ RECOMENDAÇÕES

Utilize ferramentas gráficas (opcional), como:

- GitKraken
- GitHub Insights
- Extensões como GitLens no VSCode

✅ **Colaboração, engajamento e comunicação entre os membros são essenciais.**

❌ O trabalho não é individual e não haverá prorrogação de prazo.

ℹ️ Poderá haver defesa do trabalho caso haja dúvidas em relação à participação dos integrantes.

---

## 📋 Requisitos do Projeto

Antes de iniciar, verifique se você possui os seguintes requisitos instalados:

- **Git** >= 2.20
- **Node.js** >= 16 (opcional, se forem usados scripts ou automações)
- **VSCode** (ou outro editor de sua preferência)
- Extensões recomendadas:
  - [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)
  - [EditorConfig](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)

---

## 🤝 Como Contribuir

1. **Crie uma branch** a partir de `develop` com um nome descritivo:
   ```
   git checkout -b feature/nome-da-sua-feature
   ```
2. **Siga o padrão de commits semânticos**, por exemplo:
   ```
   feat: adiciona funcionalidade X
   fix: corrige bug Y
   ```
3. **Abra um Pull Request** detalhado para revisão.
4. **Adicione reviewers** e descreva claramente as mudanças.
5. **Resolva conflitos** antes de solicitar a aprovação.

---

## 📝 Licença

Este projeto é de **uso livre** e pode ser utilizado para quaisquer finalidades, incluindo fins comerciais e educacionais.

---

## 📫 Contato

Caso tenha dúvidas ou sugestões, entre em contato:

- Ronald Ferreira Mendes – [GitHub](https://github.com/Ronald-FM/)
- Emerson Oliveira Dos Santos – [GitHub](https://github.com/EmersonOsantos/)
- Eduã De Jesus Sorino Da Silva – [GitHub](https://github.com/EduaDeJesus/)

Ou utilize o repositório para abrir uma issue.

---