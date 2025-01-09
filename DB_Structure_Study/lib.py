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



def acess_port(usuario):
    if usuario.permissao == 1:
        print("Acesso de Segurança liberado.")
        print("Autorizado a passar !!")
    else:
        print("Caso seja um erro, entre em contato com o Administrador.")