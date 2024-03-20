numero_tel = '4523453563' #(452) ...

if len(numero_tel) !=10:
 print('il numero inserito non è lungo 10 cifre!')
 exit()

#parte_1 = '452'
#parte_2 = '345'
#parte_3 = '3563'

parte_1 = numero_tel[0:3]
parte_2 = numero_tel[3:6]
parte_3 = numero_tel[6:]

#res_num = '(' * parte_1 +')' + ' ' + part_2 + '-' +
res_num = f'({parte_1}) {parte_2}-{parte_3}'

print(res_num)