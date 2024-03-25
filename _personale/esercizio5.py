





from esercizio3 import quadrato, rettangolo, triangolo
nomeFile = 'a.txt'

with open(nomeFile, 'r' , encoding = 'utf-8') as fr:
    dati = fr.read()

compiti = fr.split('\n')

for c in compiti: 

    componenti = c.split(',')

    figura = componenti[0]

    if figura == 'quadrato':
        print('\ncalcolo un quadrato')
        lato = int(componenti[1].split('=')[1])
        print(f'di lato {lato}.')
        p,a = quadrato(lato)
        print(f'risultato: Area = {a} e perimetro = {p}')

    elif figura == 'rettangolo':
        print('\ncalcolo un rettangolo')
        base = int(componenti[1].split('=')[1])
        altezza = int(componenti[2].split('=')[1])
        print(f' che ha base = {base} e altezza = {altezza}')
        p,a = rettangolo(base,altezza)
        print(f'risultato: Area = {a} e perimetro = {p}')

    elif figura == 'triangolo':
        print('\ncalcolo un triangolo')
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
        print(f'che ha base = {base}, altezza = {altezza} e lati{l1}, {l2}, {l3}')
        p,a = triangolo(base,altezza,l1,l2,l3)
        print(f'risultato: Area = {a} e perimetro = {p}')

    else:
        print(f'\nho trovato una figura sconosciuta: {figura}\n')


