# Esercizio di oggi

# Dobbiamo produrre un file con estensione .csv [comma separed value - (Nome, Cognome, Età, 55)]

# Ha origine negli anni '70/'80 quando i computer si dovevano telefonare (si chiamavano flussi di informazione)

# 1. Fare un file .csv                                     (formato antico)
# 2. Leggerlo e trasformarlo in un dizionario
# 3. Salvare il dizionario in formato .json
# 4. Leggere .json e trasformarlo in un dizionario         (formato moderno)


# Il formato JSON serve per essere utilizzato all'interno di "inter process communication", per far parlare più processi.
# Formati moderni: JSON (Java Script Object Notation), XML
# Esempio: Smartphone (Front End) - Cloud (Back End) ----------------- (vedi quaderno in data in oggetto)


# https -> Hyper Text Transfer Protocol Secure                         (come faccio a trasferire l'html)
# L'Hyper Text è scritto in HTML -> Hyper Text Markup Language         (come faccio una pagina web)

# <-------------------------------------------------------------------------------------------------------------------------->

# Scopo: Leggere un file CSV
#        Trasformarlo in un dizionario
#        Salvarlo in un file .JSON
#        Rileggerlo

# Il file si chiama dati.csv

# <-------------------------------------------------------------------------------------------------------------------------->

import os 
import uuid                                            # Universal United IDentifier
import json                                            # Una volta che ho il codice importo json

filename = 'dati.csv'
# filenameCompleto = os.path.abspath(filename)           # Dato che ci serve il percorso assoluto dobbiamo scrivere questo
filenameCompleto = 'C:\\Users\\lucas\\Desktop\\Python - Scuola Camerana\\PPBD02\\_personale\\Appunti\\Enrico\\2024_03_28\\dati.csv'

# Per non scrivere:

# ff = open(filenameCompleto, 'r', encoding = 'utf-8')
# contenuto = ff.read()
# ff.close()

# Scriviamo questo equivalente per rendere atomica l'azione,
# in modo che apra il file e chiuda il file (se c'è un errore il file rimane aperto)

with open(filenameCompleto, 'r', encoding = 'utf-8') as fr:      
    contenuto = fr.read()

righe = contenuto.split('\n')                          # Splitta i dati in base al ritorno a capo

dizDati = {}                                           # Intanto creo un dizionario vuoto

for r in righe[1:]:                                    # Voglio eliminare la prima riga di dati, non mi serve -> [1:]
    colonne = r.split(';')
    chiave = str(uuid.uuid4())

    dizDati[chiave] = {}                               # Stiamo facendo un dizionario di dizionari
    dizDati[chiave]['Cognome'] = colonne[0]
    dizDati[chiave]['Nome'] = colonne[1]
    dizDati[chiave]['Età'] = colonne[2]
    dizDati[chiave]['Indirizzo'] = colonne[3]

# Ora ho l'intero dizionario, lo stampo
    
print(dizDati)

strDati = json.dumps(dizDati)                           # Me lo dumpi in un dizionario json, trasforma il dizionario in file json

# diz2 = json.loads(strDati)                            # Trasforma il json in dizionario
# print(diz2)

filename = 'dati.json'
# filenameCompleto = os.path.abspath(filename)
filenameCompleto = 'C:\\Users\\lucas\\Desktop\\Python - Scuola Camerana\\PPBD02\\_personale\\Appunti\\Enrico\\2024_03_28\\dati.json'

with open(filenameCompleto, 'w', encoding = 'utf-8') as fw:
    fw.write(strDati)

print(strDati)
