# Bookstore API

API de gerenciamento de livraria desenvolvida com Django e Django REST Framework.

## Tecnologias

- Python
- Django
- Django REST Framework
- Docker
- Poetry

## Executando com Docker

Criar a imagem:

docker build -t bookstore .

Executar o container:

docker run -p 8000:8000 bookstore

A aplicação estará disponível em:

http://localhost:8000