# scrivi qui
import os
import uuid
import json
from datetime import date                              

anno_corrente = date.today().year                                         

filename = "//workspaces//PPBD02//_personale//nomi_data_nascita.txt"     
filenameCompleto = os.path.abspath(filename)

with open(filename, 'r', encoding = 'utf-8') as fr:            
    contenuto = fr.readlines()

report = {}               

for line in contenuto:

    lista_oggetti = line.split(':')                         
                                     
    nome = lista_oggetti[0].strip()                         
    anno = int(lista_oggetti[1].strip())
    eta = anno_corrente - anno

    if eta in report:                                        
        report[eta].append(nome)

    else:
        report[eta] = [nome]

report

strDati = json.dumps(report)

filename = 'dati.json'
filenameCompleto = os.path.abspath(filename)

with open(filenameCompleto, 'w') as fw:
    fw.write(strDati)

    print(strDati)


with open('./outputs/nomi_eta.csv', 'w' , encoding = 'utf-8') as output_file:

    intestazione = 'nome;eta\n'       # \n
    output_file.write(intestazione)

    for eta in report:
        for nome in report[eta]:
            riga = nome + ';' + str(eta) + '\n'
            print(riga)
            #riga = f'{nome},{eta}\n'
            #print(riga)              # scrittura alternativa
            output_file.write(riga)
