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
# -
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
    nome=input("Nome: ")
    sobrenome=input("Sobrenome: ")
    cpf=int(input("CPF: "))
    email=input("E-mail: ")
    endereco=input("Endereço: ")
    telefone=int(input("Telefone: "))
    nconta=int(input("Número da Conta: "))

def inserir_cliente():
    novo_cliente=tipo_cadastro()
    novo_cliente.a=input("Nome: ")
    novo_cliente.b=input("Sobrenome: ")
    novo_cliente.c=int(input("CPF: "))
    novo_cliente.d=input("E-mail: ")
    novo_cliente.e=input("Endereço: ")
    novo_cliente.f=int(input("Telefone: "))
    novo_cliente.g=int(input("Número da Conta: "))
    lista_principal_cliente.append(novo_cliente)

def busca_cliente ():
    print("Em desenvolvimento.")

def listar_cliente ():
    print(lista_principal_clientes)

print("This is vBank.")
inserir_cliente()

print("\n\n\nSua lista de clientes:")
listar_cliente()
