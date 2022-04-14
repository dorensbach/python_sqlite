# create_data_sql.py

import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# Inserindo dados na tabela
cursor.execute("""
    INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
    VALUES ('Regis', 35, '00000000000', 'regis@email.com', '11-98765-4321', 'São Paulo', 'SP', '2022-04-13');
    """)

cursor.execute("""
    INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
    VALUES ('Aloisio', 87, '11111111111', 'aloisio@email.com', '51-98765-4322', 'Porto Alegre', 'RS', '2022-04-13');
    """)

cursor.execute("""
    INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
    VALUES ('Paulo', 39, '22222222222', 'paulo@email.com', '21-98765-4323', 'Rio de Janeiro', 'RJ', '2022-04-14');
    """)

cursor.execute("""
    INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
    VALUES ('Paula', 40, '33333333333', 'paula@email.com', '11-98765-4320', 'Campinas', 'SP', '2022-04-14');
    """)

# Gravando no BD
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()
