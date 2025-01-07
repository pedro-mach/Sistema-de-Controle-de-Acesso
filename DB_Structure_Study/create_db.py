import peewee

db = peewee.SqliteDatabase('Acess_Control.db')

class BaseModel(peewee.Model):
    class Meta:
        database = db

class Usuario(BaseModel):
    username = peewee.CharField(unique=True)
    cargo = peewee.CharField()
    senha = peewee.CharField()
    permissao = peewee.BooleanField()

if __name__ == '__main__':
    db.create_tables([Usuario])