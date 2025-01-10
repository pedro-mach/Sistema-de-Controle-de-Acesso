import peewee
from create_db import *
from main import criar_hash

def linha(tam = 42):
    return '-' * tam

def tittle_(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
 
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n
    
def menu(lista):
    print(linha())
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1  
    print(linha())
    opc = leiaInt("Escolha:")
    return opc

def cargo():
    opcao = menu(['Administração', 'Funcionário'])
    return 'Administração' if opcao == 1 else 'Funcionário'

def menu_admin():
    opcao = menu(['Criar usuario', 'Modificar usuario', 'Apagar usuario', 'Abrir porta', 'Logoff'])
    return opcao

def edit_user_from_db():
    username = input("Nome de Usuário: ")
    usuario = Usuario.get(Usuario.username == username)
    print(f'Segue as informações do usuario: {usuario.username}')
    print(f'Username: {usuario.username} || Cargo: {usuario.cargo} || Liberação: {usuario.permissao} ')
    opc = menu(['Modificar usarname', 'Modificar Senha', 'Mudar Cargo', 'Mudar Liberação', 'Apagar Usuario'])
    if opc == 1:
        new_username = input("Nome de Usuário: ")
        usuario.username = new_username
        usuario.save()
        
    elif opc == 2:
        new_pssw = input("Nova senha: ")
        senha = criar_hash(new_pssw)
        usuario.senha = senha
        usuario.save()
        
    elif opc == 3:
        new_cargo = cargo()
        usuario.cargo = new_cargo
        usuario.save()  
        
    elif opc == 4: # corrigir
        new_liberacao = input("Liberação (True/False): ")
        liberation = new_liberacao.lower()
        usuario.permissao = liberation
        usuario.save()
    
    elif opc == 5:
        usuario.delete_instance()
        print("Usuário deletado com sucesso!")
        
    else:
       print('Opção Invalida')
    



def acess_port(usuario):
    if usuario.permissao == 1:
        print("Acesso de Segurança liberado.")
        print("Autorizado a passar !!")
    else:
        print("Caso seja um erro, entre em contato com o Administrador.")