import sys
from datetime import date

args = sys.argv

anno_corrente = date.today().year
report = {}  
input_path = args[1]
output_path = args[2]


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

