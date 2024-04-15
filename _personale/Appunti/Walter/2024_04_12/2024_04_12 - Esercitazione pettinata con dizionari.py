# Esercitazione INF_PR_PY_E04
# Denominazione: Programma Pagella con le liste

# Definizione studente:
nome = input('Inserire il nome dello studente: ')
nome = nome.capitalize()
cognome = input('Inserire il cognome dello studente: ')
cognome = cognome.capitalize()
classe = input('Inserire la classe frequentata dallo studente: ')

# Creazione della lista materie

materie = []

while True:
    nome_materia = input('Inserire il nome della materia (oppure premere invio per terminare): ')
    if nome_materia:
       nome_materia = nome_materia.capitalize()
       materie.append(nome_materia)
       continue
    else:
       break

# Richiesta di conferma delle materie inserite

while True:
    conferma = input(f'Le materie inserite sono: {materie}. Vuoi confermare? (Sì/No): ')

    if conferma[0].lower() == 's':
        break
    
    elif conferma[0].lower() == 'n':
        materie = []
        
        while True:
         
            nome_materia = input('Inserire il nome della materia (oppure premere invio per terminare): ')
            if nome_materia:
               nome_materia = nome_materia.capitalize()
               materie.append(nome_materia)
               continue
            else:
               break
    
    else:
       print('Input non valido, rispondere sì o no.')
       continue
    
voti = []

# <------------------------------------------------------------------------------------------------------------------------------->

# Definizione della funzione chiedi numero

def chiedi_voto(m, mat):  # vanno messi due argomenti, quelli che metto nella f string dell'input
    
    while True:

        voto = input(f'Inserire il voto {m} di {mat}: ')
        
        try:
            voto = int(voto)
            if 0 <= voto <= 100:
                pass
            elif voto < 0 or voto > 100:
                print(f'Il voto inserito non è valido: "{voto}". Il voto deve essere compreso tra 0 e 100')
                continue
        
        except Exception:
            print(f'Input non valido: "{voto}". Inserire un numero compreso tra 0 e 100')
            continue

        return voto


# <------------------------------------------------------------------------------------------------------------------------------->

# Richiesta numero voti 

quanti_voti = input('Indicare quanti voti vuoi inserire per materia: ')
quanti_voti = int(quanti_voti)

print(f'Pagelle: inserire {quanti_voti} voti per materia in CENTESIMI - Voto tra 1 e 100.')

count = 0 

for mat in materie:
    if count == 0:
        print(f'Inserisci i voti per {mat}.')
    else:
        print(f'Attenzione! Cambio materia: {mat}!')
    
    count += 1
       
    voti_parziali = []

    for m in range (1,quanti_voti+1):
    #    voto = input(f'Inserire il voto {m} di {mat}: ')
    #    voto = int(voto)
       voto = chiedi_voto(m, mat)
       voti_parziali.append(voto)

    voti.append(voti_parziali)


# Richiesta conferma voti inseriti:

# while True:

#     for idx,materia in materie.enumerate():   # da un identificativo
#         print(f'I voti inseriti sono: \n'
#             f'{materia}: {voti[idx]}\n')

    
#     conferma = input('Vuoi confermare? (Sì/No): ')

#     if conferma[0].lower() == 's':
#         break
    
#     elif conferma[0].lower() == 'n':
#         voti = []
#         voti_parziali = []

#         count = 0 

#         for mat in materie:
#             if count == 0:
#                 print(f'Inserisci i voti per {mat}.')
#             else:
#                 print(f'Attenzione! Cambio materia: {mat}!')
            
#             count += 1
                
#             voti_parziali = []

#             for m in range (1,quanti_voti+1):
#                 #    voto = input(f'Inserire il voto {m} di {mat}: ')
#                 #    voto = int(voto)
#                 voto = chiedi_voto(m, mat)
#                 voti_parziali.append(voto)
            
#             voti.append(voti_parziali) 

#     else:
#        print('Input non valido, rispondere sì o no.')
#        continue


# Stampa output richiesto

print(f'Ecco la lista di voti inseriti per lo studente {nome} {cognome} della classe {classe}: \n'
      f'{materie[0]}: {voti[0]}\n'
      f'{materie[1]}: {voti[1]}\n'
      f'{materie[2]}: {voti[2]}\n'                    # <----- SONO ARRIVATO QUI
      f'{materie[3]}: {voti[3]}')                     # <----- CAPIRE COME MODIFICARE QUESTA COSA IN BASE AL NUMERO DI MATERIE


media_matematica = sum(voti[0])/len(voti[0])
media_italiano = sum(voti[1])/len(voti[1])
media_inglese = sum(voti[2])/len(voti[2])
media_storia = sum(voti[3])/len(voti[3])

print(f'La media dello studente {nome} {cognome} della classe {classe} in ogni materia è:\n'
      f'Matematica: {media_matematica:.2f}\n'
      f'Italiano: {media_italiano:.2f}\n'
      f'Inglese: {media_inglese:.2f}\n'
      f'Storia: {media_storia:.2f}')

media_globale = (media_matematica + media_italiano + media_inglese + media_storia)/len(materie)

print(f'La media globale dello studente {nome} {cognome} è: {round(media_globale)}')

# Concateniamo la lista dei voti:
lista_globale = []

for sottolista in voti:
    lista_globale += sottolista

print(f'Il voto più alto registrato è {max(lista_globale)}\n'
      f'Il voto più basso registrato è {min(lista_globale)}.')