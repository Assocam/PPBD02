from datetime import date
import sys

# Creazione funzione calcolo età

def calcolo_età(anno_di_nascita):
    
    anno_corrente = date.today().year
    return anno_corrente-int(anno_di_nascita)

# Creazione funzione di conversione file

def converti_file(input_file, output_file):
    
    # Provo ad aprire il file

    try:

        #input_file = 'C:\\Users\\lucas\\Desktop\\Python - Scuola Camerana\\PPBD02\\_personale\\'

        with open(input_file, mode = 'r', encoding = 'utf-8') as file_input:
            righe = file_input.readlines()


        intestazione = "Nome,Età\n"

        # Creo la lista vuota solita ma con dentro già l'intestazione
        report = [intestazione]

        for riga in righe:

            nome, anno = riga.split()
            nome = nome.replace(':', '')   
            eta = calcolo_età(anno)                     # uso la funzione di prima
            riga_formattata = f"{nome},{eta}\n"         # formatto i dati per come voglio
            report.append(riga_formattata)              # appendi la riga ottenuta all'intestazione,
#                                                       # quindi in pratica scrivi sotto

        # Percorso del nuovo file
        #output_file = 'C:\\Users\\lucas\\Desktop\\Python - Scuola Camerana\\PPBD02\\files_esercizi'    

        with open(output_file, 'w', encoding = 'utf-8') as file_output:
            file_output.writelines(report)

        print(f"Il file {output_file} è stato creato con successo.")


    # Se non riesco ad aprire il file stampo un messaggio di errore

    except Exception:
        print("Errore: il file di origine non è stato trovato.")


# if __name__ == "__main__":
#     input_file = 'C:\\Users\\lucas\\Desktop\\Python - Scuola Camerana\\PPBD02\\_personale\\nomi_data_nascita.txt'
#     output_file = 'C:\\Users\\lucas\\Desktop\\Python - Scuola Camerana\\PPBD02\\files_esercizi\\nomi_eta_generato.csv'
#     converti_file(input_file, output_file)


if __name__ == "__main__":
    if len(sys.argv) > 3:      # sys.argv contiene ['script.py', 'arg1', 'arg2', 'arg3']
        print('Attenzione, la sintassi corretta è: "py converti_nomi_nascita.py file_sorgente.txt file_output.csv"')
    else:
        input_file = sys.argv[1]   # --> file_sorgente.txt
        output_file = sys.argv[2]  # --> file_output.csv
#       output_file = f'C:\\Users\\lucas\\Desktop\\Python - Scuola Camerana\\PPBD02\\files_esercizi\\{sys.argv[2]}'  # --> file_output.csv

        converti_file(input_file, output_file)
