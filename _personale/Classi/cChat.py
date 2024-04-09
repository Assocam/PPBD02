import sys

sys.path.append("\\\\CORSI\\DATI\\Documenti\\Corsisti\\PPBD02-14\\Desktop\\lavoro Marco PPBD02-14")

from Classi.cMessaggio import Messaggio
import json
import uuid
import datetime
import os

class Chat:

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

        self.ChatList.append(m)

    def Importa(self, nomeFile):

        #apriamo e leggiamo il file
        with open(nomeFile, 'r', encoding = 'utf-8') as fr:
            datiJSON = fr.read()

        dizDati = json.loads(datiJSON)

        self.Svuota()

        self.ChatList = []

        chiavi = dizDati.keys()

        for k in chiavi:
            msg = dizDati[k]

            m = Messaggio

            dizMessaggio = dizDati[k]

            m.Mittente = msg['Mittente'] = m.Mittente
            m.Destinatario = msg['Destinatario'] = m.Destinatario
            m.Testo = msg['Testo'] = m.Testo
            m.DTMessaggio = msg['DTMessaggio'] = m.DTMessaggio.isoformat()
            m.DTInvio = msg['DTInvio'] = m.DTInvio.isoformat()
            m.Status = msg['Status'] = m.Status
            m.Chiave = msg['Chiave'] = m.Chiave

            self.Aggiungi(m)

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
            dizExport[contaMessaggi]['DTMessaggio'] = m.DTMessaggio.isoformat()
            dizExport[contaMessaggi]['DTInvio'] = m.DTInvio.isoformat()
            dizExport[contaMessaggi]['Status'] = m.Status
            dizExport[contaMessaggi]['Chiave'] = m.Chiave

        dizJSON = json.dumps(dizExport)
        nomeChiave = str(uuid.uuid4())
        DTBackup = str(datetime.datetime.now().isoformat())

        nomefile = f'BackupChat_{nomeChiave}_{DTBackup}.chat'
        #nomeCompleto = os.path.abspath(nomefile)
        nomefile = nomefile[:57]
        print(os.path.abspath(nomefile))
        #adesso bisogna scrivere
        with open(nomefile, 'w') as fw:
            fw.write(dizJSON)



        









            
















