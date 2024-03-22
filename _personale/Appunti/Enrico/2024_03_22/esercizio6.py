from fibonacci import fibo

lunghezza = input('Lunghezza della lista: ')
lunghezza = int(lunghezza)

listaret = fibo(20)
#print(listaret)

x = 0 
for l in listaret:
    x+=1
    print(f'Elemento numero {x}, vale {l}')