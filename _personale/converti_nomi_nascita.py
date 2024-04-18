import sys
from datetime import date

args = sys.argv

anno_corrente = date.today().year
report = {}  #dizionario vuoto
input_path = args[1]
output_path = args[2]

with open (input_path, mode='r', encoding='utf-8') as file_testo:
    list_lines = file_testo.readlines()

for line in list_lines:
    lista_oggetti = line.split(':')
    nome = lista_oggetti[0].strip()
    anno = int(lista_oggetti[1].strip())
    eta = anno_corrente - anno
    
    if eta not in report: # se chiave è presente
        report[eta] = [nome]
    else:
        report[eta].append(nome)


with open(output_path, 'w', encoding= 'utf-8') as outputs_file:

    intestazione = 'Nome,Eta\n'
    outputs_file.write(intestazione)
    # per ciascuna eta
    for eta in report:
        for nome in report[eta]:
            riga = f'{nome},{eta}\n'
            outputs_file.write(riga)
        
