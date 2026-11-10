# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Construa uma API REST para uma biblioteca de livros usando FastAPI. Nesta atividade, você vai criar endpoints HTTP, validar dados com modelos Pydantic e responder a consultas com sucesso ou erro.

## 📝 Tarefas

### 🛠️ Listar os livros

#### Descrição
Use o código inicial para configurar o ambiente e implemente um endpoint que retorne todos os livros cadastrados. Instale o FastAPI com `python -m pip install "fastapi[standard]"`, inicie o servidor com `fastapi dev starter-code.py` e explore a documentação interativa em `http://127.0.0.1:8000/docs`.

#### Requisitos
O programa concluído deve:

- Responder a uma requisição `GET /books` com a lista de livros de exemplo.
- Retornar cada livro como um objeto JSON com `id`, `title` e `author`.
- Usar o modelo de resposta definido no código inicial.

### 🛠️ Cadastrar um livro

#### Descrição
Implemente um endpoint para receber os dados de um livro novo e adicioná-lo à lista em memória. Use o modelo `BookCreate` para validar os dados recebidos.

#### Requisitos
O programa concluído deve:

- Aceitar uma requisição `POST /books` com `title` e `author` em formato JSON.
- Atribuir ao novo livro um `id` que não esteja em uso e adicioná-lo à lista.
- Retornar o livro criado com status HTTP `201`.

### 🛠️ Buscar um livro pelo ID

#### Descrição
Implemente um endpoint que receba o identificador do livro pela rota e procure esse livro na lista.

#### Requisitos
O programa concluído deve:

- Responder a `GET /books/{book_id}` com os dados do livro quando o ID existir.
- Retornar status HTTP `404` com uma mensagem clara quando o livro não for encontrado.
- Permitir testar os casos de sucesso e de ID inexistente pela documentação interativa do FastAPI.
