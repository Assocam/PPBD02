def request_voto():
    while True:
        voto_alpha = input ("inserire un voto: ")
        if len (voto_alpha) < 3:
            if len(voto_alpha) == 1  or voto_alpha[1] in ['-', '+']:
                voto_alpha = voto_alpha.lower()
                if voto_alpha[0] in ['a', 'b', 'c', 'd', 'f']:
                    return voto_alpha
                else:
                    print (f'Il carattere "{voto_alpha[0]}" non è un voto!')
                    continue
            else:
                print (f"secondo valore non corretto: {voto_alpha}!")
                continue
        else:
            print (f"valore troppo lungo: {voto_alpha}!")
            continue
#--
def put_Value(x):
    if x[0] == 'a':
        value = 4.0
        return value
    elif x[0] == 'b':
        value = 3.0
        return value
    elif x[0] == 'c':
        value = 2.0
        return value
    elif x[0] == 'd':
        value = 1.0
        return value
    elif x[0] == 'f':
        value = 0.0
        return value
#-- 
def second_value(x, y):
    if x == '-':
        y -= 0.3
        if y == -0.3:
            y += 0.3
        return y
    elif x == '+':
        y += 0.3
        if y == 4.3:
            y -= 0.3
        return y
    else:
        return y
# Main()
voto_string = request_voto()
voto_digit = put_Value(voto_string)
if len (voto_string) > 1:
    voto_digit = second_value(voto_string[1], voto_digit) 

print (f'il voto {voto_string.upper()} è equivalente a {voto_digit}')


    