# Abbiamo fatto delle classi generiche per gestire i messaggi.
# Una parte che si chiama front end è quella che ci fa la videata con le informazioni che vogliamo inviare,
# non si deve preoccupare della validità dei dati. Fa due cose: raccolgo i dati e te li mando,
# oppure ricevo i dati e te li rappresento.
#                                                          ^
# <----------------------------------------------- IPC = API Restful ----------------------------------------------->
#                                                          v

# Nel back end ci si occupa delle varie ricerche ed elaborare i dati controllando sia tutto ok.
# Non rappresenta alcun dato.
 

# API, contiene qualche informazione:

# FASE DI RICHIESTA AL BACK-END:
# 1) Indirizzo da chiamare, faccio una richiesta (request)
# 2) Ci sono quattro metodi, o verbi -> Leggere (Get), Scrivere (Put), Modificare (Post), Cancellare (Delete)
# 3) Passare dei dati tramite JSON, quindi devo preparare i dati
# 
# FASE DI RISPOSTA DEL BACK-END: 
# La risposrta viene fatta tramite HTTP e API restful:
#  
# 1) Dati: HTML (sito internet), oppure JSON, XML, ...  
# 2) Devo rispondere con un CODICE DI RITORNO, OVVERO UN CODICE DI ERRORE HTML:

#    200 - Tutto ok           <---- Importante
#    404 - Non trovato        <---- Importante
#    403 - Proibito 
#    405 - Metodo sbagliato (tipo se non uso Get)
#    500 - Errore del server  <---- Importante


# <------------------------------------------------------ 10/04/2024 ------------------------------------------------------>

# Quale database usare?

# Ogni database è diverso, alcuni fanno cose che altri non riescono a fare, tipo usare il modulo datetime.
# Useremo SQL lite, fare attenzione alla differenza di "dialetti" tra i vari database che si possono usare.
# C'è quindi un repository di dati a cui accede il back end e che il front end non conosce.
# Dobbiamo costruirlo.

# Linguaggio SQL -> DDL (data definition language), DML (data manipulation language):

# DML, 4 verbi -> Select, Insert, Update, Delete
# DDL, 4 verbi -> Create (crea), Alter (altera), Drop (cancella), posso farlo su una tabella, sui dati, ecc...

# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 