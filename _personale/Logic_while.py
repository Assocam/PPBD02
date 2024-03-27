# CICLO WHILE - In modo da tornare a inizio codice

def chiedi_continua():
    while True:
        risp = input('Vuoi continuare? (s/n): ')                # Converte la risposta in minuscolo e prende la prima lettera
        risp = risp.lower()[0] if risp else ''                  # If risp è truthy/falsy, è come dirgli che non è un oggetto vuoto
        # risp = risp.lower()[0] if risp != '' else None      
        # if risp == 's' or risp == 'n':     
        if risp in ['s', 'n']:                                  # Se la risposta non è tra le opzioni della lista
            return risp                                         # Restituisce l'input
        else:                                                   # Se l'utente ha inserito un valore non valido
            pass                                                # Non fa nulla (e dunque riparte il ciclo while)
                                                                # richiede se vuoi continuare

while True:

    x = input('Prego, inserire un numero: ')
    
    if x.replace('.','').isdigit():
        x = float(x)
    
        print(f'{x} > 0 and x < 100:', x > 0 and x < 100)
        print(f'{x} > 0 or x < 100:', x > 0 or x < 100)
        print(f'{x} > 0 or 100 < x:', x > 0 or 100 < x)
        print(f'{x} > 0 and x < 100 or x == -1:', x > 0 and x < 100 or x == -1)
    
        risp = chiedi_continua()
      
        if risp == 's':
            pass                          # Continue = torna indietro; Pass = non fare nulla e torna al ciclo

        else:
            break                         # Così interrompe il codice a un ciclo, sennò andrebbe avanti all'infinito


    else:
        print(f'Hai inserito un valore non valido: {x}')