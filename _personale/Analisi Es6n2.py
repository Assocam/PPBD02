# Analisi Es6n2

#-- Main()

stringa = input("Inserire una stringa:\n")

L_maiuscole = []
L_pari = []
count_digits = 0
L_vocali = []
stringa2 = stringa

for idx, char in enumerate(stringa):
    idx += 1

    if char.isupper():
        L_maiuscole.append(char) # contare e mettere all'interno le maiuscole in una lista
    
    if idx % 2 == 0: # usando il contatore si tiene conto della posizione della lettera
        L_pari.append(char) # aggiungo la lettera(se in una posizione pari) ad una lista
    
    if char.isdigit(): # controlla se la lettera è una cifra
        count_digits += 1 # conta quante cifre ci sono all'interno della stringa
    
    if char.lower() in 'aeiou': # controllo se ci sono vocali nella stringa
        L_vocali.append((idx, char)) # aggiungo ad una lista le posizioni delle vocali nella stringa
        stringa2 = stringa2.replace(char, '_') # rimpiazzia le vocali con '_'


print (f'Le lettere maiuscole sono: {L_maiuscole}\n'
       f'Le lettere in posizioni pari sono: {L_pari}\n'
       f'Il numero di cifre è: {count_digits}\n'
       f'Le posizioni delle vocali sono: {L_vocali}')

print (f'La stringa originale è:\n{stringa}\n'
       f'La stringa rimpiazzata è:\n{stringa2}')


    
