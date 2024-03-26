#prima di tutto devo leggere il file
#poi devo, per ogni riga, stabilire quale forma è
#devo anche stabilire la forma, estrarre i dati dei lati
#per ognuno calcolare area e perimetro
#e stamparlo.

from esercizio3 import quadrato, rettangolo, triangolo


# from flask import jsonify

import json 

nomeFile = 'C:\\Users\\lucas\Desktop\\Python - Scuola Camerana\\PPBD02\\_personale\\Appunti\\Enrico\\2024_03_22\\a.txt'

with open(nomeFile, 'r',encoding='utf-8') as fr:
    dati = fr.read()

compiti = dati.split('\n')

contatore = 0

dizio = {}

for c in compiti: 

    contatore += 1
    # contatore = contatore + 1
    
    componenti = c.split(',')

    figura = componenti[0]
    chiave = contatore
    dizio[chiave] = {}

    if figura == 'quadrato':
        #print('\ncalcolo un quadrato')
        lato = int(componenti[1].split('=')[1])
        #print(f'di lato {lato}.')
        p,a = quadrato(lato)
        #print(f'risultato: Area = {a} e perimetro = {p}')
        dizio[chiave] = {'figura':figura,
                         'lato':lato,
                         'area':a,
                         'perimetro':p}

    elif figura == 'rettangolo':
        #print('\ncalcolo un rettangolo')
        base = int(componenti[1].split('=')[1])
        altezza = int(componenti[2].split('=')[1])
        #print(f' che ha base = {base} e altezza = {altezza}')
        p,a = rettangolo(base,altezza)
        #print(f'risultato: Area = {a} e perimetro = {p}')
        dizio[chiave] = {'figura': figura,
                         'base': base,
                         'altezza': altezza,
                         'area': a,
                         'perimetro': p}


    elif figura == 'triangolo':
       #print('\ncalcolo un triangolo')
        base = int(componenti[1].split('=')[1])
        altezza = int(componenti[2].split('=')[1])
        l1 = int(componenti[3].split('=')[1])
        l2 = int(componenti[4].split('=')[1])
        l3 = int(componenti[5].split('=')[1])                                            #componente[4] = 'lato2=50'
                                                                                         #se splitto ('=') ottengo una lista
                                                                                         #'lato2'       elemento 0 della lista
                                                                                         #'50'          elemento 1 della lista
                                                                                         # poi voglio l'intero dell'elemento 1
                                                                                         # della lista quindi '50' -> 50
        
        #print(f'che ha base = {base}, altezza = {altezza} e lati{l1}, {l2}, {l3}')
        p,a = triangolo(base,altezza,l1,l2,l3)
        #print(f'risultato: Area = {a} e perimetro = {p}')
        dizio[chiave] = {'figura': figura,
                         'base': base,
                         'altezza': altezza,
                         'lato1': l1,
                         'lato2': l2,
                         'lato3': l3, 
                         'area': a,
                         'perimetro': p}

    #else:
        #print(f'\nho trovato una figura sconosciuta: {figura}\n')


    # if figura == 'quadrato':
    #     pass
    # elif figura == 'rettangolo':
    #     pass
    # elif figura == 'triangolo':
    #     pass

   
    else:
        dizio[chiave] = {'figura': figura}


print(dizio)

djstr = json.dumps(dizio)   # Jsonifizziamo il dizionario, la differenza tra dizionario e json sono virgolette
                            # e che le chiavi sono tutte stringhe ("1" e non 1)
print(djstr)

# adesso che ho il formato json stringa,
# voglio scriverlo in un file.

file = "C:\\Users\\lucas\Desktop\\Python - Scuola Camerana\\PPBD02\\_personale\\Appunti\\Enrico\\2024_03_22\\a.json"

with open(file, 'w') as fw:
    fw.write(djstr)