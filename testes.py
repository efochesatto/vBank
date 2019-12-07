
variavel=[]
class dados:
    primeiro=0
    segundo=0

def insere_item():
    item=dados()
    item.primeiro=input("Primeiro: ")
    item.segundo=input("Segundo: ")
    variavel.append(item)

insere_item()
numero=0
print(variavel[numero].primeiro)
