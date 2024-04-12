def fattoriale(x):
    
    risultato = 1
    for x in range (1,x+1):
        risultato *= x

    return risultato

fattoriale(16)