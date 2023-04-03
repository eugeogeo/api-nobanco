from django.test import TestCase
from django.core.exceptions import ValidationError
from users.models import User

class UserTestCase(TestCase):
    
    def test_senha_invalida(self):
      with self.assertRaises(ValidationError):
        User.objects.create(
            cpf="111.111.111-11",
            email="teste@teste.com",
            cellPhone="(11) 11111-1111",
            name="Teste",
            password="senha_fraca"
        )
    
    def test_senha_valida(self):
      User.objects.create(
          cpf='111.111.111-11',
          email='teste@teste.com',
          cellPhone='(11) 11111-1111',
          name='Teste',
          password='Teste123'
      )
      self.assertEqual(User.objects.count(), 1)

