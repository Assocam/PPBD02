import math

def reciproco(numero):
    
    try:
        risultato = 1/numero
    except:
        risultato = 0
    return risultato
print(reciproco(4))

def radicequadrata(numero):
    
    try:

        risultato = math.sqrt(numero)

    except Exception as e:

        risultato = 0
        print(e.__repr__())
        
    return risultato


print(reciproco(9))
print(radicequadrata(-9))

