from django.shortcuts import render, redirect
from .usuario import Usuario

def lista_usuario(request):
    usuarios = Usuario.objects.all()
    return render(request, 'lista_usuario.html', {'usuarios': usuarios})

def detalhe_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, 'detalhe_usuario.html', {'usuario': usuario})

def criar_usuario(request):
    if request.method == 'POST':
      cpf = request.POST.get('cpf')
      email = request.POST.get('email')
      celular = request.POST.get('celular')
      nome = request.POST.get('nome')
      senha = request.POST.get('senha')
      return redirect('lista_usuario')
    return render(request, 'criar_usuario.html')

def atualiza_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'POST':
      email = request.POST.get('email')
      celular = request.POST.get('celular')
      nome = request.POST.get('nome')
      senha = request.POST.get('senha')
      usuario.email = email
      usuario.celular = celular
      usuario.nome = nome
      usuario.senha = senha
      usuario.save()
      return redirect('lista_usuario')
    return render(request, 'atualiza_usuario.html', {'usuario': usuario})
      
def delete_usuario(request, id):
  usuario = Usuario.objects.get(id=id)
  usuario.delete()
  return redirect('lista_usuario')
      