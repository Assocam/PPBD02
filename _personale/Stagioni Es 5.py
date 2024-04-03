# Stagioni Es 5
def mese_input():
    while True:
        q = input ("inserire il mese in numero: ")
        if q.isdigit():
            q = int(q)
            if q in range (1, 13): # q <= 12 and q != 0; by using range i can check at once.
                return q
            else:
                print ("Il numero inserito non è un mese!", q)
                continue
        else: 
            print ("Il numero inserito non è un mese!", q)
            continue
def giorno_input(x):
    while True:
        q = input("Inserire un giorno: ")
        if q.isdigit():
            q = int(q)
            if x in (1, 3, 5, 7, 8, 10, 12):
                if q <=31 and q != 0: 
                    return q 
                else: 
                    print (f'Il giorno {q} non corrisponde con il mese {x}!')
                    continue
            if x in (4, 6, 9, 11):
                if q <=30 and q != 0: 
                    return q
                else:
                    print (f'Il giorno {q} non corrisponde con il mese {x}!')
                    continue
            if x == 2:
                if q <=29 and q != 0: 
                    return q
                else:
                    print (f'Il giorno {q} non corrisponde con il mese {x}!')                
                    continue
#- Main()
mese = mese_input()
giorno = giorno_input(mese)

stagione = ""

if mese in (1, 2, 3):
    stagione = 'Inverno'
elif mese in (4, 5, 6):
    stagione = 'Primavera'
elif mese in (7, 8, 9):
    stagione = 'Estate'
else:
    stagione = 'Autunno'

if not (mese % 3) and giorno >= 21: # 'not (mese % 3)' is the same as 'mese % 3 == 0'
    if stagione == 'Inverno': 
        stagione = 'Primavera'
    elif stagione == 'Primavera': 
        stagione = 'Estate'
    elif stagione == 'Estate': 
        stagione = 'Autunno'
    else: 
        stagione = 'Inverno'



print (f'Il giorno è {giorno} del mese {mese}, '
       f'La stagione è: {stagione}')