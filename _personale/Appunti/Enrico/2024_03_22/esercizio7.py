import json
from esercizio3 import quadrato

# Leggere il file di dati e ottenere un dizionario.

with open('C:\\Users\\lucas\Desktop\\Python - Scuola Camerana\\PPBD02\\_personale\\Appunti\\Enrico\\2024_03_22\\a.json', 'r', encoding='utf-8') as fr:
    buffer = fr.read()

diz = json.loads(buffer)

# print(diz)

#--------------------------------------------------

# Assegnazione:
# Se scrivo: a = 10, assegno il valore 10 intero alla variabile a
# a = 10.5 assegno il valore 10.5 float alla variabile a
# a = 'ciao' assegno una stringa alla variabile a

# Tuple:
# a = (3, 'ciao') assegno una tupla alla variabile a

# Liste:
# a = [] indico che "a" è una lista vuota
# a.append(valore a caso) aggiungo alla lista a un valore casuale
# a[4] indico che voglio il valore dell'elemento 4 nella lista a

# Dizionari
# a = {} indico che "a" è un dizionario vuoto
# a['ppp'] = 10 indico che nel dizionario alla chiave 'ppp' assegno il valore 10
# se la chiave 'ppp' non esiste, ne crea una


# Come si fa a ciclare in un dizionario? 

# Supponiamo io voglia sapere tutte le chiavi del dizionario

#----------------------------------------------------------------

# for k in diz.keys():
#     print(k)
#     print(diz[k])

#     if diz[k]['figura'] == 'quadrato':
#         print('ho trovato un quadrato')
#         lato = diz[k]['lato']

#         print(f'il cui lato è {lato}')

#         p,a = quadrato(lato)
#         print(f'di cui perimetro = {p} e area = {a}')

# -----------------------------------------------------------------

# dati di una tupla
        
# tp = ('ciao', 44, ('come', 'stai'), 'casa', 'automobile')

# print(tp)

# a1,a2,a3,a4,a5 = tp

# print(a1,a2,a3,a4,a5)

# b1,b2 = a3

# print(b1,b2)

# # dati di una lista

# lis = [3,7,4,1,99,12]
# print(lis)

# print(f'la lunghezza della lista è {len(lis)}')
# # se voglio l'elemento 3 (partendo da 0)
# print(lis[3])

# # se voglio dall'elemento 3 per 2 elementi
# print(lis[3:5])

# b='abcdefghi'
# print(b[:3])

# ---------------------------------------------------------------------

# lavoriamo con i dizionari

print(diz['4'])

# Se uso un indice che non esiste da Keyerror. Come possiamo prevenire?

try:                                                  # prova a fare questo

    print(diz['66'])

except Exception as e:                                # se non lo trovi fai questa eccezione
   
    print('chiave inesistente')
    print(e.__repr__())                                          # motivo del perché non esiste

