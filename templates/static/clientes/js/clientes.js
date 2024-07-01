function add_carro(){

    //Adiciona um carro (inputs na variavel html) dentro de uma div chamada container

    container = document.getElementById('form-carro')

    html = "<br> <div class='row'>  <div class='col-md'> <input type='text' placeholder='carro' class='form-control' name='carro'> </div> <div class='col-md'><input type='text' placeholder='Placa' class='form-control' name='placa'></div> <div class='col-md'> <input type='number' placeholder='Ano' class='form-control' name='ano'> </div> </div>"

    container.innerHTML += html
}

function exibir_form(tipo) {

    add_cliente = document.getElementById('adicionar-cliente')
    att_cliente = document.getElementById('att_cliente')

    // Se tipo que entro nos parametros for igual a 1

    if (tipo == "1"){
        att_cliente.style.display = "none"
        add_cliente.style.display = "block"
    } else if (tipo == "2"){
        add_cliente.style.display = "none"
        att_cliente.style.display = "block"
    }

}

function dados_cliente(){
    cliente = document.getElementById('cliente-select')

    //Criando um metodo

    /*Quando criamos uma requisição enviamos dois tipos de dados que são os
    cabeçalhos e os corpos da requisições

    nesse corpo vai token de segurança,contenti type e outras que vão no corpo
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value/ pegando o csrf_token pelo name

    */

    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    console.log(csrf_token)
    //Criando um simulção de formulario
    id_cliente = cliente.value
    data = new FormData()
    data.append('id_cliente', id_cliente)

    fetch("/clientes/atualizar_cliente/",{
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data
    //then esta respondendo a requeste acima ou seja vai te devolver uma response e vou converte toda a response para json
    }).then(function (result){
        return result.json()
    //Respondendo a request convertido em json
    }).then(function (data){
        //pegando esse dados pela request enviada da view e igualando com os valores correspondentes
        document.getElementById('form-att-cliente').style.display = 'block'

        id = document.getElementById("id")
        id.value = data['cliente_id']

        nome = document.getElementById('nome')
        nome.value = data['clientes']['nome']

        sobrenome = document.getElementById('sobrenome')
        sobrenome.value = data['clientes']['sobrenome']

        cpf = document.getElementById('cpf')
        cpf.value = data['clientes']['cpf']

        email = document.getElementById('email')
        email.value = data['clientes']['email']

        div_carros =document.getElementById('carros')
        div_carros.innerHTML = ""
            console.log(data['carros'])
        for(i=0; i<data['carros'].length; i++){
            //Vendo os carros de cada cliente escolhido no select
            console.log(data['carros'][i]['fields']['carro'])

            /*Aqui eu estou passando um arquivo HTML na minha div que recebeu a id carros, e nesse HTML estou
            pegando as informaçoes do meu carro de cada cliente e colocamdo pelo value cada informação no input do carro
            e cada input tem o atibuto do carro cadastrado, cada div abaixo
            */
            div_carros.innerHTML += "<form action='/clientes/update_carro/" + data['carros'][i]['id'] + "' method='POST'>\
                    <div class='row'>\
                        <div class='col-md'>\
                            <input class='form-control' type='text' name='carro' value='" + data['carros'][i]['fields']['carro'] + "'>\
                        </div>\
                        <div class='col-md'>\
                            <input class='form-control' type='text' name='placa' value='" + data['carros'][i]['fields']['placa'] + "'>\
                        </div>\
                        <div class='col-md'>\
                            <input class='form-control' type='text' name='ano' value='" + data['carros'][i]['fields']['ano'] + "'>\
                        </div>\
                        <div class='col-md'>\
                            <input type='submit' class='btn btn-success' value='Enviar Pedido'>\
                            <a class='btn btn-danger' href='/clientes/excluir_carro/"+ data['carros'][i]['id']+"'>Exculir</a>\
                        </div>\
                        <form>\
                </div><br>"


        }

    })

}
//Pegando tudo isso
function update_cliente(){
    nome = document.getElementById('nome').value
    sobrenome = document.getElementById('sobrenome').value
    email = document.getElementById('email').value
    cpf = document.getElementById('cpf').value
    id = document.getElementById('id').value

    //Pegando a informação do update cliente da minha views

    fetch('/clientes/update_cliente/' + id, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: JSON.stringify({
            nome: nome,
            sobrenome: sobrenome,
            email: email,
            cpf: cpf,
        })

    }).then(function(result){
        return result.json()
    }).then(function(data){
    console.log(data)
        // Mesmo que os valores do update cliente possa ja esta tudo certo aqui pegamos do nosso propio banco para nao haver erros
        //possa ser que deva ter algum erro no envio de request
        if(data['status'] == 200) {
            nome = data['nome']
            sobrenome = data['sobrenome']
            email = data['email']
            cpf = data['cpf']

            console.log('Dados alterados com sucesso')
        }
        else {
            console.log('Dados não cadastrados')
        }
    })


}


