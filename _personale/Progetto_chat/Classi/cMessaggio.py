import datetime
import requests
import uuid        # Devo poter identificare univocamente il messaggio
import sqlite3
import json

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
    
    def __dictmsg__(self):

        self.dicmsg = {}
        self.dicmsg['mittente'] = self.Mittente
        self.dicmsg['destinatario'] = self.Destinatario
        self.dicmsg['testo'] = self.Testo

        
    '''
    def Test(self):

        # Scrive sul DataBase i messaggi
        pass
        conn = sqlite3.connect('chat.db')

        # DDL - Primary key significa che il dato deve essere univoco, non ci possono essere due nomi uguali
        # Autoincrement: creo un dato (1), il dato successivo registrato è automaticamente (2)

        SQL = """
            CREATE TABLE IF NOT EXISTS RUBRICA
            (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOME TEXT,
            COGNOME TEXT,
            USERNAME TEXT,
            PASSWORD TEXT
            )
        """

        cur = conn.cursor()          # il cursore è il ditino che indica le righe
        
        STATUS = 0

        try:                         # Try perché potrebbe esserci un errore
            cur.execute(SQL)
            conn.commit()
            STATUS = 200             # 200 -> è tutto ok

        except Exception as e:
            conn.rollback()
            print(e)
            STATUS = 500

        finally:
            cur.close()                  # devo chiudere altrimenti rimane una connessione....
            conn.close()                 # a un file aperto
        

        return STATUS


    def TestInsertUser(self,
                       username, password,
                       nome, cognome):

        
        conn = sqlite3.connect('chat.db')

        SQL = """
            INSERT INTO RUBRICA (
            NOME, COGNOME, USERNAME, PASSWORD
            ) VALUES (?,?,?,?)
        """

        cur = conn.cursor()

        STATUS = 0

        try: 
            cur.execute(SQL,(nome,
                             cognome,
                             username,
                             password))

            conn.commit()
            
            STATUS = 200

        except: 
            conn.rollback()

            STATUS = 500

        finally:
            
            cur.close()
            conn.close()


    def TestSelectUtenti(self):

        conn = sqlite3.connect('chat.db')
        
        cur = conn.cursor()

        SQL = """
                SELECT * FROM RUBRICA
        """

        cur.execute(SQL)
        righe = cur.fetchall()

        for r in righe:
            print(r)

        cur.close()
        conn.close()
    '''

    def Invia(self):

        self.DTInvio = datetime.datetime.now()
        self.Status = 'INVIATO'

        # Tutta la procedura per mandare al mio backend i dati:
        # Compilare il formato JSON adatto
        # Vedi in documentazione, 
        # Chiamare la API apposita con request
        # inserendo i dati dove devono essere
        # e valutare il codice di ritorno

        self.__dictmsg__()                        # Lancio il metodo
        dJson = json.dumps(self.dicmsg)

        response = requests.put('http://127.0.0.1:80/scriviMsg', json = dJson)

        testo = response.text
        codice = response.status_code  # Il codice di errore

        print(testo, codice)

        # poi devo aggiornare la chat?
        

    def Leggi(self, idMsg):
        
        # Leggo il messaggio idMsg dal backend
        pass

