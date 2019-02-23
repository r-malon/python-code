import sqlite3 as sql
conn=sql.connect('Music/clientes.db')
cursor=conn.cursor()

cursor.execute('''
CREATE TABLE clientes (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	idade INT,
	local VARCHAR(2),
	data DATE
);
''')

#cursor.execute(''')

cursor.execute('''
	INSERT INTO clientes VALUES (1, 'jailson', 45, 'SP', '2017-04-15');
''')

cursor.execute('''
	SELECT * FROM clientes;
''')

conn.commit()
conn.close()