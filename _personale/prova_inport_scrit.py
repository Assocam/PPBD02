from converti_nomi_nascita_univeral import converti_file 
import os 

# ottiene il persorso assoluto dello script corente
script_path = os.path.abspath(__file__)

# Ottiene la directory in cui risiede lo script
script_dir = os.path.dirname(script_path)

# Construisce un percorso assoluto al file di input
input_path = os.path.join(script_dir, 'input.txt')
output_path = os.path.join(script_dir, 'output.csv')


converti_file(input_path,output_path)