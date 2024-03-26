



import os

from esercizio3 import quadrato, rettangolo, triangolo
nomeFile = 'C:\\Users\\marco\\OneDrive\\Desktop\\Lavoro git\\PPBD02\\a.txt'

nomeFileassoluto = os.path.abspath('a.txt')    

with open(nomeFile, 'r' , encoding = 'utf-8') as fr:
    dati = fr.read()


compiti = fr.split('\n')

contatore = 0

dizio = {}

for c in compiti:

    contatore +=1

    componenti = c.split(',')
    chiave = contatore
    figura = componenti[0]


    if figura == 'quadrato':
        lato = int(componenti[1].split('=')[1])
        p,a = quadrato(lato)
        dizio[chiave] = {'figura': figura, 'lato': lato, 'area': a, 'perimetro': p}
       

    elif figura == 'rettangolo':
        base = int(componenti[1].split('=')[1])
        altezza = int(componenti[2].split('=')[1])
        p,a = rettangolo(base,altezza)
        dizio[chiave] = {'figura': figura, 'base': base, 'altezza': altezza, 'area': a, 'perimetro': p}    
        

    elif figura == 'triangolo':
        base = int(componenti[1].split('=')[1])
        altezza = int(componenti[2].split('=')[1])
        l1 = int(componenti[3].split('=')[1])
        l2 = int(componenti[4].split('=')[1])
        l3 = int(componenti[5].split('=')[1]) 
        dizio[chiave] = {'figura': figura, 'base': base, 'altezza': altezza, 'lato1': l1, 'lato2': l2, 'lato3': l3, 
                         'area': a, 'perimetro': p}
                                                                                         #componente[4] = 'lato2=50'
                                                                                         #se splitto ('=') ottengo una lista
                                                                                         #'lato2'       elemento 0 della lista
                                                                                         #'50'          elemento 1 della lista
        print(f'che ha base = {base}, altezza = {altezza} e lati{l1}, {l2}, {l3}')
        p,a = triangolo(base,altezza,l1,l2,l3)
        print(f'risultato: Area = {a} e perimetro = {p}')

    else:
        print(f'\nho trovato una figura sconosciuta: {figura}\n')


    chiave = contatore

    dizio = [chiave] = {}
    if figura == 'quadrato':
    elif figura == 'rettangolo':
    elif figura == 'triangolo':
       
    else:
        dizio[chiave] = {'figura': figura}   

print(dizio)        