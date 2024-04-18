import sys

args = sys.argv

#print(args)  # è una lista di un elemento contenente il percorso del file, ovvero il nome del file
#             # ['c:/Users/lucas/Desktop/Python - Scuola Camerana/PPBD02/_personale/moltiplica_due_numeri.py']
#             # posso usarlo per sapere il percorso del file sul quale sto scrivendo lo script

# se mi metto sul terminale sul percorso file (tasto destro sul file - open in integrated terminal)
# "py" + mol(premi tab per trovare il file)

# Eseguo: py .\moltiplica_due_numeri.py


# Ottengo: 

# PS C:\Users\lucas\Desktop\Python - Scuola Camerana\PPBD02\_personale> py .\moltiplica_due_numeri.py
# ['.\\moltiplica_due_numeri.py']
# PS C:\Users\lucas\Desktop\Python - Scuola Camerana\PPBD02\_personale> 

primo_num = float(args[1])       # trasformo il numero scritto da stringa a numero float
secondo_num = float(args[2])     # trasformo il numero scritto da stringa a numero float

risultato = primo_num * secondo_num

print(f'Il prodotto di {primo_num} e {secondo_num} è: {risultato}')

