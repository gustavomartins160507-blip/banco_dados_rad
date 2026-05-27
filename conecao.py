import sqlite3 as conector
try:
    conexao = conector.connect('meu_banco.db')
    cursor = conexao.cursor()
    comando = ''' ALTER TABLE Pessoa 
    ADD COLUMN pessoa_fisica;
    '''
    cursor.execute(comando)
    conexao.commit()
except conector.DatabaseError as err:
    print(f"Erro ao conectar no banco de dados {err}")
finally:
    if conexao:
        cursor.close()
        conexao.close()