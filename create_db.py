# create_db.py

import sqlite3

# Conecta no banco. Se não existe, cria o banco
conn = sqlite3.connect('clientes.db')
# Para criar na memoria, sem persistir
# conn = sqlite3.connect(':memory:')

# Definindo um cursor
cursor = conn.cursor()
# Cursor é um interador que permite navegar e manipular os registros do BD

# Criando a tabela (schema)
cursor.execute("""
    CREATE TABLE clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        cpf VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
        fone TEXT,
        cidade TEXT,
        uf VARCHAR(2) NOT NULL,
        criado_em DATE NOT NULL
    );
    """)

print('Tabela criada com sucesso.')

# Desconecta do banco
conn.close()
