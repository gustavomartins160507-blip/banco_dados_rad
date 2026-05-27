import sqlite3 as conector
import pandas as pd
import os
def conectar_banco(nome_banco):
    conexao = conector.connect(nome_banco)
    return conexao
def executar_comandos(conexao):
    cursor = conexao.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS locais(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        endereco TEXT NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS eventos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        data TEXT NOT NULL,
        id_local INTEGER,
        FOREIGN KEY(id_local) REFERENCES locais(id)
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS participantes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        id_evento INTEGER,
        FOREIGN KEY(id_evento) REFERENCES eventos(id)
    )
    ''')
    cursor.execute(''' INSERT INTO locais(nome, endereco) VALUES('Gustavo martins de sousa',
     'Rua 21 conjunto Polar')''')
    caminho_pastas = "dados"
    caminho_db = os.path.join(caminho_pastas,"eventos.db")
    print(caminho_db)
    sql = "SELECT nome, endereco FROM locais"
    df = pd.read_sql_query(sql, conexao)
    df.to_csv('minha planilha.csv', index=False)
    print(df)
    conexao.commit()
    cursor.close()
conexao = conectar_banco('eventos.db')
executar_comandos(conexao)
print("Tabelas criadas com sucesso!")
conexao.close()