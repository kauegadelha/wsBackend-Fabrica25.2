# wsBackend-Fabrica25.2
- Repositório remoto para o final do desafio do Workshop da Fábrica de Software 2025.2.

## API de Animes 
- Projeto Django com a API de animes.

## Descrição do projeto
- Projeto backend para gerenciamento de animes, com integração à API pública Jikan para complementar informações.

## Tecnologias utilizadas
- Python 3.13.
- Django 5.2.
- Django REST Framework.
- SQLite (banco de dados padrão).
- API pública Jikan.

## Funcionalidades
- CRUD completo para as entidades Anime e Gênero.
- Relação Many-To-Many: um anime pode ter múltiplos gêneros.
- Usuário comum pode realizar operações CRUD.
- Admin pode se cadastrar no servidor e manipular todas as informações do CRUD.
- Informações complementares do anime (como sinopse e data de lançamento) são preenchidas automaticamente via API pública Jikan.

## Endpoints da API
* principais endpoints:
- /animes/ . Método: GET. Descrição: Lista todos os animes.
- /animes/ . Método: POST. Descrição: Adiciona um novo anime à lista.
- /animes/{id}/ . Método: GET. Descrição: Detalhes de um anime em específico.
- /animes/{id}/ . Métodos: PUT, PATCH. Descrição: Atualiza um anime existente.
- /animes/{id}/ . Método: DELETE. Descrição: Remove um anime da lista.
- /generos/ . Métodos: GET/POST. Descrição: Lista e adiciona gêneros.
- /generos/{id}/ . Métodos: GET/PUT/PATCH/DELETE: Detalhes e manipulação de um gênero.

## API Pública Jikan
- Utilizada para complementar os dados dos animes cadastrados.
- Fornece detalhes adicionais do anime, como sinopse e data de lançamento do anime.

## Como rodar o projeto
* Passos a serem seguidos:
- 1. Abra o terminal.
- 2. Navegue até a pasta do projeto usando: cd MeuProjeto.
- 3. Crie o ambiente virtual (venv) com o comando: python -m venv venv.
- 4. Ative a venv:
       * No Windows, execute: ./venv/scripts/activate.
         * Se não ativar, rode: Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned, e depois: ./venv/scripts/activate.
       * No Linux/macOS, rode: source venv/bin/activate.
- 5. Instale as dependências do projeto com: pip install -r requirements.txt.
- 6. Crie o banco de dados e aplique as migrações com: python manage.py migrate.
* (Opcional) Para criar um superusuário (admin), execute: python manage.py createsuperuser. Em seguida, insira o nome de usuário (ex.: admin), e-mail (ex.: admin@admin.com
) e senha (ex.: admin).
- 7. Para rodar o servidor, utilize: python manage.py runserver.

## Recomendação na experiência da API
- 1. Ao rodar o servidor, adicione primeiro o gênero. 
- 2. Depois adicione o anime, colocando o título (campo obrigatório) e selecionando o gênero criado.

* Exemplo:
- Criar gênero: Action.
- Criar anime: Naruto, selecionar Action.
