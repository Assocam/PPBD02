import sys
import os
from datetime import date


def check_file(input_file, output_file):
    if not os.path.exists(input_file):
        print('ERRORE! Il file di input non esiste!')
        return False
    
    # ci serve verificare se la cartella esista, non il file che ancora non esiste
    dir_string = os.path.dirname(output_file)

    if not os.path.exists(dir_string):
        print('ERRORE! La cartella di output non esiste!')
        return False
    
    # else: non va scritto ma il senso è che se le condizioni sono soddisfatte
    # deve procedere, quindi scrivo solo return True
    return True


def converti_file(input_path, output_path):
  
    anno_corrente = date.today().year
    report = {}  

    with open(input_path, mode='r', encoding = 'utf-8') as file_testo:
            list_lines = file_testo.readlines()

    for line in list_lines:
        lista_oggetti = line.split(':')
        nome = lista_oggetti[0].strip()
        anno = int(lista_oggetti[1].strip())
        eta = anno_corrente - anno

        if eta in report: 
            report[eta].append(nome)
        else:
            report[eta] = [nome]


    with open(output_path, mode = 'w', encoding = 'utf-8') as output_file:
        intestazione = 'nome,eta\n'
        output_file.write(intestazione)
        for eta in report:
            for nome in report[eta]:
                riga = f'{nome},{eta}\n'
                output_file.write(riga)

#   return None   è il default se non scrivo nulla

# Controlla se il file è stato eseguito come script o no    
if __name__ == 'main':    # necessario per usare il codice in caso di importazione come script

    args = sys.argv


    # Condizioni: len = 1, 2, 3, > 3

    if len(args) == 3:
        input_path = args[1]
        output_path = args[2]

        if check_file(input_path, output_path):
            converti_file(input_path, output_path)
            path_assoluto = os.path.abspath(output_path)
            print(f'SUCCESSO! Il file è stato creato correttamente alla '
                f'posizione {path_assoluto}')


        
    elif len(args) == 1:
        print('Non hai passato i due parametri necessari: '
            'File di input e file di output.')
    elif len(args) == 2:
        print('Non hai passato il secondo parametro: '
            'File di input o file di output.')    
    else:
        print('Hai inserito troppi parametri. Ne servono solo due: '
            'File di input e file di output.')

