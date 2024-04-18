# Imports
from datetime import date
#-Main()
dati = {}
dict_eta = {}
anno_corrente = date.today().year
dict_sub = {}

with open('./files_esercizi/nomi_data_nascita.txt', mode='r', encoding='utf-8') as  f:
    file = f.readlines()
    for line in file:
        line = line.strip().split(':')
        dati[line[0]] = (line[1]) # Dati = {Nome, Anno di nascita}

for e in dati:
    eta = anno_corrente - int(dati[e])
    dict_eta[e] = eta # Dict_eta = {Nome, età}
    if eta in dict_sub:
        dict_sub[eta] = f'{dict_sub[eta]}; {e}'
    else:
        dict_sub[eta] = e

with open('./_personale/outputs/nomi_eta.csv', mode='+w', encoding='utf-8') as f:
    file = f
    file.write('Nome, Età, Anno di nascita\n')
    for e in dict_eta:
        file.write(f'{e}, {dict_eta[e]}, Nato/a il{dati[e]}\n')
    file.write('\nEtà, Persone\n')
    for e in dict_sub:
        file.write(f'{e}, {dict_sub[e]}\n')