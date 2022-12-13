import sqlite3 as lite

class TransactionObject():
    database = "dados.db"
    con = None
    cur = None
    connected = False

    def connect(self):
        TransactionObject.con = lite.connect(TransactionObject.database)
        TransactionObject.cur = TransactionObject.con.cursor()
        TransactionObject.connected = True

    def disconnect(self):
          TransactionObject.con.close()
          TransactionObject.connected = False

    def execute(self, lite, parms = None):
        if TransactionObject.connected:
            if parms == None:
                TransactionObject.cur.execute(lite)
            else:
                TransactionObject.cur.execute(lite, parms)
            return True
        else:
            return False

    def fetchall(self):
        return TransactionObject.cur.fetchall()

    def persist(self):
        if TransactionObject.connected:
            TransactionObject.con.commit()
            return True
        else:
            return False

def initDB():
    trans = TransactionObject()
    trans.connect()
    trans.execute("CREATE TABLE IF NOT EXISTS aluno (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, cpf TEXT, idade TEXT, sexo TEXT, data_nasc TEXT, endereco TEXT)")
    trans.persist()
    trans.disconnect()


# ADICIONA OS DADOS DO DB
def insert(nome, cpf, idade, sexo, data_nasc, endereco):
    trans = TransactionObject()
    trans.connect()
    trans.execute("INSERT INTO aluno VALUES(NULL, ?,?,?,?,?,?)", (nome, cpf, idade, sexo, data_nasc, endereco))
    trans.persist()
    trans.disconnect()

# VISUALIZA OS DADOS DO DB
def view():
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM aluno")
    rows = trans.fetchall()
    trans.disconnect()
    return rows

# EXCLUI UM DADO DO DB
def delete(i):
    trans = TransactionObject()
    trans.connect()
    trans.execute("DELETE FROM aluno WHERE id = ?", i)
    trans.persist()
    trans.disconnect()

initDB()
