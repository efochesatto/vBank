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
# - quando o usuário confirmar saída, o programa não encerra, mas solicita login de um novo usuário;
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

def cadastrar_cliente():
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

def consultar_cadastro ():
    cpf_busca=int(input("Consultar CPF: "))
    for i in range(len(lista_principal_clientes)):
        buscando_cpf=lista_principal_clientes[i].cpf
        if cpf_busca == buscando_cpf:
            print("Este CPF já está cadastrado.\nNome do/a cliente: ",lista_principal_clientes[i].nome,lista_principal_clientes[i].sobrenome)

def alterar_cadastro ():
    print("Em desenvolvimento")

def excluir_cadastro ():
    print("Em desenvolvimento")

# Validar a saída do menu secundario Clientes e retorno ao menu principal do programa
def valida_saida_clientes():
    testando_saida="s"
    while testando_saida == "s":
        testando_saida=input("Deseja realmente retonar ao menu principal (s/n)? ")
        testando_saida.lower
        if testando_saida == "s":
            return "s"
        if testando_saida == "n":
            return "n"
        if testando_saida != "s" and testando_saida != "n":
            print("Esta não é uma opção válida.")
            testando_saida="s"

# Chama as funções secundárias da opção principal Clientes
def menu_secundario_clientes():
    opcao="1"
    print("1 = Consultar cadastro\n2 = Cadastrar cliente\n3 = Alterar cadastro\n4 = Excluir cadastro\n0 = Voltar para o menu principal\n")
    while opcao != "0":
        opcao=input("Informe a opção desejada: ")
        if opcao == "1":
            consultar_cadastro()
        if opcao == "2":
            cadastrar_cliente()
        if opcao == "3":
            alterar_cadastro()
        if opcao == "4":
            excluir_cadastro()
        if opcao == "0":
            retornar=valida_saida_clientes()
            if retornar == "s":
                return "s"
            if retornar == "n":
                opcao="1"
        if opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "0":
            print("Esta não é uma opção válida.")

def debitar():
    print("Em desenvolvimento")

def creditar():
    print("Em desenvolvimento")

# Validar a saída do menu secundario Conta Corrente e retorno ao menu principal do program
def valida_saida_conta():
    testando_saida="s"
    while testando_saida == "s":
        testando_saida=input("Deseja realmente retonar ao menu principal (s/n)? ")
        testando_saida.lower
        if testando_saida == "s":
            return "s"
        if testando_saida == "n":
            return "n"
        if testando_saida != "s" and testando_saida != "n":
            print("Esta não é uma opção válida.")
            testando_saida="s"

# Chama as funções secundárias da opção principal Conta Correte
def menu_secundario_conta():
    opcao="1"
    print("1 = Débito\n2 = Crédito\n0 = Voltar para o menu principal\n")
    while opcao != "0":
        opcao=input("Informe a opção desejada: ")
        if opcao == "1":
            debitar()
        if opcao == "2":
            creditar()
        if opcao == "0":
            retornar=valida_saida_conta()
            if retornar == "s":
                return "s"
            if retornar == "n":
                opcao="1"
        if opcao != "1" and opcao != "2" and opcao != "0":
            print("Esta não é uma opção válida.")

# Confirmação da ooção principal de sair do programa
def valida_saida_principal():
    testando_saida="s"
    while testando_saida == "s":
        testando_saida=input("Deseja realmente sair do SCGO vBank (s/n)? ")
        testando_saida.lower
        if testando_saida == "s":
            return "s"
        if testando_saida == "n":
            return "n"
        if testando_saida != "s" and testando_saida != "n":
            print("Esta não é uma opção válida.")
            testando_saida="s"

# Chama as funções principais do programa
def menu_principal():
    logado=1
    while logado == 1:
        gerente=input("\n\nBem-vindo/a ao Sistema Central de Gerenciamento de Operações vBank.\nPara iniciar o SCGO vBabk, informe seu IDvBank: ")
        print ("\n\n---------------------------------------------\nUtilizador/a registrado/a:",gerente,"\nPerfil do/a utilizador/a: Gerente de Contas\nSistema Central de Gerenciamento de Operações\n©SCGO 2019 | Versão 1.0 | vBank®\n---------------------------------------------\n")
        opcao="1"
        while opcao != "0":
            print("\nSCGO vBank Gerente de Contas\n1 = Gerenciar clientes\n2 = Gerenciar conta corrente\n0 = Sair do SCGO vBank")
            opcao=input("\nInforme a operação desejada: ")
            if opcao == "1":
                print("\nSCGO vBank Gerente de Contas- Gerenciar Clientes")
                retorno=menu_secundario_clientes()
                if retorno == "s":
                    opcao="1"
            if opcao == "2":
                print("\nSCGO vBank Gerente de Contas- Gerenciar Conta Corrente")
                retorno=menu_secundario_conta()
                if retorno == "s":
                    opcao="1"
            if opcao == "0":
                desiste=valida_saida_principal()
                if desiste == "s":
                    print("\nLogout efetuado com sucesso.\nSistema Central de Gerenciamento de Operações\n©SCGO 2019 | vBank®")
                    opcao="0"
            if opcao != "1" and opcao != "2" and opcao != "0":
                print("Esta não é uma opção válida.")



# PROGRAMA PRINCIPAL
menu_principal()
