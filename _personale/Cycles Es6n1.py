# Cycles Es6n1

def get_input():
    inputs = []
    somma = 0
    while True:
        q = input("Inserire un nuovo valore")
        if q.isdigit():
            q = int (q)
            somma += q
            inputs.append(q)
            continue
        elif q == '':
            return inputs, somma
        else:
            print (f'Il valore inserito non è corretto! {q}')
            continue
#-- Main()

