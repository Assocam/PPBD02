# Imports
from datetime import date
#-Main()
dati = {}
dict_eta = {}
anno_corrente = date.today().year
dict_sub = {}
lines = []

filePath = './files_esercizi/nomi_data_nascita.txt'
with open(filePath, mode='r', encoding='utf-8') as  f:
    file = f.readlines()
    for line in file:
        line = line.strip().split(':')
        dati[line[0]] = (line[1]) # Dati = {nome, Anno di nascita}

for e in dati:
    eta = anno_corrente - int(dati[e])
    dict_eta[e] = eta # Dict_eta = {nome, età}
    if eta in dict_sub: # Dict_sub = {età, nomi di persone}
        dict_sub[eta] = f'{dict_sub[eta]}, {e}'
    else:
        dict_sub[eta] = e

filePath = './_personale/outputs/nomi_eta.csv'
with open(filePath, mode='+w', encoding='utf-8') as f:
    file = f
    lines.append('Nome, Età, Anno di nascita\n')
    for e in sorted(dict_eta):
        lines.append(f'{e}, {dict_eta[e]}, Nato/a il{dati[e]}\n')
    lines.append('\n')
    file.writelines(lines)

lines = []

filePath = './_personale/outputs/eta_nomi.txt'
with open(filePath, mode='+w', encoding='utf-8') as f:
    file = f
    lines.append('Età: Persone\n')
    for e in sorted(dict_sub):
        lines.append(f'{e}: {dict_sub[e]}\n')
    lines.append('\n')
    file.writelines(lines)
    