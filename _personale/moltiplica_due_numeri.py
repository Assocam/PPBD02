import sys

args = sys.argv
print(args)
# "C:/Program Files/Python312/python.exe" "c:/Users/admin/OneDrive/Desktop/Python Projects/git/PPBD02/_personale/moltiplica_due_numeri.py"
# ['c:/Users/admin/OneDrive/Desktop/Python Projects/git/PPBD02/_personale/moltiplica_due_numeri.py']
# stampa il percorso .

primo_num = float(args[1])
secondo_num = float(args[2])
risultato = primo_num * secondo_num
print(f'Il prodoto di {primo_num} per {secondo_num} è uguale a {risultato}')




