# Cicli
# while : va avanti finchè le funzioni sono TRUE  -   for : un ciclo che continua
# finchè non si interrompe con un "break" o se vuoi continuare a fargli ripetere il ciclo
# si fa "continue"
# costrutto with- primo caso fr = open('file.csv','r', encoding = 'utf.8')
# secondo caso DATI = fr.Read()
# terzo caso fr.close() - rimane aperto un file che non si chiude più
# usando with open('file.csv') as fr   -   rende atomica la soluzione
#             dati = fr.read()    -   così si può chiudere il file
# python è un linguaggio posizionale es:
#
# for x in range(4) - il ciclo prende solo questi  comandi identati
#     print(x)      -
#     y = x**       -
#
# print(y)           questo comando è fuori dal ciclo 
# 
# funzione def:
# def quadrato(lato)          
#    Per = lato * 4
#    area = lato * lato
#    Return lato 
# in un file pyton: from funzioni import quadrato
# P = 20   -   A = 25    quadrato(5) ci si preoccupa di come usare il quadrato
# -Definito questo si affronta la programmazione orientata agli oggetti
# cos'è un'oggetto esempio una classe e l'istanza è fisicamente l'automobile fatta
# secondo il progetto
# -rif ai 4 pilastri Linguaggi_py.txt
# ci sono anche ereditarietà multiple
# i singoli OP si chiamano "metodi" che stanno dentro gli oggetti
# quando si definisce una classe "progetto" in py
# es: class Animale:
#         def Verso(self):                    "self : se stesso"
#           Return "Bau"
# 
# # ani = animale   "si crea una classe del mondo animale"
# V = ani.Verso()         
# 
# -Termini moderni:     Front End   |   Back End
#                                  IPC
#                              API  |  Restful   
#                                con dati
#                                  Json
# scambio dati tra un processo e un altro
# protocollo HTTP per controllare internet su dati Json
# API Restful: serve a far comunicare i due fronti
#