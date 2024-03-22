#serie dei fibonacci:

#prende la somma dei numeri precedenti

#esempio

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ecc.

def fibo(lunghezza):


    pri = 0
    sec = 1

    listaFibo = []                                            # lista

    for x in range(lunghezza):

        fibonacci = pri + sec
        #print(x+1, fibonacci)
        listaFibo.append(fibonacci)
        pri = sec
        sec = fibonacci 

    return listaFibo 


#--------------------------------------------------------------------
#lun = input('inserire lunghezza desiderata:')        
#lun = int(lun)
#risultato = fibo(lun)        
#print(risultato)
