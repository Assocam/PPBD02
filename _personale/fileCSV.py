
import os
import uuid
import json

filename = "//workspaces//PPBD02//_personale//dati.csv"
filenameCompleto = os.path.abspath(filename)

with open(filenameCompleto, 'r', encoding = 'utf-8') as fr:    # Atomica lettura e chiusura
    contenuto = fr.read()

righe = contenuto.split('\n')

dizDati = {}

for r in righe:                  # for r in righe[1:]: fa saltare la lista
    colonne = r.split(';')
    chiave = str(uuid.uuid4())

    dizDati[chiave] = {}
    dizDati[chiave]['Cognome'] = colonne[0]
    dizDati[chiave]['Nome'] = colonne[1]
    dizDati[chiave]['Età'] = colonne[2]
    dizDati[chiave]['Indirizzo'] = colonne[3]

# Si ha l'intero dizionario
print(dizDati)

strDati = json.dumps(dizDati)                           # Formato Json ""
# diz2 = json.loads(strDati)                               

filename = 'dati.json'
filenameCompleto = os.path.abspath(filename)

with open(filenameCompleto, 'w') as fw:
    fw.write(strDati)

print(strDati)