import sqlite3


conexao = sqlite3.connect('escola.db')
cursor = conexao.cursor()

#C - Criar tabela e adicionar os dados
cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    email TEXT NOT NULL);
    
                ''')
print ('tabela criada com sucesso\n')

# Adicionar alunos
#cursor.execute("INSERT INTO alunos('nome','idade','email')VALUES(?,?,?)",('Gabriel',17,'gabrielsantos81@gmail.com'))
#cursor.execute("INSERT INTO alunos('nome','idade','email')VALUES(?,?,?)",('Isabella',16,'isaa5561@gmail.com'))
#cursor.execute("INSERT INTO alunos('nome','idade','email')VALUES(?,?,?)",('Carlos',18,'carlao0102@gmail.com'))
#cursor.execute("INSERT INTO alunos('nome','idade','email')VALUES(?,?,?)",('Heloyza',17,'heloyzao81462@gmail.com'))
#cursor.execute("INSERT INTO alunos('nome','idade','email')VALUES(?,?,?)",('Davi',19,'davi6608581@gmail.com'))
#cursor.execute("INSERT INTO alunos('nome','idade','email')VALUES(?,?,?)",('Wesley',17,'wesleysantos8484@gmail.com'))
print('Alunos adicionados\n')


conexao.commit()
conexao.close()

# R - Consultar todos os dados do banco
conexao = sqlite3.connect('escola.db')
cursor = conexao.cursor()

consulta = cursor.execute('SELECT * FROM alunos')
for escola in consulta.fetchall():
    print(f'Alunos:{escola[1]} - Idade:{escola[2]} - Email:{escola[3]}')
    
# U - atualizar um dado da tabela
cursor.execute("UPDATE alunos SET idade = ? WHERE id = ?", (19,1))
print('Registro atualizado\n')
conexao.commit()
conexao.close()

# D - Deletar um dado do banco
conexao = sqlite3.connect('escola.db')
cursor = conexao.cursor()

cursor.execute("DELETE from alunos WHERE id = ?",(3,))
conexao.commit()
conexao.close()

print('Aluno deletado com sucesso')

