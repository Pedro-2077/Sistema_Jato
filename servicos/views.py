from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ServicoForm
from .models import Servico

# Create your views here.


def novo_servicos(request):

    if request.method == "GET":
        #Instanciando ele vazio
        form = ServicoForm
        return render(request, 'novo_servico.html', {'form': form})

    elif request.method == "POST":
        # Instanciando ele com informações do meu post
        form = ServicoForm(request.POST or None)

        if form.is_valid():
            form.save()

        else:
            #Caso o formulario não seja valido ele vai volta para mesma pagina com tudo que a pessoa digito deixando em branco so o errado
            return render(request, 'novo_servico.html', {'form': form})

        return render(request, 'novo_servico.html', {'form': form})

        #Vai ver se o formulario é valido de acordo com oque voce coloco na models
        #Se voce deniu exemplo string no model se colocar int nao vai passa na validação
        #Ou se voce define que nao pode ser nulo


def listar_servicos(request):
    if request.method == "GET":
        servicos = Servico.objects.all()
        return render(request, "lista_servicos.html", {'servicos': servicos})


