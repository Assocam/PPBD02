from datetime import date

# Creazione funzione calcolo età

def calcolo_età(anno_di_nascita):
    
    anno_corrente = date.today().year
    return anno_corrente-int(anno_di_nascita)

# Creazione funzione di conversione file

def converti_file(input_file, output_file):
    
    # Provo ad aprire il file

    try:

        with open(input_file, mode = 'r', encoding = 'utf-8') as file_input:
            righe = file_input.readlines()


        intestazione = "Nome,Età\n"

        # Creo la lista vuota solita ma con dentro già l'intestazione
        report = [intestazione]

        for riga in righe:

            nome, anno_di_nascita = riga.split()
            nome = nome.replace(':', ',')   
            eta = calcolo_età(anno_di_nascita)          # uso la funzione di prima
            riga_formattata = f"{nome},{eta}\n"         # formatto i dati per come voglio
            report.append(riga_formattata)              # appendi la riga ottenuta all'intestazione,
#                                                       # quindi in pratica scrivi sotto

            with open(output_file, 'w') as file_output:
                file_output.writelines(report)

            print(f"Il file {output_file} è stato creato con successo.")



    # Se non riesco ad aprire il file stampo un messaggio di errore

    except Exception:
        print("Errore: il file di origine non è stato trovato.")

