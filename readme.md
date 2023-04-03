# NoBanco

É um sistema que gerencia contas bancárias e transações financeiras. Ele permite que os usuários criem e gerenciem suas contas, consultem seus saldos e histórico de transações, bem como realizem compras e atualizem suas informações de perfil. A API é implementada em Python e usa o framework Django em conjunto com o Django REST framework para gerenciar os endpoints da API, banco de dados e lógica de negócios.

## Requisitos

- Python 3.x
- Django 3.x
- Django REST Framework

## Instalação

1. Clone o repositório em sua máquina local:

   `git clone https://github.com/eugeogeo/api-nobanco.git`

2. Instale as dependências:

   `pip install -r requirements.txt`

3. Instale o Django REST Framework:

   `pip install djangorestframework`

4. Configure o banco de dados:

   `python manage.py migrate`

5. Crie um superusuário:

   `python manage.py createsuperuser`

6. Execute o servidor:

   `python manage.py runserver`

7. Acesse a aplicação em seu navegador em http://localhost:8000/.


## Endpoints

Lista todos os usuários cadastrados: `/userList/`.

Permite visualizar, atualizar um usuário específico:`/updateUser/<int:pk>/`.

Permite criar uma nova conta: `/createUser/`.

Permite visualizar e excluir uma conta específica: `/deleteUser/<int:pk>/`.


## Testes

Para rodar os testes, execute o seguinte comando na raiz do projeto:

   `python manage.py test` ou `python3 manage.py test`
   
Esse comando vai rodar todos os testes da sua aplicação e exibir o resultado no console. Certifique-se de que o ambiente de teste esteja configurado corretamente antes de rodar os testes.

## Licença

Este projeto é licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE.md) para mais informações.
