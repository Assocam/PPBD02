number = input ("Inserire un numero a 10 cifre:")

number = str(number)
if len(number) != 10:
    print ("Il numero non è lungo 10 cifre!")
    exit()

first_part = number[:3]
second_part = number [3:6]
third_part = number [6:]
print (f'({first_part}) {second_part}-{third_part}')