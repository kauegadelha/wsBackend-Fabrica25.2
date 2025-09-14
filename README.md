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
- Usuário comum pode apenas visualizar os animes e gêneros.
- Admin pode se cadastrar no servidor e manipular todas as informações do CRUD.
- Informações complementares do anime (como sinopse e data de lançamento) são preenchidas automaticamente via API pública Jikan.

## Endpoints da API
* principais endpoints:
- /animes/ . Método: GET. Descrição: Lista todos os animes.
- /animes/ . Método: POST. Descrição: Adiciona um novo anime à lista. (somente admin)
- /animes/{id}/ . Método: GET. Descrição: Detalhes de um anime em específico.
- /animes/{id}/ . Métodos: PUT, PATCH. Descrição: Atualiza um anime existente. (somente admin)
- /animes/{id}/ . Método: DELETE. Descrição: Remove um anime da lista. (somente admin)
- /generos/ . Métodos: GET/POST. Descrição: Lista e adiciona gêneros. (POST apenas admin)
- /generos/{id}/ . Métodos: GET/PUT/PATCH/DELETE: Detalhes e manipulação de um gênero. (somente admin)

## API Pública Jikan
- Utilizada para complementar os dados dos animes cadastrados.
- Fornece detalhes adicionais do anime, como sinopse e data de lançamento.

## Como rodar o projeto
1. Abra o terminal.
2. Navegue até a pasta do projeto usando: cd MeuProjeto.
3. Crie o ambiente virtual (venv) com o comando: python -m venv venv.
4. Ative a venv:
      * No Windows, execute: ./venv/scripts/activate.
        * Se não ativar, rode: Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned, e depois: ./venv/scripts/activate.
      * No Linux/macOS, rode: source venv/bin/activate.
5. Instale as dependências do projeto com: pip install -r requirements.txt.
6. Crie o banco de dados e aplique as migrações com: python manage.py migrate.
7. (Opcional) Para criar um superusuário (admin), execute: python manage.py createsuperuser. Em seguida, insira o nome de usuário (ex.: admin), e-mail (ex.: admin@admin.com) e senha (ex.: admin).
8. Para rodar o servidor, utilize: python manage.py runserver.

## Login Admin na API
- Para acessar a interface da API como administrador, clique em "Login" no canto superior direito da página.  
- Caso não encontre o botão, utilize diretamente o endpoint do admin na interface: /admin/.  
- Após logar como admin, você terá permissão para realizar todas as operações CRUD.  
- Usuários comuns poderão apenas visualizar os dados, sem capacidade de modificar nada.

## Recomendação na experiência da API
1. Crie o superusuário (admin) para ter acesso completo às operações CRUD.
2. Faça o login admin na api.
3. Adicione primeiro o gênero. 
4. Depois adicione o anime, colocando o título (campo obrigatório) e selecionando o gênero criado.

* Exemplo:
- Criar gênero: Action.
- Criar anime: Naruto, selecionar Action.

