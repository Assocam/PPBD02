# Deve tenere conto delle ROTTE necessarie a gestire le API
# e deve usare un gestore di API.

from flask import Flask, request
import json

import sqlite3  # Per il database

# Start
chat = Flask('AppChat')

# Tutte le rotte
@chat.route('/scriviMsg', methods = ['PUT'])  # Se metto solo put mi da errore 500 - "Method not allowed"
#                                               Solo put per scrivere

#@chat.route('/scriviMsg')      # "@"" indica un decoratore. Visto che chat lo gestisce Flask, uso un metodo route, che non modifica
def wMessage():                 # ma decora. Cos'è un decoratore? Vedi quaderno (10/04/2024 - Pagina "2")
#                               # se vado su chrome e scrivo: "http://127.0.0.1/scriviMsg" (127.0.0.1 è questo pc)
    
    metodo = request.method
    
    return f'Cippirimerlo {metodo}'  # Mi faccio dire il metodo e il codice di errore


@chat.route('/leggiMsg', methods = ['GET'])  # Così nessun errore. Se non scrivo niente il metodo generico è get.
#@chat.route('/leggiMsg')                      solo get per leggere
def RMessage():
    
    metodo = request.method

    # Errore:
    # b = 1/0

    return f'Ti piacerebbe leggere il messaggio... {metodo}'


# Run
if __name__ == '__main__':                   # se il nome del modulo è il modulo principale (entry module dell'applicazione)
    chat.run(host='0.0.0.0', port = 80)      # port = 80 così evitiamo i firewall

