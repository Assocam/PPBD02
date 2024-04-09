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

    def __repr__(self):   # metodo repr, mi serve per rappresentare l'oggetto, init è il costruttore, REPR È IL RAPPRESENTANTE

        msg = f'Da: {self.Mittente}, A: {self.Destinatario}'
        msg += f' Ti ha scritto: {self.Testo} \n'

        return msg

    def Invia(self):

        self.DTInvio = datetime.datetime.now()
        self.Status = 'INVIATO'

        # Tutta la procedura per mandare al mio backend i dati:
        # Compilare il formato JSON adatto
        # Vedi in documentazione, 
        # Chiamare la API apposita con request
        # inserendo i dati dove devono essere
        # e valutare il codice di ritorno

        # poi devo aggiornare la chat?
        

    def Leggi(self, idMsg):
        
        # Leggo il messaggio idMsg dal backend
        pass
    