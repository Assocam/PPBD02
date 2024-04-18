# Esercitazione INF_PR_PY_E04
# Denominazione: Programma Pagella con le liste

def input_non_vuoto(dato):
    while True:
        valore = input(f'Inserire il {dato} dellə studentə: ')
        if valore:
            return valore.capitalize()
        else:
            print(f'Il campo {dato} non può essere vuoto.')


# Definizione studente:
nome = input_non_vuoto('nome')
cognome = input_non_vuoto('cognome')

while True:
    classe = input('Inserire la classe frequentata dallə studentə: ')
    if classe:
        classe = classe.upper()
        break
    else:
        print('Il campo classe non può essere vuoto.')

# Creazione della lista materie

materie = []

def chiedi_materie():
   
    while True:
        numero_materia = len(materie) + 1
        nome_materia = input(f'Inserire il nome della materia {numero_materia} (oppure premere invio per terminare): ')
        if nome_materia:
           nome_materia = nome_materia.capitalize()
           materie.append(nome_materia)
           continue
        else:
           break

chiedi_materie()

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
        chiedi_materie() 
   
    else:
       print('Input non valido, rispondere sì o no.')
       continue
    
voti = []

# <------------------------------------------------------------------------------------------------------------------------------->

# Definizione della funzione chiedi numero

voto_massimo = input('Inserire il voto massimo della base di valutazione adottata (esempio: 10, 30, 100): ')

# prossima volta meglio chiedi_voto(num_voto, materia)
def chiedi_voto(m, mat):  # vanno messi due argomenti, quelli che metto nella f string dell'input 
    
    while True:

        voto = input(f'Inserire il voto {m} di {mat}: ')
        
        try:
            voto = int(voto)
            if 0 <= voto <= int(voto_massimo):
                pass
            elif voto < 0 or voto > int(voto_massimo):
                print(f'Il voto inserito non è valido: "{voto}". Il voto deve essere compreso tra 0 e {voto_massimo}')
                continue
        
        except Exception:
            print(f'Input non valido: "{voto}". Inserire un numero compreso tra 0 e {voto_massimo}')
            continue

        return voto


# <------------------------------------------------------------------------------------------------------------------------------->

# Richiesta numero voti 

while True:

    quanti_voti = input('Indicare quanti voti vuoi inserire per materia: ')

    try:
        quanti_voti = int(quanti_voti)
        break

    except Exception:
        print(f'Input non valido: "{quanti_voti}". Inserire un valore numerico intero.')


print(f'Pagelle: inserire {quanti_voti} voti per materia in {voto_massimo[0:(len(voto_massimo))]}-ESIMI - Voto tra 1 e {voto_massimo}.')

controllo = True

# Inserimento dei voti

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

print(f'Ecco la lista di voti inseriti per lə studentə {nome} {cognome} della classe {classe}: \n')

for k in range (0,len(materie)):
    print(f'{materie[k]}: {voti[k]}')

print()

print(f'La media dellə studentə {nome} {cognome} della classe {classe} in ogni materia è:\n')

for k in range (0,len(materie)):
    print(f'{materie[k]}: {sum(voti[k])/len(voti[k]):.2f}/{voto_massimo}')


# Concateniamo la lista dei voti:
lista_globale = []

for sottolista in voti:
    lista_globale += sottolista

media_globale = sum(lista_globale)/len(lista_globale)

print()

print(f'La media globale dellə studentə {nome} {cognome} è: {round(media_globale)}\n')

print(f'Il voto più alto registrato è {max(lista_globale)}/{voto_massimo}\n'
      f'Il voto più basso registrato è {min(lista_globale)}/{voto_massimo}.')

