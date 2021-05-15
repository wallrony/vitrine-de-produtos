# Vitrine de Produtos

Este é um projeto feito em Django que apresenta uma vitrine de produtos, onde o lojista gerencia os produtos das lojas enquanto os usuarios podem visualiza-los.

## Como Executar?

Siga a lista de comandos abaixo para organizar todas as necessidades e fazer com que a aplicação execute.

Obs.: Este projeto foi criado utilizando o python 3.8. Sugiro que o utilize para evitar conflitos que possam acontecer a partir do versionamento dos pacotes.

```
1. Crie o ambiente virtual do projeto: python3 -m venv venv
2. Ative-o: source venv/bin/activate
3. Instale suas dependências: pip3 install -r requirements.txt
4. Preencha as variáveis de ambiente no arquivo .env que está dentro de "vitrine_produtos" para ter a referência do banco de dados;
5. Crie o banco de dados executando as migrations: python3 manage.py migrate
6. Crie um usuário primário: python3 manage.py createsuperuser
7. Inicie o Servidor: python3 manage.py runserver
```

E pronto, a aplicação estará executando de forma local na porta 8000.

## Rotas da Aplicação

Na raiz do projeto, há um arquivo chamado `Insomnia Workspace.json` que está em formado JSON. Ele pode ser utilizado como 
esquema/configuração das requisições e pode ser utilizado tanto no Insomnia quanto no Postman. 

### Autenticação

Método | Rota | Objetivo
-------|------|---------
POST   | /api/accounts/register | Cadastrar uma nova conta.
POST   | /api/accounts/login    | Realizar autenticação.

#### Objeto de Envio - /api/accounts/register

```json
{
  "name": "Nome",
  "email": "email@email.com",
  "password": "123456",
  "role": 1
}
```

Name: Nome o usuário

Email: Email do Usuário

Password: Senha do usuário

Role: Função do usuário

Essa requisição retorna o seguinte resposta com status 201:

```json
{
  "message": "Conta cadastrada com sucesso!"
}
```

---

#### Objeto de Envio - /api/accounts/login

```json
{
  "email": "email@email.com",
  "password": "123456"
}
```

Email: Email do Usuário

Password: Senha do usuário

Essa requisição retorna o seguinte resposta com status 200:

```json
{
  "auth_token": "Token de Autorização",
  "user": {
    "id": 1,
    "name": "Nome",
    "email": "email@email.com",
    "role": 2
  },
  "created": "2021-05-15T00:00:00.000000Z"
}
```

---

### Categoria

Método | Rota | Objetivo
-------|------|---------
GET    | /api/core/category | Retornar a lista de categorias cadastradas.
POST   | /api/core/category | Adicionar uma nova categoria.
PUT    | /api/core/category/<id> | Atualizar uma categoria existente.
DELETE | /api/core/category/<id> | Excluir uma categoria existente.

#### Objeto de Resposta - (GET) /api/core/category

Status da resposta: 200

```json
[
  {
    "id": 1,
    "name": "Categoria 1",
    "created_at": "2021-05-10T19:32:07.404946Z",
    "updated_at": "2021-05-10T19:32:07.405005Z"
  },
  {
    "id": 2,
    "name": "Categoria 2",
    "created_at": "2021-05-15T00:00:00.000000Z",
    "updated_at": "2021-05-15T00:00:00.000000Z"
  }
]
```

---

#### Objeto de Envio - (POST) /api/core/category

```json
{
  "name": "Categoria 1"
}
```

Essa requisição retorna a seguinte resposta com status 201:

```json
{
  "id": 1,
  "name": "Categoria 1",
  "created_at": "2021-05-15T00:00:00.000000Z",
  "updated_at": "2021-05-15T00:00:00.000000Z"
}
```

---

#### Objeto de Envio - (PUT) /api/core/category/<id>

```json
{
  "name": "Categoria 1"
}
```

Essa requisição não retorna nenhuma resposta com status 200.

---

#### Objeto de Envio - (DELETE) /api/core/category/<id>

Essa requisição não envia nem retorna nenhuma resposta, somente tem status de resposta 200.

---

### Produtos

Método | Rota | Objetivo
-------|------|---------
GET    | /api/core/products | Retornar a lista de produtos cadastrados.
POST   | /api/core/products | Adicionar um novo produto.
PUT    | /api/core/products/<id> | Atualizar um produto existente.
DELETE | /api/core/products/<id> | Excluir um produto existente.

#### Objeto de Resposta - (GET) /api/core/products

Status da resposta: 200

```json
[
  {
    "id": 1,
    "name": "Meu produto",
    "description": "Descrição do Produto",
    "price": 24.99,
    "category": 1,
    "created_at": "2021-05-15T00:00:00.000000Z",
    "updated_at": "2021-05-15T00:00:00.000000Z",
    "images": [
      {
        "id": 1,
        "image": "URL da imagem",
        "created_at": "2021-05-15T00:00:00.000000Z",
        "updated_at": "2021-05-15T00:00:00.000000Z"
      },
      {
        "id": 2,
        "image": "URL da imagem",
        "created_at": "2021-05-15T00:00:00.000000Z",
        "updated_at": "2021-05-15T00:00:00.000000Z"
      }
    ]
  }
]
```

---

#### Objeto de Envio - (POST) /api/core/products

OBS.: Essa resposta deve ser enviada em FormData ao invés de JSON para o envio das imagens, porém considere o exemplo abaixo no formato JSON:

```json
{
  "name": "Produto 1",
  "description": "Descrição do Produto 1",
  "price": 24.99,
  "category": 1,
  "img0": "file da imagem",
  "img1": "file da imagem"
}
```

Obs.: É possível colocar quantas imagens quiser. 

Essa requisição retorna a seguinte resposta com status 201

```json
{
  "id": 1,
  "name": "Meu produto",
  "description": "Descrição do Produto",
  "price": 24.99,
  "category": 1,
  "created_at": "2021-05-15T00:00:00.000000Z",
  "updated_at": "2021-05-15T00:00:00.000000Z",
  "images": [
    {
      "id": 1,
      "image": "URL da imagem",
      "created_at": "2021-05-15T00:00:00.000000Z",
      "updated_at": "2021-05-15T00:00:00.000000Z"
    },
    {
      "id": 2,
      "image": "URL da imagem",
      "created_at": "2021-05-15T00:00:00.000000Z",
      "updated_at": "2021-05-15T00:00:00.000000Z"
    }
  ]
}
```

---

#### Objeto de Envio - (PUT) /api/core/products/<id>

OBS.: Essa resposta deve ser enviada em FormData ao invés de JSON para o envio das imagens, porém considere o exemplo abaixo no formato JSON:

```json
{
  "name": "Produto 1",
  "description": "Descrição do Produto 1",
  "price": 24.99,
  "category": 1,
  "img0": "file da imagem",
  "img1": "file da imagem"
}
```

Obs.: É possível colocar quantas imagens quiser.

Essa requisição não retorna nenhuma resposta com status 200.

---

#### Objeto de Envio - (DELETE) /api/core/products/<id>

Essa requisição não envia nem retorna nenhuma resposta, somente tem status de resposta 200.

---

## Features Presentes

A seguinte lista apresenta as features presentes e disponíveis no Frontend.

- `/` - Visualizar produtos;
- `/manager/login` - Realizar login
- `/manager/products` - Gerenciar produtos
- `/manager/products/add` - Adicionar um produto
- `/manager/products/edit` - Editar um produto
- `/manager/categories` - Gerenciar categorias
