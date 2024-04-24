# Deve tenere conto delle ROTTE necessarie a gestire le API
# e deve usare un gestore di API.

from flask import Flask, request
import json
import sys

sys.path.append("C:\\Users\\lucas\\Desktop\\Python - Scuola Camerana\\PPBD02\\_personale\\Progetto_chat")

import sqlite3  # Per il database
import os

from Classi.cConfig import Config

# In app config il percorso era: C:\\Users\\lucas\\Desktop\\Python - Scuola Camerana\\PPBD02\\chat.db
# In pratica in questo modo gli sto indicando la cartella del file database dove leggerla
# Il vantaggio di usare la classe Config è che posso andare a indicare diversi database (app.config/app.config2)
# O indicare diverse cose a back-end e front-end
cfg = Config("_personale\\Progetto_chat\\BackEnd\\app.config")
cfg.LeggiConfig()

conn = sqlite3.connect(cfg.DBFile)


# Start
chat = Flask('AppChat')


def CercaUtente(usr, pwd):

    # # Queste tre righe vanno bene

    # file_database = "chat.db"   
    # cartella = os.getcwd()
    # percorso_db = os.path.join(cartella, file_database)

#################################################################################################################

    # nomedb = os.path.abspath('chat.db')
    # print(nomedb)

#   conn = sqlite3.connect('chat.db')
    conn = sqlite3.connect(cfg.DBFile)

    cur = conn.cursor()

    # "*" IN SQL = "ALL"
    SQL = """
        SELECT * FROM RUBRICA
        WHERE USERNAME = ? AND
        PASSWORD = ?
        """

    cur.execute(SQL,(usr,pwd))  # eseguiamo il codice sql su tupla user, pwd

    righe = cur.fetchone()      # prendi una riga

    if righe:
        id,nome,cognome,u,p = righe

        dictRet = {}
        dictRet['KEY'] = id
        dictRet['NOME'] = nome
        dictRet['COGNOME'] = cognome
        
        dictJson = json.dumps(dictRet)
        retCode = 200

    else:

        dictJson = 'Utente non trovato'
        retCode = 404


    return dictJson, retCode


# Quello che c'è sotto lo faccio su tutte le rotte
# Tutte le rotte
@chat.route('/login', methods = ['POST'])

def FaiLogin():

    retcode = 0
    retdata = 'Ciccio'

    # da implementare
    try:
    # recupero i dati:

        datiJson = request.json
        dati = json.loads(datiJson)

        user = dati['USER']
        pwd = dati['PASSWORD']

        # Chiamo CercaUtente(u, p)
        retdata, retcode = CercaUtente(user,pwd)

    except Exception as e:
        retdata = "C'è qualche casino con i dati\n" + e.__repr__()
        retcode = 500

    return retdata, retcode




@chat.route('/scriviMsg', methods = ['PUT', 'GET'])  # Se metto solo put mi da errore 500 - "Method not allowed"
#                                                      Solo put per scrivere

#@chat.route('/scriviMsg')      # "@"" indica un decoratore. Visto che chat lo gestisce Flask, uso un metodo route, che non modifica
def wMessage():                 # ma decora. Cos'è un decoratore? Vedi quaderno (10/04/2024 - Pagina "2")
#                               # se vado su chrome e scrivo: "http://127.0.0.1/scriviMsg" (127.0.0.1 è questo pc)
    
    metodo = request.method
    
    return f'Cippirimerlo {metodo}'  # Mi faccio dire il metodo e il codice di errore


@chat.route('/leggiMsg', methods = ['GET', 'POST'])  # Così nessun errore. Se non scrivo niente il metodo generico è get.
#@chat.route('/leggiMsg')                              solo get per leggere
def RMessage():
    
    metodo = request.method

    # Errore:
    # b = 1/0

    return f'Ti piacerebbe leggere il messaggio... {metodo}'


# Run
if __name__ == '__main__':                   # se il nome del modulo è il modulo principale (entry module dell'applicazione)
    chat.run(host='0.0.0.0', port = 80)      # port = 80 così evitiamo i firewall

