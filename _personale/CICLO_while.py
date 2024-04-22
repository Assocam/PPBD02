# CILO "while"                                ciclo continuo

def chiedi_continua():
     while True:
        risp = input('Vuoi continuare? s/n e poi premi invio:')
        # Trasformo la risp in minuscolo prendendo il primo carattere
        risp = risp.lower()[0] if risp != '' else None                   # op ternario

        if risp in['s', 'n']:                           
            return risp                               # return blocca il ciclo dentro la funzione
        
        else:
            pass

while True:

    x = input('Prego, inserire un numero')                    # Per creare un'input da inserire in alto
                                                          
    if x.replace('.', '').isdigit():
        x = float(x)
 
        print(f'{x} > 0 and {x} < 100 :', x > 0 and x < 100)                 
        print(f'{x} > 0 or {x} < 100 :', x > 0 or x < 100)                    
        print(f'{x} > 0 or 100 < {x} :', x > 0 or 100 < x)                   
        print(f'{x} > 0 and {x} < 100 or {x} == -1 :', 
              x > 0 and x < 100 or x == -1)
        
        risp = chiedi_continua()

        if risp == 's':
            pass
            
        else:
            break

    else:
        print('Hai inserito un valore non valido: ', x)