from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Clientes, Carros
import re #Importando para usar expresão regular
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
# Create your views here.

''' antes do igual são as estruturas da models, no caso esta pegando direto os atibutos da models e depois de iguais 
são os inputs que colocamos no clientes.html.

Ou seja esta os inputs do clientes.html esta colocando os valores digitados nos atibutos do models para salvar no banco
 
'''


def clientes(request):
    if request.method == 'GET':
        clienteLista = Clientes.objects.all()
        return render(request, 'clientes.html', {"cliente": clienteLista})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carros = request.POST.getlist('carro')
        placas = request.POST.getlist('placa')
        anos = request.POST.getlist('ano')

        '''
        No trecho de código cliente = Clientes.objects.filter(cpf=cpf), está sendo feita uma consulta 
        ao banco de dados para recuperar um objeto do tipo Clientes que tenha o atributo cpf igual ao
        valor especificado em cpf.'''

        cliente = Clientes.objects.filter(cpf=cpf)

        '''cliente: Esta é a variável que armazena o resultado da consulta ao banco de dados. 
        Ela contém uma queryset que pode conter zero, um ou mais objetos do modelo Clientes, 
        dependendo dos critérios de filtragem.
        .exists(): O método exists() é usado para verificar se há algum objeto na queryset. 
        Se houver pelo menos um objeto na queryset, o método exists() retornará True; caso contrário, retornará False.

        Portanto, if cliente.exists(): está verificando se a queryset cliente contém algum objeto. Se existir pelo menos 
        um objeto com o CPF fornecido na queryset, a condição será avaliada como verdadeira e o bloco de código 
        dentro do if será executado. Caso contrário, se não houver nenhum objeto com o CPF fornecido, a condição será 
        avaliada como falsa e o bloco de código dentro do if será ignorado.'''

        if cliente.exists():
            '''Neste trecho de codigo no final dele estou colocando os valores que a pessoa digito e cada varaivel 
            respectiva para enviar para value do formulario, ou seja quando a pessoa erra neste caso aqui o cpf 
             o formulario vai volta com todos os campos preenchidos porem o unico campo preenchido que não voltara é o cpf'''
            return render(request, 'clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'carros': zip(carros, placas, anos)})

        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            return render(request, 'clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'cpf': cpf, 'carros': zip(carros, placas, anos)})


        #Cliente esta pegando dos input que fizemos do clientes html no metodo POST e colocando nos atibutos referentes
        #na model
        cliente = Clientes(
            nome=nome,
            sobrenome=sobrenome,
            email=email,
            cpf=cpf
        )

        """Explixação rapida sobre zip iterator
            
            sintaxe:zip(it1,it2)
            faz com que uma lista se correlacione it1 = [1, 2, 3] it2 = [A, B, C] o zip ira junta
            [(1, 'A'), (2, 'B'), (3, 'C')] lista e dentro tem uma tupla 
        
        """

        cliente.save()

        for carros, placas, anos in zip(carros, placas, anos):
            # Essa coluna cliente vai ser igual a que foi salva na linha 37 ou seja o usuario que foi salvo
            car = Carros(
                carro=carros, placa=placas, ano=anos, cliente=cliente
            )
            car.save()

        return render(request, 'clientes.html')


def att_cliente(request):
    #Esse id pego do js(linha 47) onde ele me envia essa  informação por uma request ajax onde cria toda a request, e recebo ela aqui
    id_cliente = request.POST.get('id_cliente')
    cliente = Clientes.objects.filter(id=id_cliente)

    #Estou pegando aqui o object do carro
    carros = Carros.objects.filter(cliente=cliente[0])

    '''serializers faz parte da biblioteca onde consequimos converte uma variavel qualquel 
    para um arquivo seja xml ou json
    
    importamos um o jason la em cima e agora a com a parte do codigo escrita json.loads podemos converter para um json 
    de fato 
       
    cliente_json = json.loads(serializers.serialize('json', cliente))[0]['fields']#pegando só os fields
    nessa linha de codigo estamos pegando [0], porque como estamos preocurando pela id do cliente eu so preciso achar
    na primeira ocoreencia, poque so existe uma id, diferente do carros_json que sao varios carros para uma pessoa 
    
    '''
    #Extrai so o id do cliente no select
    cliente_id = json.loads(serializers.serialize('json', cliente))[0]['pk']

    #Extrai as informaçoes dos clientes no select
    cliente_json = json.loads(serializers.serialize('json', cliente))[0]['fields']#pegando só os fields

    #Extrai o carro do clioente referente no select
    carros_json = json.loads(serializers.serialize('json', carros))

    #convertendo para lista, e pegando só um campo especifico utlizando o for
    carros_json = [{'fields': carro['fields'], 'id': carro['pk']} for carro in carros_json]
    print(carros_json)

    #aqui juntamos  o cliente_json e carrros_json para um lista so especifica
    data = {'clientes': cliente_json, 'carros': carros_json, 'cliente_id': cliente_id}

    return JsonResponse(data)

"""Puxando esse form la no JS da div_carros e passando todas as informações que ja estao cadastrada
e enviando uma request para ca com esse formulario, porque a pessoa vai poder atualizar e mandar para ca para atualizar

Esse @csrf_exempt serve quando um formulario enviar uma request nao vai ter problema, o csrd token nao precisa porque
nesse formulario não tem necessidade
"""

@csrf_exempt
def update_carro(request, id):
    nome_carro = request.POST.get('carro')
    placa = request.POST.get('placa')
    ano = request.POST.get('ano')

    #Essa id foi passada pelo meu parametro la no jS no form action e caiu aqui nesse meu parametro da função
    carro = Carros.objects.get(id=id)
    lista_carros = Carros.objects.filter(placa=placa).exclude(id=id)
    if lista_carros.exists():
        return HttpResponse('Placa ja existente')

    carro.carro = nome_carro
    carro.placa = placa
    carro.ano = ano
    carro.save()


    return HttpResponse('Dados alterados com sucesso')


def excluir_carro(request, id):
    try:
        carro = Carros.objects.get(id=id)
        carro.delete()
        #Redirecionando para minha url clientes
        return redirect(reverse(clientes)+f'?aba=att_cliente&id_cliente={id}')

    except:
        #Colocar mensagem de erro
        return redirect(reverse(clientes)+f'?aba=att_cliente&id_cliente={id}')


def update_cliente(request, id):
    #Enviar via json para meu java script fazendo que quando a pessoa click no nome ele ja apareça todas aas informações
    body = json.loads(request.body)

    nome = body['nome']
    sobrenome = body['sobrenome']
    cpf = body['cpf']
    email = body['email']

    #pegando o id referente a minha tabela cliente
    cliente = get_object_or_404(Clientes, id=id)

    try:
        cliente.nome = nome
        cliente.sobrenome = sobrenome
        cliente.email = email
        cliente.cpf = cpf
        cliente.save()

        return JsonResponse({'status':200 ,'nome': nome , 'sobrenome':sobrenome, 'email':email, 'cpf':cpf})

    except:
        return JsonResponse({'status':500})


