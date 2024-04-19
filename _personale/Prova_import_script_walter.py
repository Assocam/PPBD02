import os
from converti_nome_nascita_walter_universal import check_file, converti_file

# Indipendentemente da dove si trova l'utente durante l'esecuzione sul terminal
# voglio che comandi lo script:
# Sul terminal ho un percorso, mentre lo script è su un altro.
# Di solito per eseguire qualcosa devo spostarmi sulla cartella necessaria
# ed eseguire i comandi dopo "py" 
# Quindi quello che mi serve è:

#print(__file__)  # --> ti da il percorso del file dove stiamo scrivendo, ovvero
#                 #     questo file Prova_import_script_walter.py


# Ottiene il percorso assoluto dello script corrente
script_path = os.path.abspath(__file__)

# Ottiene la directory in cui risiede lo script
script_dir = os.path.dirname(script_path)

# Costruisce un percorso assoluto al file di input
input_path = os.path.join(script_dir, 'input.txt')
output_pathput_path = os.path.join(script_dir, 'output.txt')


input_path = './nomi_data_nascita.txt'
output_path = './output_walter_import.csv'

converti_file(input_path, output_path)
