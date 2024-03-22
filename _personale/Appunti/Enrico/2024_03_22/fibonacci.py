#serie di fibonacci

#prende la somma dei due numeri precedenti a n

#esempio

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ecc.

# primo = 0
# secondo = 1

# for x in range(5):

#     fibonacci = primo + secondo
#     print(x+1, fibonacci)
#     primo = secondo
#     secondo = fibonacci

# <--------------------------------------------------->

def fibo(lunghezza):      # fibo è il simbolo

    primo = 0
    secondo = 1

    listaFibo = []

    for x in range(lunghezza):

        fibonacci = primo + secondo
        #print(x+1, fibonacci)
        listaFibo.append(fibonacci)
        primo = secondo
        secondo = fibonacci

    return listaFibo

# <------------ definito il simbolo ---------->7

# lun = input('Inserire un numero: ')
# lun = int(lun)
# risultato = fibo(lun)
# print(risultato)