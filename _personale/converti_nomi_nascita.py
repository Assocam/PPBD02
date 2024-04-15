dati = {}
with open('C:\\Users\\Gigi3\\Desktop\\PythonP\\PPBD02\\files_esercizi\\nomi_data_nascita.txt', 'r', encoding='utf-8') as  f:
    file = f
    for line in file:
        line = line.strip('\n').split(':')
        dati[line[0]] = (line[1])
dict_eta = {}

for e in dati:
    eta = 2024 - int(dati[e])
    dict_eta[e] = eta

with open('C:\\Users\\Gigi3\\Desktop\\PythonP\\PPBD02\\_personale\\outputs\\nomi_eta.csv', 'w+', encoding='utf-8') as f:
    file = f
    file.write('Nome, Età\n')
    for e in dict_eta:
        file.write(e)
        file.write(',')
        file.write(str(dict_eta[e]))
        file.write('\n')




