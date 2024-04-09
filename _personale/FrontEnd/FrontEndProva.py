# FrontEnd raccoglie informazioni che vogliamo inviare richiede msg al BeckEnd

import sys
sys.path.append("\\\\CORSI\\DATI\\Documenti\\Corsisti\\PPBD02-14\\Desktop\\lavoro Marco PPBD02-14")
from Classi.cChat import Chat
from Classi.cMessaggio import Messaggio

# Voglio impostare un messaggio e inizializzare la chat

chat = Chat(1)
msg = Messaggio(2, 3, 'Ti ho inviato un msg')
chat.Aggiungi(msg)
msg = Messaggio(3, 2, 'Ti ho risposto al msg')
chat.Aggiungi(msg)
msg = Messaggio(3, 2, 'Nuovo messaggio')
chat.Aggiungi(msg)
msg = Messaggio(3, 2, 'Caso mai non avessi risposto')
chat.Aggiungi(msg)
msg = Messaggio(3, 2, 'E te lo dico ancora una volta')
chat.Aggiungi(msg)

chat.Esporta(msg)

print(chat.ChatList)



