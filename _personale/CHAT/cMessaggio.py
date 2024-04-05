import datetime
import requests
import uuid



class messaggio:

    def __init__(self, mitt, dest, msg):

        chiaveMSG = str(uuid.uuid4)

        self.Mittente = mitt
        self.Destinatario = dest                 # destinatario in una lista
        self.Testo = msg
        self.DTMessaggio = datetime.datetime.now()
        self.DTInvio = datetime.datetime.now()
        self.Status = 'BOZZA'
        self.Chiave = chiaveMSG

    def Status(self, status):

        self.Status = status

    def Invia(self, destinatario, testo):
        
        #
        # self.Destinatario = destinatario                         # procedura invio al BackEnd
        # self.Testo = testo
        self.DTInvio = datetime.datetime.now()
        self.Status = 'INVIATO'

    def Leggi(self, idMsg):

        # leggo il messaggio idMsg dal backend               
        pass







