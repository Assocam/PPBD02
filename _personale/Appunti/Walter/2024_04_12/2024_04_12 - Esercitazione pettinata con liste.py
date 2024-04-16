# Esercitazione INF_PR_PY_E04
# Denominazione: Programma Pagella con le liste

# Definizione studente:
nome = input('Inserire il nome dello studente: ')
nome = nome.capitalize()
cognome = input('Inserire il cognome dello studente: ')
cognome = cognome.capitalize()
classe = input('Inserire la classe frequentata dallo studente: ')
classe = classe.upper()

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

    if conferma == '':
       print('Il campo non può essere vuoto, digitare sì o no e premere invio.')
       continue

    elif conferma[0].lower() == 's':
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

controllo = True

for mat in materie:
    if controllo == True:
        print(f'Inserisci i voti per {mat}.')
    else:
        print(f'Attenzione! Cambio materia: {mat}!')
    
    controllo = False
       
    voti_parziali = []

    for m in range (1,quanti_voti+1):
       voto = chiedi_voto(m, mat)
       voti_parziali.append(voto)

    voti.append(voti_parziali)

print()

# Richiesta conferma voti inseriti:

while True:
    print('I voti inseriti sono:\n')
    for idx, materia in enumerate(materie):
        print(f'{materia}: {voti[idx]}')

    conferma = input('\nVuoi confermare? Rispondere sì o no): ')

    if conferma == '':
        print('Il campo non può essere vuoto, rispondere sì o no.\n')
        continue

    elif conferma.lower() == 's':
        break

    elif conferma.lower() == 'n':
        voti = []
        for mat in materie:
            voti_parziali = []
            for m in range(1, quanti_voti + 1):
                voto = chiedi_voto(m, mat)
                voti_parziali.append(voto)
            voti.append(voti_parziali)
        continue

    else:
        print(f'Input non valido: {conferma}, rispondere sì o no.\n')
        continue


# Stampa output richiesto

print(f'Ecco la lista di voti inseriti per lo studente {nome} {cognome} della classe {classe}: \n')

for k in range (0,len(materie)):
    print(f'{materie[k]}: {voti[k]}')      # <----- CAPIRE COME MODIFICARE QUESTA COSA IN BASE AL NUMERO DI MATERIE

print()

print(f'La media dello studente {nome} {cognome} della classe {classe} in ogni materia è:\n')

for k in range (0,len(materie)):
    print(f'{materie[k]}: {sum(voti[k])/len(voti[k]):.2f}')


# Concateniamo la lista dei voti:
lista_globale = []

for sottolista in voti:
    lista_globale += sottolista

media_globale = sum(lista_globale)/len(lista_globale)

print()

print(f'La media globale dello studente {nome} {cognome} è: {round(media_globale)}\n')

print(f'Il voto più alto registrato è {max(lista_globale)}\n'
      f'Il voto più basso registrato è {min(lista_globale)}.')

# Verifica se si può associare il voto massimo e minimo alla materia