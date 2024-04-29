import csv
import json
import xml
from pprint import pprint
import os

# Recupero file path

file_path = os.path.abspath(__file__)
dir_name = os.path.dirname(file_path)
dir_name = os.path.dirname(dir_name)


# Dichiarazioni contatori
tot_comuni = 0
tot_abitanti = 0
quota = int(input("Inserisci il minimo di quota': "))

# Raccolta da file csv:
nome_dati_file = 'Sardegna_centri_urbani_per_abitante_e_altitudine_2014-01-13.csv'
dati_path = os.path.join(dir_name, 'files_esercizi', nome_dati_file)

with open(dati_path, 'r', encoding='latin-1') as fr:
    file_csv_reader = csv.DictReader(fr, delimiter=";")
    for linea in file_csv_reader:
        if int(linea['QUOTA LOCALITA\'']) > quota:
            tot_comuni += 1
            tot_abitanti += int(linea["ABITANTI LOCALITA'"])

# Risultato csv
print('Da file csv:')
print(f'N. centri urbani sopra i quota m s.l.m.: {format(tot_comuni, ",d")}')
print(f'N. Abitanti sopra i quota m s.l.m.: {format(tot_abitanti, ",d")}')

# Resetto le variabili
tot_comuni = 0
tot_abitanti = 0

# Prendo il path del file .json
nome_dati_file = 'Sardegna_centri_urbani_per_abitante_e_altitudine_2014-01-13.json'
dati_path = os.path.join(dir_name, 'files_esercizi', nome_dati_file)

# Raccolta da file JSON:
with open(dati_path, 'r', encoding='latin-1') as fr:
    dati_file = fr.read()
    file_json_reader = json.loads(dati_file)
    for dict_row in file_json_reader:
        if int(dict_row["QUOTA LOCALITA'"]) > quota:
            tot_comuni += 1
            tot_abitanti += int(dict_row["ABITANTI LOCALITA'"])

# Risultato json
print('Da file json:')
print(f'N. centri urbani sopra i quota m s.l.m.: {format(tot_comuni, ",d")}')
print(f'N. Abitanti sopra i quota m s.l.m.: {format(tot_abitanti, ",d")}')