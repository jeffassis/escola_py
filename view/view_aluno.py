import sqlite3 as lite

# criando conexao
con = lite.connect('dados.db')

# Adicionar informações


def add_aluno_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO aluno (nome, cpf, idade, sexo, data_nasc, endereco) VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)

# Acessar informações


def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM aluno"
        cur.execute(query)
        informacao = cur.fetchall()

        for i in informacao:
            lista.append(i)
    return lista

# Deletar informações


def deletar_aluno_info(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM aluno WHERE id=?"
        cur.execute(query, i)
