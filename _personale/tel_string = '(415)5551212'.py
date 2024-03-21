tel_string = '(415)5551212'
pref = tel_string [0:5]
print(pref)
part1 = tel_string [5:8]
part2 = tel_string [8:]

print (pref+' '+part1+'-'+part2)

num_tel = '0123456789'

if len(num_tel) != 10:
     print ('il numero inserito non è lungo 10 cifre!')
     exit()
parte_1 = num_tel [0:3]
parte_2 = num_tel [3:6]
parte_3 = num_tel [6:]

res_num = f'({parte_1}) {parte_2}-{parte_3}'

print(res_num)
