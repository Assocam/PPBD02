import sys
sys.path.append("C:\\Users\\lucas\\Desktop\\Python - Scuola Camerana\\PPBD02\\_personale\\Progetto_chat")


#C:\\Users\\lucas\\Desktop\\Python - Scuola Camerana\\PPBD02\\_personale\\Progetto_chat\\Classi\\cChat.py
#C:\\Users\\lucas\\Desktop\\Python - Scuola Camerana\\PPBD02\\_personale\\Progetto_chat\\Classi\\cMessaggio.py

from Classi.cChat import Chat
from Classi.cMessaggio import Messaggio

# Voglio impostare un messaggio e inizializzare la chat

chat = Chat(1)  # Dobbiamo dargli un proprietario, per il momento 1 va bene
msg = Messaggio(2, 3, 'Ti ho inviato un msg')
chat.Aggiungi(msg)
msg = Messaggio(2, 3, 'Ti ho risposto al msg')
chat.Aggiungi(msg)
msg = Messaggio(2, 3, 'Nuovo messaggio')
chat.Aggiungi(msg)
msg = Messaggio(2, 3, "Casomai non l'avessi capito")
chat.Aggiungi(msg)
msg = Messaggio(2, 3, 'E te lo dico ancora una volta')
chat.Aggiungi(msg)

msg.Invia() # Lo invia al Back-End!!!!!

chat.Esporta()

print(chat.ChatList)


# Ora provo il DB

# msg.Test()  # Costruisce il DB

# for x in range(5):
#     msg.TestInsertUser('enr', 'ter', 'Enrico', f'Terzolo {x}')

# msg.TestSelectUtenti()