#
#-- Main()
ricetta_orig = "Oliva\t, pepe,cappero ,\n detersivo,\t \n cappero, peperone, acciuga ,oliva , pepe\t,\t cappero , \noliva,pasta\n"
ricetta_finale = []
lista_spesa = set()
oliva_count = 0
pepe_count = 0
cappero_count = 0

stringa = ricetta_orig.replace("\t", ' ')  
stringa = stringa.replace("\n", ' ')
stringa = stringa.split(',')

for n in stringa:
    n = n.strip()
    ricetta_finale.append(n)
    if n.lower() == 'oliva':
        oliva_count += 1
    elif n.lower() == 'pepe':
        pepe_count += 1
    elif n.lower() == 'cappero':
        cappero_count += 1
    else:
        pass

for n in ricetta_finale:
    
    if ricetta_finale.count(n) > 1:
        lista_spesa.add((ricetta_finale.count(n), n))


print(f' Ricetta finale:\n{ricetta_finale}')
print(f'Lista della spesa:\n{lista_spesa}')
print('Servono:')
for n in lista_spesa:
    print(n)

print(f'Servono:\n'
      f'{oliva_count} Olive\n'
      f'{pepe_count} Pepe\n'
      f'{cappero_count} Capperi\n')