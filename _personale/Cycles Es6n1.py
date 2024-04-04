# Cycles Es6n1

def get_input():
    inputs = []
    somma = 0
    count_pari = 0
    count_dispari = 0

    while True:
        question = input("Inserire un nuovo valore: ")
        if question.isdigit():
            question = int (question)
            somma += question
            print (f'somma parziale: {somma}')
            inputs.append(question)
            if question % 2 == 0:
                count_pari += 1
            else:
                count_dispari += 1
        elif question == '':
            return inputs, somma, count_pari, count_dispari
        else:
            print (f'Il valore inserito non è corretto! {question}')
#-- Main()

lista, somma, n_pari, n_dispari = get_input()

print(f'La somma totale è: {somma}')
print(f'Il valore massimo è {max(lista)}\n'
       f'Il valore minimo è {min(lista)}')


print(f'N. valori pari: {n_pari}\n'
      f'N. valori dispari: {n_dispari}\n'
      f'La lista completa: {lista}')