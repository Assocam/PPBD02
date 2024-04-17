# Imports
from datetime import date
#-Main()
dati = {}
dict_eta = {}
anno_corrente = date.today().year

with open('C:\\Users\\Gigi3\\Desktop\\PythonP\\PPBD02\\files_esercizi\\nomi_data_nascita.txt', mode='r', encoding='utf-8') as  f:
    file = f.readlines()
    for line in file:
        line = line.strip('\n').split(':')
        dati[line[0]] = (line[1])

for e in dati:
    eta = anno_corrente - int(dati[e])
    dict_eta[e] = eta

with open('C:\\Users\\Gigi3\\Desktop\\PythonP\\PPBD02\\_personale\\outputs\\nomi_eta.csv', mode='+w', encoding='utf-8') as f:
    file = f
    file.write('Nome, Età, Anno di nascita\n')
    for e in dict_eta:
        file.write(f'{e}, {dict_eta[e]}, Nato/a il{dati[e]}\n')




