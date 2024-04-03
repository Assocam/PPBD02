lista_pari = []
lista_dispari = []
numeri = []

somma = 0                      # La somma parte da 0

while True:

    user_input = (input(
        'Inserisci un numero e premi invio, '
        'oppure premi solo invio per terminare: ')
        )
  
    if not user_input:                 # If user_input --> se è piena è vero, se è vuota è falso (truthy or falsy)
        break                          # Se la stringa è vuota mi fermo ed esco dal ciclo, vado dopo riga 32
    else:
        user_input = int(user_input)   # Implementazione eventuali controlli prima della conversione in intero
        somma += user_input            # somma = somma + user input
        print(f'La somma parziale è: {somma}')
    
    numeri.append(user_input)      # Inserisco nella lista il numero inserito dall'utente
        

max_lista = max(numeri)
min_lista = min(numeri)


print(f'Ho creato una lista: {numeri}.')
print(f'Valore massimo: {max_lista}\nValore minimo: {min_lista}')


valori_pari = 0
valori_dispari = 0


for num in numeri:
    if num % 2:      # Quando non si mettono condizioni solitamente vuol dire implicitamente vero, quindi che % da valore pieno, ovvero
                     # c'è resto, quindi che è dispari
        lista_dispari.append(num)
        valori_dispari += 1
    else:
        lista_pari.append(num)
        valori_pari += 1



# prova mia senza for
# valori_pari += 1 if user_input % 2 == 0 else valori_pari
# valori_dispari += 1 if user_input % 2 != 0 else valori_dispari

print(f'Numero di valori pari: {valori_pari} - {lista_pari}\nNumero di valori dispari: {valori_dispari} - {lista_dispari}')



