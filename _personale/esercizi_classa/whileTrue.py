def chiedi_continua():
    while True:
        risp = input('vuoi continuare o ti vuoi fermare: si \ no: ')
        # transformo la risposta in minuscolo e prendo il primo carattere 
        risp = risp.lower()[0] if risp else None

        # se l'utente ha risposto 'si' o 'no'
        # if risp == 'si' or risp == 'n':
        if risp in ['si', 'no']:
            # restituisce l'input utente ed esce dal ciclo
            return risp
        
        # se l'utente ha inserito un valore non valido
        else:
            # non fa nulla ( e dunque riparte il ciclo while )
            pass


while True:

    x = (input('Prego , inserire un numero:'))

    if x.replace('.', '').isdigit():
        x = float(x)

        print(f'{x} > 0 and {x} < 100 : ', x > 0 and x < 100)
        print(f'{x} > 0 or  {x} < 100 : ', x > 0 or x < 100)
        print(f'{x} > 0 or 100 < {x}  : ', x > 0 or 100 < x)
        print(f'{x} > 0 and {x} < 100 or {x} == -1', x > 0 and x < 100 or x == -1)
    
        risp = chiedi_continua
        if risp == 'si':
            pass
        else:
            break 
    
    else: 
        print('hai inserito un valore non valido: ', x)
        break
    
    


    
    

    
