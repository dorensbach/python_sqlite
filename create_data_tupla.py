# create_data_tupla.py

import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# Criando uma lista de dados
lista = [
    ('Fabio', 23, '44444444444', 'fabio@email.com', '1234-5678', 'Belo Horizonte', 'MG', '2022-04-17'),
    ('Joao', 21, '55555555555', 'joao@email.com', '11-1234-5600', 'São Paulo', 'SP', '2022-04-18'),
    ('Carlos', 24, '66666666666', 'carlos@email.com', '12-1234-5601', 'Campinas', 'SP', '2022-04-18')
]

# Inserindo dados na tabela
cursor.executemany("""
    INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
    VALUES (?,?,?,?,?,?,?,?)
    """, lista)

# Gravando no BD
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()
