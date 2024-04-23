# Classe che permette la gestione degli utenti
import requests
import json

class Utente:

    def __init__(self):
        
        self.Status = 'LOGOUT'  # Di default è logout
        self.Nome = 'Nome'
        self.Cognome = 'Cognome'
        self.Username = 'User'
        self.Password = 'Password'

        self.key = ''  # Una chiave che identifica l'utente


    def __repr__(self):

        return self.key + ': -> ' + self.Nome + '' + self.Cognome
    
    def DoLogin(self, u, p):      # u: username, p: password

        # Chiamo il backend ed eseguo il login
        # Esito: 200 - Ok -> Status = 'LOGIN'
        #        altro codice -> Status = 'LOGOUT'

        # Il login lo deve fare il backend,
        # predispongo la chiamata

        # API:          /login   # definisco la rotta
        # Metodo:       POST
        # Parametri:    {"USER: "Utente", "PASSWORD": "Pwd"}
        # Risposta:     {"KEY": "???", "NOME": "nnnn", "COGNOME": "cccccc"}
        # Return code:  200 - OK
        #               404 - Not found (utente non trovato)
        #               403 - Forbidden (utente ha già fatto il login)
        #               405 - Method not allowed (metodo sbagliato)
        #               500 - Internal Server Error (ogni altro errore)

        # Preparo i dati da inviare 
        dati = {}
        dati['USER'] = u
        dati['PASSWORD'] = p

        # Preparo i dati in formato JSON

        datiJson = json.dumps(dati)

        # Effettuo la richiesta

        risposta = requests.post('http://127.0.0.1/login', json = datiJson)     # metodo post

        # Analizzo la risposta 

        codice = risposta.status_code

        if codice == 200: # Tutto ok
            ret = risposta.text
            dRet = json.loads(ret)                                              # dizionario risposte
            print(dRet)

        else:
            
            dRet = {}
            print(risposta.text)
















