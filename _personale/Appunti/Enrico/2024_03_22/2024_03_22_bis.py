# Voglio aprire il file, leggerlo
# e scrivere le righe che non siano vuote e 
# che non comincino col simbolo #

import os                # libreria di sistema operativo

filename = os.path.abspath('_personale\Appunti\Enrico\2024_03_22\dati.txt')
print(filename)


fr = open('_personale\Appunti\Enrico\\2024_03_22\dati.txt', 'r', encoding = 'utf-8')    # "fr" è l'apertura di quel file, 'r è read'
dati = fr.read()                                  # leggi il file
fr.close()                                        # chiudilo

# with open(filename, 'r', encoding='utf-8') as fr:           # Questo è uguale alle righe 11-13, ma chiude il file in automatico
#     dati = fr.read()                                        # un file aperto non è cosa buona

righe = dati.split('\n')                          # 

for r in righe:

    if len(r) == 0:           # se la lunghezza della riga è uguale a zero, ovvero RIGA VUOTA
        pass                  # non fare niente
    elif r[0] == '#':         # se la riga inizia con #
        pass                  # non fare niente
    else:                     # altrimenti
        print(r)              # stampa la riga
