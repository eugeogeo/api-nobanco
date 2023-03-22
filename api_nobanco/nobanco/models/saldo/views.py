from django.shortcuts import render, redirect
from .saldo import Saldo

def lista_saldo(request):
    saldos = Saldo.objects.all()
    return render(request, 'lista_saldo.html', {'saldos': saldos})

def detalhe_saldo(request, id):
    saldo = Saldo.objects.get(id=id)
    return render(request, 'detalhe_saldo.html', {'saldo': saldo})

def criar_saldo(request):
    if request.method == 'POST':
      valor = request.POST.get('valor')
      tipo_conta = request.POST.get('tipo_conta')
      data = request.POST.get('data')
      return redirect('lista_saldo')
    return render(request, 'criar_saldo.html')

def atualiza_saldo(request, id):
    saldo = Saldo.objects.get(id=id)
    if request.method == 'POST':
      valor = request.POST.get('valor')
      tipo_conta = request.POST.get('tipo_conta')
      data = request.POST.get('data')
      saldo.valor = valor
      saldo.tipo_conta = tipo_conta
      saldo.data = data
      saldo.save()
      return redirect('lista_saldo')
    return render(request, 'atualiza_saldo.html', {'saldo': saldo})
      
def delete_saldo(request, id):
  saldo = Saldo.objects.get(id=id)
  saldo.delete()
  return redirect('lista_saldo')
      