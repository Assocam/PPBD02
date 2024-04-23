import requests
import json

# Facciamo il frontend - PER LANCIARE QUESTO CODICE è NECESSARIO ATTIVARE SUL CMD IL FILE BackEnd.py
# Una volta posti nella cartella in cui si trova il file scrivere: "py BackEnd.py"

dati = {}
dati['user'] = 'pippo'
dati['password'] = 'cicciobello'

datij = json.dumps(dati)

risposta = requests.post('http://127.0.0.1:80/login', json = datij)

# Gli errori possibili si trovano qui: https://it.wikipedia.org/wiki/Codici_di_stato_HTTP

if risposta.status_code == 200:                 # Gli stiamo dicendo cosa scrivere in caso di errore 200
    print('A posto!')
elif risposta.status_code == 405:
    print('Metodo sbagliato!')
else:
    print('qualcosa non va', risposta.status_code)

print(risposta.reason)