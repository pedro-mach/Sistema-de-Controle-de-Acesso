import peewee

db = peewee.SqliteDatabase('Acess_Control.db')

class Usuario(peewee.Model):
    username = peewee.CharField()
    cargo = peewee.CharField()
    senha = peewee.CharField()
    permissao = peewee.BooleanField()

    class Meta:
        database = db

# Criar a tabela (execute apenas uma vez)
db.create_tables([Usuario])