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
# - informar data e hora de login e logout de um utilizador
# -----------------------------------------------
#
# PROBLEMAS
# - na busca de cadastro, se não encontra, dá erro; tem que retornar que não encontrou
#
#
#
#
#
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
    telefone=""
    nconta=0
    limite=0.0
    saldo=0.0

#
# ------------------------------------------------------------------------------------------------------------------------------------
# FUNÇÕES DE CLIENTE
# ------------------------------------------------------------------------------------------------------------------------------------
#


def cadastrar_cliente_ver_cadastro():
    i=(len(lista_principal_clientes))-1
    print("\nNome:",lista_principal_clientes[i].nome,"\nSobrenome:",lista_principal_clientes[i].sobrenome,"\nCPF:",lista_principal_clientes[i].cpf,"\nE-mail:",lista_principal_clientes[i].email,"\nEndereço:",lista_principal_clientes[i].endereco,"\nTelefone:",lista_principal_clientes[i].telefone,"\nvConta:",lista_principal_clientes[i].vconta,"\nLimite autorizado: R$ {0:.2f}".format(lista_principal_clientes[i].limite),"\nSaldo: R$ {0:.2f}".format(lista_principal_clientes[i].saldo,"\n"))
    return "1"

def cadastrar_cliente_alterar_cadastro():
    print("Este módulo ainda não foi desenvolvido.\nPara alterar o cadastro, retorne ao menu anterior e selecione 'Alterar Cadastro'")
    return "1"

def cadastrar_cliente_finalizar():
    opcao="1"
    while opcao != "0":
        print("\n------------\nSCGO vBank Gerente de Contas- Gerenciar Clientes - Cadastrar Cliente - Finalizar Cadastro\n1 = Ver cadastro\n2 = Alterar Cadastro\n3 = Finalizar e retornar ao menu anterior\n")
        opcao=input("Informe a opção desejada: ")
        if opcao == "1":
            opcao=cadastrar_cliente_ver_cadastro()
        if opcao == "2":
            opcao=cadastrar_cliente_alterar_cadastro()
        if opcao == "3":
            return 0
        if opcao != "1" and opcao != "2" and opcao != "3":
            print("Esta não é uma opção válida.")
            opcao="1"

def cadastrar_cliente():
    print("\n------------\nSCGO vBank Gerente de Contas- Gerenciar Clientes - Cadastrar Cliente\nCadastro vBank")
    novo_cliente=tipo_cadastro()
    novo_cliente.nome=input("Nome: ")
    novo_cliente.sobrenome=input("Sobrenome: ")
    novo_cliente.cpf=int(input("CPF: "))
    novo_cliente.email=input("E-mail: ")
    novo_cliente.endereco=input("Endereço: ")
    novo_cliente.telefone=input("Telefone: ")
    novo_cliente.vconta=int(input("vConta: "))
    novo_cliente.limite=1000.00
    novo_cliente.saldo=0.00
    lista_principal_clientes.append(novo_cliente)
    print("\nCadastro realizado com sucesso")
    cadastrar_cliente_finalizar()
    return "1"

            # FALTA VERIFICAR SE O CPF JÁ EXISTE


def consultar_cadastro_ver_completo(i):
    opcao="1"
    while opcao != "0":
        opcao=input("\nDeseja visualizar o cadastro completo (s/n)?")
        if opcao == "s":
            print("\nNome:",lista_principal_clientes[i].nome,"\nSobrenome:",lista_principal_clientes[i].sobrenome,"\nCPF:",lista_principal_clientes[i].cpf,"\nE-mail:",lista_principal_clientes[i].email,"\nEndereço:",lista_principal_clientes[i].endereco,"\nTelefone:",lista_principal_clientes[i].telefone,"\nvConta:",lista_principal_clientes[i].vconta,"\nLimite autorizado: R$ {0:.2f}".format(lista_principal_clientes[i].limite),"\nSaldo: R$ {0:.2f}".format(lista_principal_clientes[i].saldo))
            return "1"
        if opcao == "n":
            return "1"
        if opcao != "s" and opcao != "n":
            print("Esta não é uma opção válida.")
            opcao="1"

def consultar_cadastro_cpf():
        busca=int(input("Consultar CPF: "))
        cadastro_encontrado=0
        for i in range(len(lista_principal_clientes)):
            buscando=lista_principal_clientes[i].cpf
            if busca==buscando:
                cadastro=i
                cadastro_encontrado=1
        if cadastro_encontrado == 1:
            print("Este CPF já está cadastrado.\nNome do/a cliente: ",lista_principal_clientes[i].nome,lista_principal_clientes[i].sobrenome,"\n")
            return consultar_cadastro_ver_completo(i)
        if cadastro_encontrado == 0:
            print("Não foi encontrado nenhum cadastro com o CPF informado.")
            return "1"

def consultar_cadastro_nome():
        busca=input("Consultar Nome: ")
        cadastro_encontrado=0
        for i in range(len(lista_principal_clientes)):
            buscando=lista_principal_clientes[i].nome
            if busca==buscando:
                cadastro=i
                cadastro_encontrado=1
        if cadastro_encontrado == 1:
            print("Este Nome já está cadastrado.\nNome do/a cliente: ",lista_principal_clientes[i].nome,lista_principal_clientes[i].sobrenome,"\n")
            return consultar_cadastro_ver_completo(i)
        if cadastro_encontrado == 0:
            print("Não foi encontrado nenhum cadastro com o CPF informado.")
            return "1"

def consultar_cadastro_sobrenome():
        busca=input("Consultar Sobrenome: ")
        cadastro_encontrado=0
        for i in range(len(lista_principal_clientes)):
            buscando=lista_principal_clientes[i].sobrenome
            if busca==buscando:
                cadastro=i
                cadastro_encontrado=1
        if cadastro_encontrado == 1:
            print("Este Sobrenome já está cadastrado.\nNome do/a cliente: ",lista_principal_clientes[i].nome,lista_principal_clientes[i].sobrenome,"\n")
            return consultar_cadastro_ver_completo(i)
        if cadastro_encontrado == 0:
            print("Não foi encontrado nenhum cadastro com o CPF informado.")
            return "1"

def consultar_cadastro_vconta():
        busca=int(input("Consultar vConta: "))
        cadastro_encontrado=0
        for i in range(len(lista_principal_clientes)):
            buscando=lista_principal_clientes[i].vconta
            if busca==buscando:
                cadastro=i
                cadastro_encontrado=1
        if cadastro_encontrado == 1:
            print("Esta vConta já está cadastrado.\nNome do/a cliente: ",lista_principal_clientes[i].nome,lista_principal_clientes[i].sobrenome,"\n")
            return consultar_cadastro_ver_completo(i)
        if cadastro_encontrado == 0:
            print("Não foi encontrado nenhum cadastro com o CPF informado.")
            return "1"

def consultar_cadastro ():
    opcao="1"
    while opcao != "0":
        print("\n------------\nSCGO vBank Gerente de Contas- Gerenciar Clientes - Consultar Cadastro\nConsultar por:\n1 = CPF\n2 = Nome \n3 = Sobrenome\n4 = vConta\n0 = Retornar ao menu anterior\n")
        opcao=input("Informe a opção desejada: ")
        if opcao == "1":
            opcao=consultar_cadastro_cpf()
        if opcao == "2":
            opcao=consultar_cadastro_nome()
        if opcao == "3":
            opcao=consultar_cadastro_sobrenome()
        if opcao == "4":
            opcao=consultar_cadastro_vconta()
        if opcao == "0":
            return "1"
        if opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "0":
            print("Esta não é uma opção válida.")

def alterar_cadastro_confirmar_conta_buscada ():
    opcao=input("Deseja alterar esta conta (s/n)? ")
    if opcao == "s":
        return 1
    if opcao == "n":
        return 0
    if opcao != "s" and opcao != "n":
        print("Esta não é uma opção válida.")
        alterar_cadastro_confirmar_conta_buscada()


def alterar_cadastro_encontrado (cadastro):
    print("Titularidade da conta a ser alterada:",lista_principal_clientes[cadastro].nome,lista_principal_clientes[cadastro].sobrenome)
    confirma=alterar_cadastro_confirmar_conta_buscada()
    if confirma == 1:
        altera=input("Você pode realizar alterações cadastrais nos seguintes campos:\n1 = Nome\n2 = Sobrenome\n3 = Email\n4 = Endereço\n5 = Telefone\n0 = Cancelar atualização cadastral e retornar\nInforme a informação que deseja alterar: ")
        if altera == "1":
            novo=input("Infome o novo Nome: ")
            lista_principal_clientes[cadastro].nome=novo
            return cadastro
        if altera == "2":
            novo=input("Infome o novo Sobrenome: ")
            lista_principal_clientes[cadastro].sobrenome=novo
            return cadastro
        if altera == "3":
            novo=input("Infome o novo E-mail: ")
            lista_principal_clientes[cadastro].email=novo
            return cadastro
        if altera == "4":
            novo=input("Infome o novo Endereço: ")
            lista_principal_clientes[cadastro].endereco=novo
            return cadastro
        if altera == "5":
            novo=input("Infome o novo Telefone: ")
            lista_principal_clientes[cadastro].telefone=novo
            return cadastro
        if altera == "0":
            return -1

def alterar_cadastro ():
    print("\n------------\nSCGO vBank Gerente de Contas- Gerenciar Clientes - Alterar Cadastro\nEsta opção permite realizar atualização cadastral. \nPara alterar um cadastro, é necessário o informar o CPF registrado.")
    busca=int(input("Informe o CPF do cadastro que deseja alterar: "))
    cadastro_encontrado=0
    for i in range(len(lista_principal_clientes)):
        buscando=lista_principal_clientes[i].cpf
        if busca==buscando:
            cadastro=i
            cadastro_encontrado=1
    if cadastro_encontrado == 1:
        alterar_cadastro_encontrado(cadastro)
    else:
        opcao="1"
        while opcao!="0":
            opcao=input("O CPF informado não é um cliente vBank.\nDeseja realizar uma nova busca (s/n)?" )
            if opcao == "s":
                alterar_cadastro()
            if opcao == "n":
                return "1"
            if opcao != "s" and opcao != "n":
                print("Esta não é uma opção válida.")
                opcao="1"

def excluir_cadastro_confirmar_conta_buscada ():
    opcao=input("Deseja realmente excluir esta conta (s/n)? ")
    if opcao == "s":
        return 1
    if opcao == "n":
        return 0
    if opcao != "s" and opcao != "n":
        print("Esta não é uma opção válida.")
        excluir_cadastro_confirmar_conta_buscada()

def excluir_cadastro_encontrado(cadastro):
    print("Titularidade da conta a ser alterada:",lista_principal_clientes[cadastro].nome,lista_principal_clientes[cadastro].sobrenome)
    confirma=excluir_cadastro_confirmar_conta_buscada()
    if confirma == 1:
        lista_principal_clientes.pop(cadastro)
        print("Cadastro excluído com sucesso.")
        return "1"

def excluir_cadastro ():
    print("\n------------\nSCGO vBank Gerente de Contas- Gerenciar Clientes - Excluir Cadastro\nEsta opção remove permanentemente um cadastro de cliente. \nPara excluir um cadastro, é necessário o informar o CPF registrado.")
    busca=int(input("Informe o CPF do cadastro que deseja excluir: "))
    cadastro_encontrado=0
    for i in range(len(lista_principal_clientes)):
        buscando=lista_principal_clientes[i].cpf
        if busca==buscando:
            cadastro=i
            cadastro_encontrado=1
    if cadastro_encontrado == 1:
        excluir_cadastro_encontrado(cadastro)
        return "1"
    if cadastro_encontrado == 0:
        opcao="1"
        while opcao!="0":
            opcao=input("O CPF informado não é um cliente vBank.\nDeseja realizar uma nova busca (s/n)?" )
            if opcao == "s":
                excluir_cadastro()
                return "1"
            if opcao == "n":
                return "1"
            if opcao != "s" and opcao != "n":
                print("Esta não é uma opção válida.")
                opcao="1"




#
# ------------------------------------------------------------------------------------------------------------------------------------
# FUNÇÕES DE CONTA
# ------------------------------------------------------------------------------------------------------------------------------------
#


def debitar():
    print("Em desenvolvimento")

def creditar():
    print("Em desenvolvimento")


#
# ------------------------------------------------------------------------------------------------------------------------------------
# FUNÇÕES DE NAVEGAÇÃO
# ------------------------------------------------------------------------------------------------------------------------------------
#


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
    while opcao != "0":
        print("\n------------\nSCGO vBank Gerente de Contas- Gerenciar Clientes\n1 = Consultar cadastro\n2 = Cadastrar cliente\n3 = Alterar cadastro\n4 = Excluir cadastro\n0 = Voltar para o menu principal\n")
        opcao=input("Informe a opção desejada: ")
        if opcao == "1":
            opcao=consultar_cadastro()
        if opcao == "2":
            opcao=cadastrar_cliente()
        if opcao == "3":
            opcao=alterar_cadastro()
            if opcao == "1":
                opcao="1"
            else:
                i=input("Deseja verificar o cadastro alterado (s/n)?")
                if i == "s":
                    print("\nNome:",lista_principal_clientes[opcao].nome,"\nSobrenome:",lista_principal_clientes[opcao].sobrenome,"\nCPF:",lista_principal_clientes[opcao].cpf,"\nE-mail:",lista_principal_clientes[opcao].email,"\nEndereço:",lista_principal_clientes[opcao].endereco,"\nTelefone:",lista_principal_clientes[opcao].telefone,"\nvConta:",lista_principal_clientes[opcao].vconta,"\nLimite autorizado: R$ {0:.2f}".format(lista_principal_clientes[opcao].limite),"\nSaldo: R$ {0:.2f}".format(lista_principal_clientes[opcao].saldo))
                    opcao="1"
                else:
                    opcao="1"
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
    while opcao != "0":
        print("\n------------\nSCGO vBank Gerente de Contas- Gerenciar Conta Corrente\n1 = Débito\n2 = Crédito\n0 = Voltar para o menu principal\n")
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
            return "1"
        if testando_saida != "s" and testando_saida != "n":
            print("Esta não é uma opção válida.")
            testando_saida="s"

# Chama as funções principais do programa
def menu_principal():
    logado=1
    while logado == 1:
        gerente=input("\n\nBem-vindo/a ao Sistema Central de Gerenciamento de Operações vBank.\nPara iniciar o SCGO vBabk, informe seu IDvBank: ")
        print ("\n\n---------------------------------------------\nLogin efetuado com sucesso.\nUtilizador/a registrado/a:",gerente,"\nPerfil do/a utilizador/a: Gerente de Contas\nSistema Central de Gerenciamento de Operações\n©SCGO 2019 | Versão 1.0 | vBank®\n---------------------------------------------\n")
        opcao="1"
        while opcao != "0":
            print("\n\n------------\nSCGO vBank Gerente de Contas\n1 = Gerenciar clientes\n2 = Gerenciar conta corrente\n0 = Sair do SCGO vBank")
            opcao=input("\nInforme a operação desejada: ")
            if opcao == "1":
                retorno=menu_secundario_clientes()
                if retorno == "s":
                    opcao="1"
            if opcao == "2":
                retorno=menu_secundario_conta()
                if retorno == "s":
                    opcao="1"
            if opcao == "0":
                desiste=valida_saida_principal()
                if desiste == "s":
                    print("\n\n---------------------------------------------\nLogout efetuado com sucesso.\nUtilizador/a registrado/a:",gerente,"\nPerfil do/a utilizador/a: Gerente de Contas\nSistema Central de Gerenciamento de Operações\n©SCGO 2019 | vBank®\n---------------------------------------------\n")
                if desiste == "1":
                    opcao="1"
            if opcao != "1" and opcao != "2" and opcao != "0":
                print("Esta não é uma opção válida.")


#
# ------------------------------------------------------------------------------------------------------------------------------------
# PROGRAMA PRINCIAL
# ------------------------------------------------------------------------------------------------------------------------------------
#

menu_principal()
