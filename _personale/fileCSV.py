#Scopo: leggere un fuile CSF
    #   Trasformarlo in un dizionario
    #   Salvarlo 
    #   rileggerlo

    #   il file si chiama dati.csv



import os
import uuid
import json

filname = 'dati.csv'
filenameCompleto = os.path.abspath(filename)

with open(filenameCompleto, 'r', encoding='utf-8') as fr: contenuto = fr.read()

righe = contenuto.split('\n')

dizDati = {}


for r in righe:
    colonne = r.split(';')
    chiave=str(uuid.uuid4())

    dizDati[chiave] = {}
    dizDati[chiave]['Cognome'] = colonne[0]
    dizDati[chiave]['Nome'] = colonne[1]
    dizDati[chiave]['Età'] = colonne[2]
    dizDati[chiave]['Indirizzo'] = colonne[3]
    

# ora ho l'intero dizionario: lo stampo    

print(dizDati)

strDati = json.dumps(dizDati)

filename = 'dati.json'
filenameCompleto = os.path.abspath(filename)


    
        