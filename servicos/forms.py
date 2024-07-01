from django.forms import ModelForm
from .models import Servico, CategoriaManutencao

''' Quando eu faço a instancia no servicoForm la na minha views eu chamo a classe a abaixo
assim ela vai tambem pegar o meu metodo init onde configuramos com mais detalhes as fields 
'''
class ServicoForm(ModelForm):
    # Classe de configuração
    class Meta:
        model = Servico
        # dentro da fields eu posso colocar o exclude e digo quais que nao quero para meu formulario
        exclude = ['finalizado', 'protocolo']

    ''' Para acessar as filds que o django ja configura automaticamente para min eu uso o metodo __init__ 
    onde vou va minha classe pai que no caso é o ModelForm(linha 7) utilizando o super e tendo acesso aos inputs(fields) 
    que o django coloca automaticamente'''

    '''Se dermos um print(self.fields) vamos poder ver todos os fields(inputs/campos)'''

    '''Depois chamamos uma fields especifica na qual chamamos pela chaves desntro do colchete ficando
    self.fields['titulo'], ou seja estou pegando referente a field titulo que eu criei
    
    o widget - self.fields['titulo'].widget: nesse caso aqui estou indo mais afundo na minha field querendo
    pegar o atributo dela que se dermos um print(self.fields['titulo'].widget vamos ver que ele é um text
    e vai ser isso que vai aparecer na tela
    
    self.fields['titulo'].widget.attrs: quando eu coloco outo metodo que é o attrs eu de fato entro na parte 
    de atributos daquele field se dermos um print(self.fields['titulo'].widget.attrs) vamos ver os atributos 
    desse field, e ae vamos perceber que ele so tem o maxlength como atributo
    
    self.fields['titulo'].widget.attrs.update({'class': "form-control"}: com o update estou adicionando
    um novo atributo a minha field que no casso é uma class 
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            #print(self.fields['titulo'].widget.attrs.update({'class': 'form-control'}))
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'placeholder': field})

            """Pegamos da model categoria_manutencao que é o choice desta model
            e depois passamos para um for onde podemos pegar a descricção de cada choice
            
            podemos subscrever o choice assim: self.fields['categoria_manutencao'].choices=
            (( '1', 'Teste' ), ('2', 'Teste2'), ('3','teste3'))

            
            """
            #self.fields['categoria_manutencao'].choices=(('1', 'Teste'), ('2', 'Teste2'), ('3', 'teste3'))

        choices = list()

        for i, j in self.fields['categoria_manutencao'].choices:
            #Estamos alocando em categoria os titulos do choice pelo j na qual esta recebendo os titulos como tvm,b e etc
            """Dentro do django por baixos dos panos quando criamos o choices dentro de uma model ele cria 
            um metdo chamado get nome do campo e display
            
            nesse caso ele aqui seria get titulo_display pegando a descrição do choice
            
            e vamos colocar numa lista essas descrição
            
            """
            categoria = CategoriaManutencao.objects.get(titulo=j)
            choices.append((i.value, categoria.get_titulo_display()))

            self.fields['categoria_manutencao'].choices = choices



