#  Prova mia

tel = str(input('Inserire un numero di telefono lungo 10 cifre: '))

while len(tel) != 10:  # "!=" è il carattere per dire diverso 
    print('Il numero inserito non è lungo 10 caratteri!')
    tel = str(input('Inserire un numero di telefono lungo 10 cifre: '))

else:
    print(f'({tel[0:3]}) {tel[3:6]}-{tel[6:]}')