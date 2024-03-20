tel = str(4155551212)

if len(tel) != 10:  # "!=" è il carattere per dire diverso 
    print('Il numero inserito non è lungo 10 caratteri!')
    exit()

print(f'({tel[0:3]}) {tel[3:6]}-{tel[6:]}')