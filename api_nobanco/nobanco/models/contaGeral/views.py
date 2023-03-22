from django.shortcuts import render, redirect
from .contaGeral import ContaGeral

def lista_contaGeral(request):
    contasGerais = ContaGeral.objects.all()
    return render(request, 'lista_contaGeral.html', {'contasGerais': contasGerais})

def detalhe_contaGeral(request, id):
    contaGeral = ContaGeral.objects.get(id=id)
    return render(request, 'detalhe_contaGeral.html', {'contaGeral': contaGeral})

def criar_contaGeral(request):
    if request.method == 'POST':
      valor = request.POST.get('valor')
      tipo_conta = request.POST.get('tipo_conta')
      return redirect('lista_contaGeral')
    return render(request, 'criar_contaGeral.html')

def atualiza_contaGeral(request, id):
    contaGeral = ContaGeral.objects.get(id=id)
    if request.method == 'POST':
      valor = request.POST.get('valor')
      tipo_conta = request.POST.get('tipo_conta')
      contaGeral.valor = valor
      contaGeral.tipo_conta = tipo_conta
      contaGeral.save()
      return redirect('lista_contaGeral')
    return render(request, 'atualiza_contaGeral.html', {'contaGeral': contaGeral})
      
def delete_contaGeral(request, id):
  contaGeral = ContaGeral.objects.get(id=id)
  contaGeral.delete()
  return redirect('lista_contaGeral')
      