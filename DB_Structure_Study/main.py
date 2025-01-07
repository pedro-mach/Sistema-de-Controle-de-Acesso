import peewee
from create_db import Usuario

if __name__ == '__main__':
    db = peewee.SqliteDatabase('Acess_Control.db') 

    def add_user():
        try:
            with db.atomic():
                input_username = input("Nome de Usuário: ")
                input_cargo = input("Qual o Cargo: ")
                input_senha = input("Qual a senha: ")
                liberation = input("Liberação (True/False): ") 
                liberation = liberation.lower() == 'true'  # Convert input to boolean

                Usuario.create(
                    username=input_username, 
                    cargo=input_cargo, 
                    senha=input_senha, 
                    permissao=liberation
                )
                print("Usuário adicionado com sucesso!")

        except Exception as e:
            print(f"Erro ao adicionar usuário: {e}")

    add_user()