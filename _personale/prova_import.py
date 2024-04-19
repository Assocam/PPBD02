import os
import tkinter
from converti_nomi_nascita_universal import *

script_path = os.path.abspath(__file__)

script_dir = os.path.dirname(script_path)
output_dir = os.path.join(script_dir, 'outputs')

input_path = os.path.join(script_dir, 'input.txt')
output_path_1 = os.path.join(output_dir, 'output.csv')
output_path_2 = os.path.join(script_dir, 'outputs', 'output.txt')

file = open_file(input_path)
dict_csv, dict_txt = conversion_data(file)
file_csv(output_path_1, dict_csv)
file_txt(output_path_2, dict_txt)