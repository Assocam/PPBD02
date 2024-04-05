
# <------------------------------------------------------RIPASSONE------------------------------------------------------>
# <------------------------------------------------------RIPASSONE------------------------------------------------------>
# <------------------------------------------------------RIPASSONE------------------------------------------------------>
# <------------------------------------------------------RIPASSONE------------------------------------------------------>

# A) STRUTTURA TUPLA: (a, b, c, ...)
# B) STRUTTURA LISTA: [a, b, c, ...]
# C) STRUTTURA DIZIONARIO: d = {'chiave': valore, 'altra chiave': valore}

# D) COSTRUTTI IF:    <----------------------------

# if <condizione>:
#     codice da eseguire se la condizione è vera

# if <condizione>:
#     codice
# else:
#     codice

# if <condizione>:
#     codice
# elif <altra condizione>:
#     codice
# elif <altra condizione>:
#     codice

# E) CICLI FOR:    <----------------------------

# for (cosa itero) in (cosa devo iterare)
# for j in range(5) -->                          il range 5 conta da 0 a 4 --> [0;5[
#                                                il range posso indicarlo come range(5,2) lo fa ogni due,
#                                                range (10,20,3) cambio intervallo e lo faccio ogni 3

# lista = [3, 5, 7, 11, 2, 44]
# for elemento in lista:
#     <codice>

# F) CICLI WHILE:    <----------------------------

# while <condizione>:
#     <codice>

# posso farlo andare avanti all'infinito in loop dando while True
# per farlo uscire dal loop posso usare:
# 1) "Break", esco dall'istruzione - ESCO DAL CICLO
# 2) "Continue", riporta l'attenzione all'inizio del ciclo - RICOMINCIA IL CICLO

# G) WITH:    <----------------------------

# 1) fr = open('file.csv, 'r', encoding = 'utf-8)              r è in lettura, utf8 è la codifica, tipo se ci sono accenti
# 2) dati = fr.read()
# 3) fr.close                                                  una volta letti i dati chiudo il file, SEMPRE

# da 1 a 2 o da 2 a 3 può andare qualcosa storto, quindi ottengo errore, magari il file rimane aperto e
# rimane un puntatore che punta a un file che non mi serve più, quindi posso scrivere:

# with open('file.csv', 'r', encoding = 'utf-8') as fr         apro il file e lo nomino fr, una volta fatto chiude il file
# dati = fr.read()

# <------------------------------------------------------------------------------------------------------------------------------->

# In alcuni linguaggi devo dichiarare che tipo è la variabile, in python no
# int a
# a = 10

# python è un linguaggio posizionale, quindi importa molto dove scrivo le istruzioni:

# for x in range(4):
#     print(x)
#     y = x**
# print(y)   ------------->   questa è fuori dal ciclo for, quindi la stamperà solo una volta,
#                             se voglio ottenere la stampa ogni volta devo metterlo dentro il ciclo
#                             ovvero:
# for x in range(4):
#     print(x)
#     y = x**
#     print(y)

# <------------------------------------------------------------------------------------------------------------------------------->

# H) FUNZIONI (DEF):    <----------------------------

# def quadrato(lato)
#     perimetro = lato * 4
#     area = lato*lato
#     return perimetro, area

# Posso scrivere molte funzioni e salvare questo file come "funzioni.py" e poi posso utilizzarlo:

# from funzioni import quadrato (la funzione "quadrato" che ho definito prima)
# (p, a) = quadrato(5) = (20, 25)

# <------------------------------------------------------------------------------------------------------------------------------->

# I) PROGRAMMAZIONE A OGGETTI (OOP - Object Oriented Programming) E ISTANZE:    <----------------------------
#
# classe --> progetto dell'automobile
# istanza --> automobile fatta secondo il progetto
 
# 4 pilastri: ereditarietà, polimorfismo, incapsulamento, astrazione, i primi due in python ok

# quando si parla di metodi e funzioni si parla di cose che stanno dentro ad oggetti o cose che non stanno dentro ad oggetti
# quando definisco una classe, ovvero un progetto di qualcosa, in python è relativamente semplice.

# faccio una classe di animali:
# class Animale:
# def verso(self): 
#     return "bau"

# ani = animale   ----> sto creando una istanza per animale
# v = ani.verso()

# <------------------------------------------------------------------------------------------------------------------------------->

# J) FRONT END - BACK END 

# Per farli comunicare uso IPC - Inter Process Communication (API Restful, con dati JSON)
# API Restful è un meccanismo che serve per far comunicare due processi diversi (FE/BE)
# devono comunicare anche quando FE e BE sono fisicamente lontani, la cosa in comune è internet
# quindi si usa protocollo HTTP

# QUINDI          ---------------------->  API RESTFUL = HTTP + JSON  <---------------------- 


# <------------------------------------------------------------------------------------------------------------------------------->

