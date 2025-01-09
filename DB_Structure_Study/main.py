import peewee
import bcrypt
from create_db import *
from lib import *

db = peewee.SqliteDatabase('Acess_Control.db')

class Usuario(peewee.Model):
    username = peewee.CharField(unique=True)
    cargo = peewee.CharField()
    senha = peewee.CharField()
    permissao = peewee.BooleanField(default=False)

    class Meta:
        database = db

def criar_hash(senha):
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

def verificar_senha(senha_digitada, senha_hash):
    return bcrypt.checkpw(senha_digitada.encode('utf-8'), senha_hash.encode('utf-8'))

def adicionar_usuario():
    try:
        with db.atomic():
            username = input("Nome de Usuário: ")
            cargo_usuario = cargo()
            senha = input("Qual a senha: ")
            liberation = input("Liberação (True/False): ")
            liberation = liberation.lower()

            # Validação básica
            if not all([username, senha]):
                print("Todos os campos são obrigatórios.")
                return

            senha_hash = criar_hash(senha)
            
            Usuario.create(
                username=username,
                cargo=cargo_usuario,
                senha=senha_hash,
                permissao=liberation
            )
            print("Usuário adicionado com sucesso!")
    except Exception as e:
        print(f"Erro ao adicionar usuário: {e}")

def fazer_login():
    sessao_ativa = {}

    username = input("Nome de Usuário: ")
    senha = input("Qual a senha: ")

    try:
        usuario = Usuario.get(Usuario.username == username)
        if verificar_senha(senha, usuario.senha):
            sessao_ativa['usuario_id'] = usuario.id
            print("Login bem-sucedido!")
            while True:
                if usuario.cargo == 'Administração':
                    opcao = menu_admin()
                    if opcao == 1:
                        adicionar_usuario()
                    elif opcao == 2:
                        edit_user_from_db()
#                    elif opcao == 3:
#                        delete_user_from_db()    
                    elif opcao == 4:
                        acess_port(usuario)
                    elif opcao == 5:
                        break
                else:
                    acess_port(usuario)
                    break

        else:
            print("Senha incorreta.")
    except Usuario.DoesNotExist:
        print("Usuário não encontrado.")

# def var_admin(usuario):
#   if usuario.cargo == admin


if __name__ == '__main__':
    db.create_tables([Usuario])
    tittle_('TRABALHO APS 1.0')
    while True:
        opcao = menu(['Fazer Login', 'Sair'])
        if opcao == 1:
            fazer_login()
        elif opcao == 2:
            print("Saindo ...")
            break
        else:
            print("Opção inválida.")