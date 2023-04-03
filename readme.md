# NoBanco

Descrição breve do projeto.

## Requisitos

- Python 3.x
- Django 3.x

## Instalação

1. Clone o repositório em sua máquina local:

   `git clone https://github.com/eugeogeo/api-nobanco.git`

2. Instale as dependências:

   `pip install -r requirements.txt`

## Configuração

1. Crie o banco de dados:

   `python manage.py migrate`

2. Crie um superusuário:

   `python manage.py createsuperuser`

3. Execute o servidor:

   `python manage.py runserver`

4. Acesse a aplicação em seu navegador em http://localhost:8000/.

## Endpoints

Liste os endpoints disponíveis na sua API e suas descrições.

## Testes

Para rodar os testes, execute o seguinte comando na raiz do projeto:

   `python manage.py test` ou `python3 manage.py test`
   
Esse comando vai rodar todos os testes da sua aplicação e exibir o resultado no console. Certifique-se de que o ambiente de teste esteja configurado corretamente antes de rodar os testes.

## Licença

Este projeto é licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE.md) para mais informações.
