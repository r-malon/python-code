'''
Use it to save game?
'''
from sqlite3 import *
con=connect("C:\\Users\\RAFAEL\\Music\\Trabalho MATaplicada\\bancodedados.db")
cursor=con.cursor()
cursor.execute('''
CREATE TABLE tabelateste(
    coluna1 TEXT NOT NULL,
    coluna2 INT NOT NULL,
    coluna3 REAL
);
''')
con.close()
