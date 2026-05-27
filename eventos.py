import sqlite3 as conector  # importa a biblioteca sqlite3 com o apelido "conector"
import pandas as pd  # importa o pandas para manipulação de dados
import os  # importa o os para manipulação de arquivos e pastas

# função que cria e retorna a conexão com o banco de dados
def conectar_banco(nome_banco):
    conexao = conector.connect(nome_banco)  # conecta ao banco (cria o arquivo .db se não existir)
    return conexao  # retorna a conexão para ser usada nas outras funções

# função principal que cria as tabelas, insere dados e exporta para CSV
def executar_comandos(conexao):
    cursor = conexao.cursor()  # cria o cursor, responsável por executar os comandos SQL

    # cria a tabela "locais" se ela ainda não existir
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS locais(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        endereco TEXT NOT NULL
    )
    ''')

    # cria a tabela "eventos" com chave estrangeira ligada à tabela locais
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS eventos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        data TEXT NOT NULL,
        id_local INTEGER,
        FOREIGN KEY(id_local) REFERENCES locais(id)  -- relaciona evento com seu local
    )
    ''')

    # cria a tabela "participantes" com chave estrangeira ligada à tabela eventos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS participantes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        id_evento INTEGER,
        FOREIGN KEY(id_evento) REFERENCES eventos(id)  -- relaciona participante com seu evento
    )
    ''')

    # insere um registro na tabela locais
    cursor.execute(''' INSERT INTO locais(nome, endereco) VALUES('Gustavo martins de sousa',
     'Rua 21 conjunto Polar')''')

    # monta o caminho do arquivo do banco dentro da pasta "dados"
    caminho_pastas = "dados"
    caminho_db = os.path.join(caminho_pastas, "eventos.db")
    print(caminho_db)  # exibe o caminho no terminal

    # busca nome e endereço de todos os registros da tabela locais
    sql = "SELECT nome, endereco FROM locais"
    df = pd.read_sql_query(sql, conexao)  # executa o SELECT e armazena o resultado num DataFrame

    df.to_csv('minha planilha.csv', index=False)  # exporta os dados para CSV sem o índice

    print(df)  # exibe os dados no terminal

    conexao.commit()  # salva todas as alterações feitas no banco
    cursor.close()  # encerra o cursor após o uso

# conecta ao banco de dados eventos.db
conexao = conectar_banco('eventos.db')

executar_comandos(conexao)  # executa a criação das tabelas, inserção e exportação

print("Tabelas criadas com sucesso!")  # confirma a execução no terminal

conexao.close()  # encerra a conexão com o banco de dados