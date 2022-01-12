from database import *
import stampaMenu as m

con = creaConn()
cur = creaCursor(con)

# executeSQL('CREATE TABLE ingredients(ID, name, IDtypology)', cur)
# executeSQL('CREATE TABLE typology(ID, typology)', cur)

#executeSQL("INSERT INTO ingredients VALUES(2, 'Banane', 1)", cur)
#executeSQL("INSERT INTO typology VALUES(2, 'Salumi')", cur)

#executeSQL('UPDATE typology SET ID=3 WHERE typology = "Scatolame"', cur)

# executeSQL("DELETE FROM typology WHERE ID = 1", cur)

'''
print('--------------------------------------------------------')

print('INGREDIENTI')
print(' ID  NOME    TIPO')
for row in cur.execute('SELECT * FROM ingredients'):
    print(row)
print('--------------------------------------------------------')

print('TIPOLOGIA')
print(' ID  TIPO')
for row in cur.execute('SELECT * FROM typology'):
    print(row)
print('--------------------------------------------------------')

print('INGREDIENTI')
print(' ID  INGR.    TIPO')
for row in cur.execute('SELECT i.ID, i.name, t.typology  FROM ingredients as i INNER JOIN typology as t on i.ID=t.ID'):
    print(row)
print('--------------------------------------------------------')
'''
opt = m.printMenu(cur)

# Save (commit) the changes
con.commit()

con.close()