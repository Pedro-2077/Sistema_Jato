## Sistema de Clientes e Serviços em Django

**1. Introdução**

Este readme documenta o sistema de clientes e serviços desenvolvido em Django. O sistema permite cadastrar, atualizar e excluir clientes, além de cadastrar e gerenciar seus carros. Também é possível cadastrar novos serviços e listar os serviços já cadastrados.

<div align="center">
<img src="https://github.com/Pedro-2077/Sistema_Jato/assets/139086553/d0b9dd0a-23db-4e54-a834-83099cd45697" width="1000px"> 
</div>
<br><br>

<div align="center">
<img src="https://github.com/Pedro-2077/Sistema_Jato/assets/139086553/31f5e2c6-388b-4b81-879b-0e1573b40151" width="1000px"> 
</div>

<br><br>

<div align="center">
<img src="https://github.com/Pedro-2077/Sistema_Jato/assets/139086553/7b67fc06-237b-4620-b596-78a44af57183" width="1000px"> 
</div>

<br><br>

**2. Tecnologias Utilizadas**

* Django: framework web full-stack para Python
* HTML: linguagem de marcação para estruturação do conteúdo das páginas
* CSS: linguagem de estilização para formatação visual das páginas
* JavaScript: linguagem de script para interação do usuário com as páginas

**3. Funcionamento do Sistema**

**3.1 Cadastro de Clientes**

* O usuário acessa a página de cadastro de clientes e preenche os campos com as informações do cliente, como nome, sobrenome, CPF, e-mail e carros.
* O sistema valida os dados informados e, se tudo estiver correto, salva o cliente no banco de dados.
* O cliente pode cadastrar um ou mais carros, informando o modelo, placa e ano de cada um.

**3.2 Atualização de Clientes**

* O usuário acessa a lista de clientes e seleciona o cliente que deseja atualizar.
* O sistema exibe os dados do cliente e permite que o usuário os edite.
* O usuário salva as alterações e o sistema atualiza os dados do cliente no banco de dados.

**3.3 Exclusão de Clientes**

* O usuário acessa a lista de clientes e seleciona o cliente que deseja excluir.
* O sistema confirma se o usuário realmente deseja excluir o cliente e, em caso afirmativo, exclui o cliente do banco de dados.

**3.4 Cadastro de Serviços**

* O usuário acessa a página de cadastro de serviços e preenche os campos com as informações do serviço, como nome, descrição, categoria, data de início e data de término.
* O sistema salva o serviço no banco de dados.

**3.5 Listagem de Serviços**

* O usuário acessa a página de listagem de serviços e visualiza a lista de todos os serviços cadastrados.
* A lista de serviços pode ser filtrada por categoria, data de início ou data de término.

**4. Estrutura do Projeto**

O projeto está organizado da seguinte forma:

* `clientes/`:
    * `models.py`: define os modelos de dados para clientes e carros
    * `views.py`: contém as views para gerenciamento de clientes e carros
    * `urls.py`: define as URLs para acesso às views de clientes e carros
* `servicos/`:
    * `forms.py`: contém o formulário de cadastro de serviços
    * `models.py`: define o modelo de dados para serviços
    * `views.py`: contém as views para gerenciamento de serviços
    * `urls.py`: define as URLs para acesso às views de serviços
* `manage.py`: script para gerenciamento do projeto Django
* `requirements.txt`: arquivo com as dependências do projeto

**5. Instalação e Execução**

Para instalar e executar o sistema, siga as seguintes etapas:

1. Clone o repositório do projeto:

```bash
git clone https://github.com/seu-repositorio/sistema-clientes-servicos.git
```

2. Acesse a pasta do projeto:

```bash
cd sistema-clientes-servicos
```

3. Crie um ambiente virtual e ative-o:

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

5. Execute o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```

6. Acesse o sistema em seu navegador web:

```
http://localhost:8000/
```

**6. Considerações Finais**

Este readme é apenas um guia básico para o sistema de clientes e serviços. Para mais informações, consulte a documentação do Django e a documentação dos demais frameworks e bibliotecas utilizados.

**7. Recursos Adicionais**

* Documentação do Django: [https://www.djangoproject.com/](https://www.djangoproject.com/)
* Documentação do HTML: [https://www.w3schools.com/tags/](https://www.w3schools.com/tags/)
* Documentação do CSS: [https://www.w3schools.com/cssref/index.php](https://www.w3schools.com/cssref/index.php)
* Documentação do JavaScript: [https://www.w3schools.com/jsref/jsref_reference.asp](https://www.w3schools.com/jsref/jsref_reference.asp)



