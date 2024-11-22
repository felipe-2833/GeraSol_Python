# Mecânixo Virtual

O foco do projeto é o diagnóstico digital, impulsionado por um assistente
virtual (chatbot), que permite aos usuários relatarem os problemas enfrentados com
seus veículos. A Inteligência Artificial assume o papel do mecânico, agilizando o
processo ao fornecer diagnósticos precisos e encaminhando-os aos profissionais
responsáveis.


## Funcionalidades

- **Cadastro usuario:** Permite cadastrar usuario

- **Login usuario:** Permite o login de usuario cadastrado.

- **Atualizar informações:** O sistema permite a edição das informações do usuario.

- **Ver informações user:** Possibilidade de ver informações do usuario.

- **Download json:** Download de um arquivo json ocm as informações do usuario

- **Conversa com bot para criação de chamado:** Chat bot mockado para pegar informações necessarias para criar chamado para oficina.

- **Criar chamado:** Possibilidade criar chamdo a partir das informações do chatbot.

- **Deletar chamado:** Possibilidade detetar chamados.

- **API java:** Todas as informações são consumidas de uma api craida em java.

- **Banco de Dados Oracle:** Todas as informações são armazenadas e manipuladas através de uma conexão com o OracleDB, garantindo persistência e segurança dos dados.

# GeraSol
O projeto GeraSol é uma solução inovadora desenvolvida para facilitar o acesso à energia solar por meio da venda e aluguel de geradores solares. Nosso sistema permite que usuários explorem diferentes opções de geradores, com características personalizadas, promovendo a sustentabilidade e reduzindo custos de energia.

## Funcionalidades

- **Cadastro de Usuários:** Permite o registro de novos usuários no sistema com informações detalhadas, como nome completo, e-mail, telefone e mais.

- **Login de Usuários:** Acesso seguro ao sistema para usuários cadastrados.

- **Atualização de Informações:** Possibilidade de editar informações pessoais de forma prática e segura.

- **Visualização de Informações do Usuário:** Exibe os detalhes do perfil de usuário, garantindo transparência e facilidade no gerenciamento de dados.

- **Gerenciamento de Geradores:**

- **Catálogo de geradores disponíveis para venda e aluguel.
  - **Filtros para encontrar geradores com base em características como portabilidade, capacidade de bateria e potência.
  - **Simulação de Chatbot para Escolha de Geradores: Um chatbot interativo ajuda os usuários a selecionar o gerador ideal com base em suas preferências.

- **Criação de Pedidos:** Funcionalidade para formalizar a compra ou aluguel de geradores, com registro detalhado no sistema.

- **Transações de Aluguel:** Sistema de gestão de aluguéis, incluindo registro de período, valor diário e status do aluguel.

- **API REST em Java:** Todas as funcionalidades são gerenciadas por meio de uma API REST robusta, desenvolvida em Java, seguindo os padrões modernos de arquitetura.

- **Banco de Dados Oracle:** Persistência e manipulação de dados realizadas com o OracleDB, garantindo segurança e confiabilidade.

## Requisitos

- Python 3.x
- oracledb
- intellij

## Instalação

1. Clone o repositório da api:

```bash
git https://github.com/felipe-2833/GeraSolJava.git
```

2. Abrir no intellij o projeto

3. entrar na pasta /java/main/main.java e dar run 

4. Clone o repositório do projeto:

```bash
git https://github.com/felipe-2833/GeraSol_Python.git
```

5. Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

6. Execute a API no terminal:

```bash
streamlit run home.py
```

Não esqueça de conferir os caminhos (path), para rodar os comandos inicializando a aplicação da forma correta!

## Equipe

- Diego Bassalo Canals - **RM: 558710**
- Felipe Levy Stephens Fidelix - **RM: 556426**
- Samir Hage Neto - **RM: 557260**

