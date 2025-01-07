import peewee
from create_db import Usuario

if __name__ == '__main__':
    db = peewee.SqliteDatabase('Acess_Control.db')

    Usuario.create(username='admin', cargo='Administrador', senha='1244466666', permissao=True)
    