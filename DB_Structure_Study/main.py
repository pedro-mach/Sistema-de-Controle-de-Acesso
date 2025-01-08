import peewee
import bcrypt
from create_db import *

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
            cargo = input("Qual o Cargo: ")
            senha = input("Qual a senha: ")
            liberation = input("Liberação (True/False): ")
            liberation = liberation.lower()

            # Validação básica
            if not all([username, cargo, senha]):
                print("Todos os campos são obrigatórios.")
                return

            senha_hash = criar_hash(senha)
            
            Usuario.create(
                username=username,
                cargo=cargo,
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
            # while sessao_ativa:
            #     # Lógica da aplicação
        else:
            print("Senha incorreta.")
    except Usuario.DoesNotExist:
        print("Usuário não encontrado.")

def acess_port():
    


if __name__ == '__main__':
    db.create_tables([Usuario])

    while True:
        opcao = input("Digite 'a' para adicionar usuário ou 'l' para fazer login: ")
        if opcao == 'a':
            adicionar_usuario()
        elif opcao == 'l':
            fazer_login()
        else:
            print("Opção inválida.")