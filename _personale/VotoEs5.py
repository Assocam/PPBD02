def request_voto():
    while True:
        voto_alpha = input("inserire un voto: ")
        if len(voto_alpha) < 3:
            if len(voto_alpha) == 1 or voto_alpha[1] in ['-', '+']:
                voto_alpha = voto_alpha.lower()
                if voto_alpha[0] in ['a', 'b', 'c', 'd', 'f']:
                    if voto_alpha in ('a+', 'f+', 'f-'): # by putting this the extra if in second_value() is useless
                        voto_alpha = voto_alpha[0]       # ...
                    return voto_alpha
                else:
                    print(f'Il carattere "{voto_alpha[0]}" non è un voto!')
                    continue # the continue is extra since it's all inside a while
            else:
                print(f"secondo valore non corretto: {voto_alpha}!")
                continue # the continue is extra since it's all inside a while
        else:
            print(f"valore troppo lungo: {voto_alpha}!")
            continue # the continue is extra since it's all inside a while
#--
def put_Value(voto):
    if voto == 'a':
        value = 4.0
    elif voto == 'b':
        value = 3.0
    elif voto == 'c':
        value = 2.0
    elif voto == 'd':
        value = 1.0
    elif voto == 'f':
        value = 0.0
    return value
#-- 
def second_value(segno, voto):
    if segno == '-':
        voto -= 0.3 
        if voto == -0.3: # If voto = -0.3(F-)
            voto += 0.3 # I bring it back to 0
    elif segno == '+': 
        voto += 0.3
        if voto in (4.3, 0.3): # If voto  =  4.3(A+)
            voto -= 0.3 # I bring it back to 4.0
    else:
        pass
    return voto
# Main()
voto_string = request_voto() # a, B, c+, D- ...
voto_digit = put_Value(voto_string[0]) # 4.0, 3.0 ...
if len(voto_string) > 1: #you could also write 'len(voto_string) =='
    voto_digit = second_value(voto_string[1], voto_digit) 

print(f'il voto {voto_string.upper()} è equivalente a {voto_digit}')


    