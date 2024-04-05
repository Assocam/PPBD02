from Classi.cMessaggio import Messaggio
import json
import uuid
import datetime
import os

class chat:

    def __init__(self, owner):

        self.Owner = owner
        self.ChatList = []

    def Aggiorna(self, m:Messaggio):

        for msg in self.ChatList:
            if msg.Chiave == m.Chiave:
                # Trovato
                msg.Status = m.Status

                # si deve informare pure il backend

    def Svuota(self):
        
        for c in self.ChatList:

            #chiamo il backend per svuotare il messaggio

            pass

        #dopo aver chiamato il beckend si svuota la lista

        self.ChatList = [] 

    def TrovaUtente(self, utente):

        ChatUtente = []

        for u in self.ChatList:

            if (u.Destinatario == utente) or \
               (u.Mittente == utente):
                
                #Trovato
                ChatUtente.insert(u)

        return ChatUtente


   

    def Aggiungi(self, m:Messaggio):

        #chiamo il backend e gli dico di inserire il messaggio
        #poi aggiorno la lista messaggi della chat

        self.ChatList.insert(m)

    def Importa(self, nomeFile):

        #apriamo e leggiamo il file
        with open(nomeFile, 'r', encoding = 'utf-8') as fr:
            datiJSON = fr.read()

        dizDati = json.loads(datiJSON)

        self.ChatList = []

        chiavi = dizDati.keys()

        for k in chiavi:

            dizMessaggio = dizDati[k]

            msg = Messaggio('','','')
            msg.Chiave = dizMessaggio['Chiave']
            msg.Destinatario = dizMessaggio['Destinatario']
            msg.DTInvio = dizMessaggio['DTInvio']
            # SONO ARRIVATO QUI

    def Esporta(self, msgList):

        # esportiamo in formato JSON quindi serve un dizionario
        # un dizionario di dizionari

        contaMessaggi = 0                   # si usa come chiave
        dizExport = {}

        for m in self.ChatList:
            contaMessaggi +=1

            dizExport[contaMessaggi] = {}

            dizExport[contaMessaggi]['Mittente'] = m.Mittente
            dizExport[contaMessaggi]['Destinatario'] = m.Destinatario
            dizExport[contaMessaggi]['Testo'] = m.Testo
            dizExport[contaMessaggi]['DTMessaggio'] = m.DTMessaggio
            dizExport[contaMessaggi]['DTInvio'] = m.DTInvio
            dizExport[contaMessaggi]['Status'] = m.Status
            dizExport[contaMessaggi]['Chiave'] = m.Chiave


        dizJSON = json.dumps(dizExport)
        nomeChiave = str(uuid.uuid4())
        DTBackup = str(datetime.date.isoformat())

        nomefile = f'BackupChat_{nomeChiave}_'
        nomeCompleto = os.path.abspath(nomefile)

        #adesso bisogna scrivere
        with open(nomeCompleto, 'w') as fw:
            fw.write(dizJSON)








            
















