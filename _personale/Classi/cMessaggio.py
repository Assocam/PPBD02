import datetime
import uuid
import requests         # Per richiamare un indirizzo Metodi o Verbi:
                        # Leggere: GET
                        # Scrivere: PUT
                        # Modificare: POST
                        # Cancellare: DELETE

class Messaggio:

    def __init__(self, mitt, dest, msg):

        chiaveMSG = str(uuid.uuid4)

        self.Mittente = mitt
        self.Destinatario = dest                 # destinatario in una lista
        self.Testo = msg
        self.DTMessaggio = datetime.datetime.now()
        self.DTInvio = datetime.datetime.now()
        self.Status = 'BOZZA'
        self.Chiave = chiaveMSG

    def __repr__(self):                                            # Metodo rappresentante
        msg = f'Da: {self.Mittente}, A: {self.Destinatario}'
        msg += f' Ti ha scritto: {self.Testo} \n'

        return msg

    def Status(self, status):

        self.Status = status

    def Invia(self):
        # Compilare il formato JSON scritto
        # Chiamare la API apposta
        # Con requests inserendo i dati dove devono essere
        # Valutare il codice di ritorno
        # Procedura di invio al Backup
        # self.Destinatario = destinatario                         # procedura invio al BackEnd
        # self.Testo = testo
        self.DTInvio = datetime.datetime.now()
        self.Status = 'INVIATO'

    def Leggi(self, idMsg):

        # leggo il messaggio idMsg dal backend               
        pass







