import os

def printMenu(cur):

    choice=-1
    while(choice !='e'):
        print()
        print('MENU')
        print('-----------------------')
        print('1 - Vedi Ingredienti')
        print()
        print('-----------------------')
        print('Scegli 1-1, e per uscire')
        choice = input()
        os.system('cls')
        if(choice=='e'):
            exit()
        if(choice=='1'):
            for row in cur.execute('SELECT i.ID, i.name, t.typology  FROM ingredients as i INNER JOIN typology as t on i.ID=t.ID'):
                print(row)