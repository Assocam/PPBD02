# a = 10

# print(a, type(a))

# a = 'Ciao, come stai?'

# print(a, type(a))

# b = 30

# if a == b:
#     pass    # Python è un linguaggio posizionale, l'indentazione è importante, se scrivo fuori dall'indentazione da errore
            
# <------------------------------------------------------------------------------------------------------------------------------->

# In cosa usiamo if ed else?

# listanomi = ['mario', 'carlo', 'giuseppe', 'angela']

# numeronomi = len(listanomi)

# if numeronomi < 5:
#     print('Lista corta')
# else:
#     print('Lista abbastanza lunga')

# if 'giuseppe' in listanomi:
#     print('Esiste pure Giuseppe')

# <------------------------------------------------------------------------------------------------------------------------------->

# listanomi = ['mario', 'carlo', 'giuseppe', 'piero', 'angela']

# print(listanomi)

# for n in listanomi:    # Per ogni elemento nella lista applica un print
#     print(n)

# for x in range (len(listanomi)):
#     print(x, listanomi)

# for x in range(5,10,2):  # Conta da 5 a 10 e salta ogni due
#     print(x)

# <-------------------------------------------------------------------------------------------------------------------------------> 

listanomi = ['mario', 'carlo', 'giuseppe', 'piero', 'luisa', 'angela']

for x in listanomi:

    if x[0] == 'p':
        print(x, 'inizia con la p')                           # stiamo chiedendo per ogni elemento di verificare le condizioni
    elif x[0] == 'l':                                         # e stampare la condizione per ogni elemento
        print(x, 'inizia con la l')
    else:
        print(x, 'non comincia con la p o con la l')


# <------------------------------------------------------------------------------------------------------------------------------->

