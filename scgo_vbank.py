# GERENCIAR CLIENTES
# - Função: inserir, alterar, excluir e consultar seus clientes
# - Atributos dos clientes: nome, sobrenome, cpf; email; endereço; telefone; número da conta corrente; limite de crédito (R$1.000,00; Saldo)
# - Observações: inserir um novo cadastro; verificar se o CPF informado já existe (se sim, informar usuário e permitir que os dados já cadastrados sejam alterados pelo gerente); aqueles que quiserem validar o CPF informado, o site http://www.macoratti.net/alg_cpf.htm apresenta um passo-a-passo; verificar se o número da conta corrente já pertence a um cliente (se sim, informar outro número); para o caso de alteração, o usuário informa um CPF e caso ele exista no cadastro, permite alterar os dados do cliente (escolha quais dados podem ser alterados); para o caso de exclusão, o usuário informa um CPF e caso ele exista no cadastro, o aplicativo pede a confirmação e exclui o cliente do cadastro; para o caso de listagem de clientes, lista de forma organizada, os dados de todos os clientes cadastrados;
# - Gerenciar conta corrente
#
# GERENCIAR CONTA CORRENTE
# - Inserir crédito (1) ou débito (2)
# - Atualizar o saldo, conforme a operação realizada
# - Em caso de débito, o sistema deve consultar o saldo para avaliar disponibilidade.
# - O valor negativo da conta não pode ser superior ao limite.
#
# DICAS
# - Faça um menu dentro de um laço para permitir que o gerente das contas acesse as opções. Por exemplo: Insere cliente; Altera dados de um cliente; Exclui cliente; Lista clientes; Movimento da conta; Sair; Digite a opção:
#
# IDEIAS ADICIONAIS
# - adicionar data e hora de inserção do cliente
# - gerar numero da conta automaticamente
# - inserir nome do utilizador que realizado cada operação (do gerente)
#
#
# -----------------------------------------------
#
# lista=[append classe com todos os itens solicitados do cadastro]
# criar as funções necessárias
# pode ser usado o import, para não inserir as funções diretamente no programa principal
# no programa principal, fazer um while true (laço eterno) e insere as oções necessárias solicitadas (incluir cliente, apagar cliente, movimentar conta); se 'inclui', chama a função que inclui o cliente; se 'movimentar', chama a função para movimentar o cliente;
#
# lista=[]
# class t:
#   nome=input(...
#   cpf=int(input....
#   [...]
# mt=t()
# mt.a=input...
# mt.b=input...
# lista.append(mt)
#
# mt[0].a - para ler o valor 'a' do 'primeiro lote'
#
# valor=input('Informe o valor a ser procurado: ')
# def buscata (v, valor) - esta busca se no atributo 'a' possui o valor referido, sendo v o nome da lista no qual deve procurar o valor e 'valor' a variavel que contem o valor a ser vuscado;
#    for i in range (len(v):
#        if v[i].a==valor:
#           return i
#     return -1
#
# l(buscata(l,30).b - busca o valor de 'b' na posição em q 'a' vale 30
#
# l.pop(2) - exclui o elemento localizado na posição 2 da lista;

# -----------------------------------------------

lista_principal_clientes=[]

class tipo_cadastro:
    nome=""
    sobrenome=""
    cpf=0
    email=""
    endereco=""
    telefone=0
    nconta=0
    limite=0.0
    saldo=0.0

def menu_princial():
    opcao=1
    while opcao != 0:
        opcao=input("Informe a operação desejada: ")
        if opcao == 1:
    print("Em desenvolvimento")


def inserir_cliente():
    novo_cliente=tipo_cadastro()
    novo_cliente.nome=input("Nome: ")
    novo_cliente.sobrenome=input("Sobrenome: ")
    novo_cliente.cpf=int(input("CPF: "))
    novo_cliente.email=input("E-mail: ")
    novo_cliente.endereco=input("Endereço: ")
    novo_cliente.telefone=int(input("Telefone: "))
    novo_cliente.nconta=int(input("Número da Conta: "))
    novo_cliente.limite=1000.00
    novo_cliente.saldo=0.00
    lista_principal_clientes.append(novo_cliente)

def listar_cliente ():
    for i in range(len(lista_principal_clientes)):
        print("\nNome:",lista_principal_clientes[i].nome,"\nSobrenome:",lista_principal_clientes[i].sobrenome,"\nCPF:",lista_principal_clientes[i].cpf,"\nE-mail:",lista_principal_clientes[i].email,"\nEndereço:",lista_principal_clientes[i].endereco,"\nTelefone:",lista_principal_clientes[i].telefone,"\nConta Corrente:",lista_principal_clientes[i].nconta,"\nLimite autorizado: R$ {0:.2f}".format(lista_principal_clientes[i].limite),"\nSaldo: R$ {0:.2f}".format(lista_principal_clientes[i].saldo))

def buscar_cliente ():
    cpf_busca=int(input("Consultar CPF: "))
    for i in range(len(lista_principal_clientes)):
        buscando_cpf=lista_principal_clientes[i].cpf
        if cpf_busca == buscando_cpf:
            print("Este CPF já está cadastrado.\nNome do/a cliente: ",lista_principal_clientes[i].nome,lista_principal_clientes[i].sobrenome)



# PRINCIPAL
gerente=input("\nBem-vindo/a ao Sistema Central de Gerenciamento de Operações vBank.\nPara iniciar o SCGO vBabk, informe seu nome: ")
print ("\n\nUtilizador/a registrado/a:",gerente,"\nSistema Central de Gerenciamento de Operações\n©SCGO 2019 | vBank®")
menu_princial()
