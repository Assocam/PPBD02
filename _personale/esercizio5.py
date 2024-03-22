





from esercizio3 import quadrato, rettangolo, triangolo
nomeFile = 'a.txt'

with open(nomeFile, 'r' , encoding = 'utf-8') as fr:
    dati = fr.read()

compiti = fr.split('\n')

for c in compiti:

    componenti = c.split(',')

    figura = componenti(0)

    if figura == 'quadrato':
        print('calcolo un quadrato')
        lato = componenti[1]
        print(f'di lato {lato}.')
        p, a = quadrato(lato)
        print(f'risultato: Area')













