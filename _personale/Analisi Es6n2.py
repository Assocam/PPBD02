# Analisi Es6n2

#-- Main()

stringa = input("Inserire una stringa:\n")

L_upper = []
L_pari = []
count_pari = 0
L_vocali = []
stringa2 = ''

for n in stringa:
    if n.isupper():
        L_upper.append(n)
    if n.count(stringa) % 2 == 0:
        L_pari.append(n)
    if n.isdigit():
        count_pari += 1
    if n.lower() in ('a', 'e', 'i', 'o', 'u'):
        L_vocali.append(n.count(stringa))
for n in stringa:
    if n.lower() in ('a', 'e', 'i', 'o', 'u'):
        stringa2 = stringa.replace(n, '_')

print (f'Le lettere maiuscole sono: {L_upper}\n'
       f'Le lettere in posizioni pari sono: {L_pari}\n'
       f'Il numero di cifre è: {count_pari}\n'
       f'Le posizioni delle vocali sono: {L_vocali}')

print (f'La stringa originale è:\n{stringa}\n'
       f'La stringa rimpiazzata è:\n{stringa2}')


    
