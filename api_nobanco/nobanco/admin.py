from django.contrib import admin
from nobanco.models.usuario.usuario import Usuario
from nobanco.models.saldo.saldo import Saldo
from nobanco.models.contaGeral.contaGeral import ContaGeral
from nobanco.models.compra.compra import Compra

admm = admin.site.register(Usuario)
admm = admin.site.register(Saldo)
admm = admin.site.register(ContaGeral)
admm = admin.site.register(Compra)
