import os
import ZODB, ZODB.FileStorage

# Certifique-se de que a pasta 'db' existe
os.makedirs('db', exist_ok=True)

# Defina o caminho do banco de dados dentro da pasta 'db'
storage = ZODB.FileStorage.FileStorage('db/mydatabase.fs')

# Inicialize o banco de dados
db = ZODB.DB(storage)
connection = db.open()
root = connection.root

# Exemplo: armazenar algo no banco
root['example'] = 'Hello, ZODB!'
import transaction
transaction.commit()

print("Banco de dados criado na pasta 'db'!")
