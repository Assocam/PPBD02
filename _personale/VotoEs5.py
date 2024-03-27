def request_voto():
    while True:
        voto_alpha = input ("inserire un voto:")
        if len (voto_alpha) < 3:
            if voto_alpha[1] in ['-', '+', ' ']:
                x = voto_alpha.lower()[1]
                x in []
            else:
                print (f"secondo valore non corretto: {voto_alpha}")
                continue
        else:
            print (f"valore troppo lungo: {voto_alpha}")
            continue
#--
def put_Value(x):
    if x == 'a':
        value = 4.0
        return value
    elif x == 'b':
        value = 3.0
        return value
    elif x == 'c':
        value = 2.0
        return value
    elif x == 'd':
        value = 1.0
        return value
    elif x == 'f':
        value = 0.0
        return value
#-- 
def second_value(x, y):
    if x == '-':
        y -= 0.3
        return y
    elif x == '+':
        y += 0.3
        return y
    else:
        return y
# Main()
voto_string = request_voto()
voto_digit = put_Value(voto_string)
voto_digit = second_value(voto_string[1], float (voto_digit))



    