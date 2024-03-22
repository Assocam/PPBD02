from fibonacci import fibo

#listaret = fibo(20)
#print(listaret)
lunghezza = input('Lunghezza della lista: ')
lunghezza = int(lunghezza)

listaret = fibo(lunghezza)

x = 0
for l in listaret:
    x+=1
    print(f'Elemento numero {x}, vale {l}')

