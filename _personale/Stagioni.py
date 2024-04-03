
risp_mese = False
risp_giorno = False

messaggio_input_mese = 'Inserire il numero del mese: '
messaggio2_mese = 'Inserire un numero compreso tra 1 e 12: '
messaggio3_mese = 'Ti ho detto di inserire un numero compreso tra 1 e 12: '

messaggio_input_giorno = 'Inserire il numero del giorno: '
messaggio2_giorno = 'Inserire un numero compreso tra 1 e 31: '
messaggio3_giorno = 'Ti ho detto di inserire un numero compreso tra 1 e 31: '


while True:                         # Fintantoché inserisco un numero valido fa break, ovvero va avanti, altrimenti mi ripropone di inserire un numero valido

    mese = int(input(messaggio_input_mese))

    if 0 < mese < 13:
        mese = mese                                  # Non è necessario togliere lo zero perché la conversione in int lo fa in automatico
        break            # Esci dal ciclo            # In questo modo avanza solo se il mese è corretto, altrimenti torna indietro (esce da questo ciclo if)
    else:
        if risp_mese is False:
            messaggio_input_mese = messaggio2_mese
            risp_mese = True
        else:
            messaggio_input_mese = messaggio3_mese


while True:

    giorno = int(input(messaggio_input_giorno))

    if 0 < giorno < 32:
        giorno = giorno
        break                                        # In questo modo avanza solo se il giorno è corretto, altrimenti torna indietro
    else:
        if risp_mese is False:
            messaggio_input_giorno = messaggio2_giorno
            risp_mese = True
        else:
            messaggio_input_giorno = messaggio3_giorno

if mese in (4, 5, 6):
    if mese % 3 == 0 and giorno <= 21 or mese in (4, 5):        # Avrei potuto scrivere anche "not (mese % 3)", in modo da farmi dare True
        stagione = 'Primavera'
    else:
        stagione = 'Estate'

elif mese in (7, 8, 9):
    if mese % 3 == 0 and giorno <= 21 or mese in (7, 8):
        stagione = 'Estate'
    else:
        stagione = 'Primavera'

elif mese in (10, 11, 12):
    if mese % 3 == 0 and giorno <= 21 or mese in (10, 11):
       stagione = 'Autunno'
    else:
       stagione = 'Inverno'

elif mese in (1, 2, 3):
    if mese % 3 == 0 and giorno <= 21 or mese in (1, 2):
       stagione = 'Inverno'
    else:
       stagione = 'Primavera'


print(f'Stagione =', stagione)

