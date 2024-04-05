from Classi.cMessaggio import Messaggio
import json           # Per esportare il backup
import uuid           # Per salvare i backup successivi e chiamarli in modo diverso per non sovrascrivere
import datetime       # Per scrivere la data del backup
import os

class Chat:

    def __init__(self, owner):

        self.Owner = owner
        self.ChatList = []

    def TrovaUtente(self, utente):
        
        ChatUtente = []

        for u in self.ChatList:
            
            if (u.Destinatario == utente) or \
               (u.Mittente == utente):
                
                # Trovati i messaggi 
                ChatUtente.insert(u)

        return ChatUtente


    def Aggiorna(self, m:Messaggio):
        
        for msg in self.ChatList:
            if msg.Chiave == m.Chiave:
                # Trovato il messaggio
                msg.Status = m.Status

                # devo informare pure il BackEnd

                break


    def Svuota(self):
        
        for c in self.ChatList:

            # Chiamo il backEnd per
            # svuotare i messaggi
            pass                             # Sto solo richiamando il messaggio

        # dopo aver chiamato il backend,
        # svuoto la lista
        
        self.ChatList = []                   # Lo cancella e ritorna all'inizio del ciclo for

    def Aggiungi(self, m:Messaggio):         # Potevo scrivere (self, m), per ricordarmi che m è messaggio posso dire
#                                              che il tipo di parametro (m) è "Messaggio", usando i due punti
#                                              se scrivo "m." mi fa vedere le proprietà e i metodi associati alla classe, 
#                                              altrimenti dovrei ricordarmeli a memoria. Dicendogli che è un messaggio mi
#                                              appaiono i metodi: Testo, Status, Mittente, tutti dentro la classe Messaggio
#                                              che ho creato. Ha funzione mnemonica per me.

        # Chiamo il back end e gli dico
        # di inserire il messaggio
        # poi aggiorno la lista di messaggi della chat

        self.ChatList.insert(m)              # Aggiungo il messaggio alla lista di messaggi 

    
    def Importa(self, nomeFile):
        
        # Apriamo e leggiamo i file
        with open(nomeFile, 'r', encoding = 'utf-8') as fr:
            datiJSON = fr.read()

        dizDati = json.loads(datiJSON)

        self.ChatList = []    # Intanto la lista è vuota

        chiavi = dizDati.keys()   # Le chiavi di un dizionario di dizionari sono dizionari
        
        for k in chiavi:

            dizMessaggio = dizDati[k]

            msg = Messaggio('', '', '')
            msg.Chiave = dizMessaggio['Chiave']
            msg.Destinatario = dizMessaggio['Destinatario']
            #msg.DTInvio = 
            # SONO ARRIVATO QUI <---------------------------------------------------------------------------------------------


    def Esporta(self, msgList):

        # Esportiamo in formato JSON.
        # Mi serve un dizionario, anzi
        # anzi, un dizionario di dizionari.

        contaMessaggi = 0                     # Lo usiamo come chiave
        dizExport = {}

        for m in msgList:
            contaMessaggi += 1

            dizExport[contaMessaggi] = {}

            dizExport[contaMessaggi]['Mittente'] = m.Mittente              # dizExport[indice][chiave] = associa
            dizExport[contaMessaggi]['Destinatario'] = m.Destinatario
            dizExport[contaMessaggi]['Testo'] = m.Testo
            dizExport[contaMessaggi]['DTMessaggio'] = m.DTMessaggio
            dizExport[contaMessaggi]['DTInvio'] = m.DTInvio
            dizExport[contaMessaggi]['Status'] = m.Status
            dizExport[contaMessaggi]['Chiave'] = m.Chiave
            
            # Questo ciclo for confeziona il dizionario


        dizJSON = json.dumps(dizExport)    # JSONIZZIAMO IL FILE
        nomeChiave = str(uuid.uuid4())
        DTBackup = str(datetime.date.isoformat())

        nomeFile = f'Backup Chat_{nomeChiave}_{DTBackup}.chat'
        nomeCompleto = os.path.abspath(nomeFile)
        
        # Adesso lo devo scrivere
        with open(nomeCompleto, 'w') as fw:
            fw.write(dizJSON)

        

