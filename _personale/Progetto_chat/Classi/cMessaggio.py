import datetime
import requests
import uuid        # Devo poter identificare univocamente il messaggio

class Messaggio: 

    def __init__(self, mitt, dest, msg):                       # Costruttore
        
        chiaveMSG = str(uuid.uuid4)                            # Devo poter identificare univocamente il messaggio per poter richiamare
#                                                              # la bozza e cambiargli status
        self.Mittente = mitt
        self.Destinatario = dest                               # Sarà una lista per adesemio fare un broadcast
        self.Testo = msg
        self.DTMessaggio = datetime.datetime.now()
        self.DTInvio = datetime.datetime.now()
        self.Status = 'BOZZA'                                  # Stato del messaggio 
        self.Chiave = chiaveMSG

    def Status(self, status):

        self.Status = status                                   # Devo poter modificare lo stato del messaggio

    def Invia(self):

        self.DTInvio = datetime.datetime.now()
        self.Status = 'INVIATO'

        # Tutta la procedura per mandare al mio backend i dati

    def Leggi(self, idMsg):
        
        # Leggo il messaggio idMsg dal backend
        pass
    