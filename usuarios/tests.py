from django.test import TestCase
from django.core.exceptions import ValidationError
from usuarios.models import Usuario

class UsuarioTestCase(TestCase):
    
    def test_senha_invalida(self):
      with self.assertRaises(ValidationError):
        Usuario.objects.create(
            cpf="111.111.111-11",
            email="teste@teste.com",
            celular="(11) 11111-1111",
            nome="Teste",
            senha="senha_fraca"
        )
    
    def test_senha_valida(self):
      Usuario.objects.create(
          cpf='111.111.111-11',
          email='teste@teste.com',
          celular='(11) 11111-1111',
          nome='Teste',
          senha='Teste123'
      )
      self.assertEqual(Usuario.objects.count(), 1)

