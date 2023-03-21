from django.shortcuts import render, redirect
from .compra import Compra

def lista_compra(request):
    compras = Compra.objects.all()
    return render(request, 'lista_compra.html', {'compras': compras})

def detalhe_compra(request, id):
    compra = Compra.objects.get(id=id)
    return render(request, 'detalhe_compra.html', {'compra': compra})

def criar_compra(request):
    if request.method == 'POST':
      valor = request.POST.get('valor')
      tipo_conta = request.POST.get('tipo_conta')
      data = request.POST.get('data')
      return redirect('lista_compra')
    return render(request, 'criar_compra.html')

def atualiza_compra(request, id):
    compra = Compra.objects.get(id=id)
    if request.method == 'POST':
      valor = request.POST.get('valor')
      tipo_conta = request.POST.get('tipo_conta')
      data = request.POST.get('data')
      compra.valor = valor
      compra.tipo_conta = tipo_conta
      compra.data = data
      compra.save()
      return redirect('lista_compra')
    return render(request, 'atualiza_compra.html', {'compra': compra})
      
def delete_compra(request, id):
  compra = Compra.objects.get(id=id)
  compra.delete()
  return redirect('lista_compra')
      