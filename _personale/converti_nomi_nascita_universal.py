# Imports
from datetime import date
import sys
import os

def check_files(input_file, output_file_csv, output_file_txt):
    dir_string_csv = os.path.dirname(output_file_csv)
    dir_string_txt = os.path.dirname(output_file_txt)
    
    if not os.path.exists(input_file):
        print("Il file di input non esiste!")
        return False
    else:
        pass

    if  not os.path.exists(dir_string_csv):
        print("La cartella del file '.csv' output non esiste")
        return False
    else:
        pass

    if  not os.path.exists(dir_string_txt):
        print("La cartella del file '.txt' output non esiste")
        return False
    else:
        pass
    return True
#-
def open_file(input_path): # Apertura dei file con i dati iniziali
    with open(input_path, mode='r', encoding='utf-8') as  f:
        file = f.readlines()
        for line in file:
            line = line.strip().split(':')
            dati[line[0]] = (line[1])
    return dati
#-
def conversion_data(dati): # conversione dei dati e creazione dei dizzionari.
    anno_corrente = date.today().year
    dict_eta = {} # dict = {nome, eta}
    dict_sub = {} # dict = {eta, nomi di persone con quell'età}

    for e in dati: 
        eta = anno_corrente - int(dati[e])
        dict_eta[e] = eta 
        if eta in dict_sub: 
            dict_sub[eta] = f'{dict_sub[eta]}, {e}'
        else:
            dict_sub[eta] = e
    return dict_eta, dict_sub
#-
def file_csv(output_path_csv, dict_eta): 
    # write of file txt, Eta, nomi delle persone con quell'età
    with open(output_path_csv, mode='+w', encoding='utf-8') as f:
        file = f
        output_file = []
        output_file.append('Nome, Età, Anno di nascita:\n')
        for e in sorted(dict_eta):
            output_file.append(f'{e}, {dict_eta[e]}, Nato/a il{dati[e]}\n')
        output_file.append('\n')
        file.writelines(output_file)
#-
def file_txt(output_path_txt, dict_sub): 
    # write of file csv, Nome, Età, Anno di nascita
    with open(output_path_txt, mode='+w', encoding='utf-8') as f:
        file = f
        file.write('Età: Persone\n')
        for e in sorted(dict_sub):
            file.writelines(f'{e}: {dict_sub[e]}\n')
        file.write('\n')
#-
#-Main()

if __name__ == '__main__': # to check if it was run as file or imported
    args = sys.argv # argomenti passati dal utente prima dell'esecuzione

    if len(args) == 4:
        input_path_dati = args [1]
        output_path_csv = args[2]
        output_path_txt = args[3]

        # input_path = filePath = './files_esercizi/nomi_data_nascita.txt' 
        # output_path1 = filePath = './_personale/outputs/nomi_eta.csv' 
        # output_path2 = filePath = './_personale/outputs/eta_nomi.txt' 

        if check_files(input_path_dati, output_path_csv, output_path_txt):
            dati = {} # dict = {nome, anno di nascita}
            dati = open_file(input_path_dati)
            dict_eta, dict_sub = conversion_data(dati)
            file_csv(output_path_csv, dict_eta)
            file_txt(output_path_txt, dict_sub)
        else:
            exit()

    elif len(args) == 1:
        print("Non hai passato i quattro parametri necessari." 
              "1 file di input e tre file di output.")

    elif len(args) == 2:
        print("Non hai passato il terzo e quarto parametro: File .csv + File .txt")

    elif len(args) == 3:
        print("Non hai passato il quarto parametro: File .txt")

    elif len(args) > 4:
        print("Hai passato troppi parametri")

    else:
        print("Hai inserito un numerto di parametri non coretto." 
              "Server indicare il file di input e il file di output.")
        exit()