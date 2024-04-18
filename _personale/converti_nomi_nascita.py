# Imports
from datetime import date
import sys
args = sys.argv
#-Main()
anno_corrente = date.today().year
dati = {} # dict = {nome, anno di nascita}
dict_eta = {} # dict = {nome, eta}
dict_sub = {} # dict = {eta, nomi di persone con quell'età}
output_file = [] # lista di line da scrivere nei nuovi files

input_path = args [1]
output_path1 = args[2]
output_path2 = args[3]

filePath = './files_esercizi/nomi_data_nascita.txt'
with open(input_path, mode='r', encoding='utf-8') as  f:
    file = f.readlines()
    for line in file:
        line = line.strip().split(':')
        dati[line[0]] = (line[1])

for e in dati:
    eta = anno_corrente - int(dati[e])
    dict_eta[e] = eta 
    if eta in dict_sub: 
        dict_sub[eta] = f'{dict_sub[eta]}, {e}'
    else:
        dict_sub[eta] = e

filePath = './_personale/outputs/nomi_eta.csv'
with open(output_path1, mode='+w', encoding='utf-8') as f:
    file = f
    output_file.append('Nome, Età, Anno di nascita:\n')
    for e in sorted(dict_eta):
        output_file.append(f'{e}, {dict_eta[e]}, Nato/a il{dati[e]}\n')
    output_file.append('\n')
    file.writelines(output_file)

output_file = []

filePath = './_personale/outputs/eta_nomi.txt'
with open(output_path2, mode='+w', encoding='utf-8') as f:
    file = f
    file.write('Età: Persone\n')
    for e in sorted(dict_sub):
        file.write(f'{e}: {dict_sub[e]}\n')
    file.write('\n')