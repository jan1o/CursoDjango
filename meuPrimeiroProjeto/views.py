from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'index.html')

def articles(request, year):
    return HttpResponse('O ano enviado foi: ' + str(year))

def lerDoBanco(nome):
    lista_nomes = [
        {'id': 0, 'nome': 'Janio', 'idade': 22},
        {'id': 1, 'nome': 'Ana', 'idade': 30},
        {'id': 2, 'nome': 'Pedro', 'idade': 25},
        {'id': 3, 'nome': 'Joaquim', 'idade': 27}
    ]

    for pessoa in lista_nomes:
        print(pessoa)
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return {'nome':'Não encontrado', 'idade': 0}

def fname(request, nome):
    result = lerDoBanco(nome)
    if(result['idade'] > 0):
        return HttpResponse('A pessoa foi encontrada, ela tem ' + str(result['idade']) + ' anos!')
    else:
        return  HttpResponse('Pessoa não encontrada!!!')

def fname2(request, nome):
    idade = lerDoBanco(nome)['idade']
    return render(request, 'pessoa.html', {'v_idade': idade})