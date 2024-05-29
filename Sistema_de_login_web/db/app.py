import sqlite3

conexao = sqlite3.connect('meubanco.db')

cursor = conexao.cursor()

#criar a tabela PASSO 1
#cursor.execute("CREATE TABLE usuarios (email text, senha text, tel integer)")

#criar objeto PASSO 2
#cursor.execute("INSERT INTO usuarios VALUES('adimin@login.com','12345',31900000000)")

#comitar PASSO 3
#conexao.commit()

cursor.execute('SELECT * FROM usuarios')
print(cursor.fetchall())