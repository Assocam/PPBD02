# Cycles Es6n1

def get_input():
    inputs = []
    somma = 0
    while True:
        question = input("Inserire un nuovo valore: ")
        if question.isdigit():
            question = int (question)
            somma += question
            print (f'somma parziale: {somma}')
            inputs.append(question)
        elif question == '':
            return inputs, somma
        else:
            print (f'Il valore inserito non è corretto! {question}')
#-- Main()

lista, somma = get_input()

print(f'La somma totale è: {somma}')
print(f'Il valore massimo è {max(lista)}\n'
       f'Il valore minimo è {min(lista)}')
count_pari = 0
count_dispari = 0
for n in lista:
    if n % 2 == 0:
        count_pari += 1
    else:
        count_dispari += 1

print(f'N. valori pari: {count_pari}\n'
      f'N. valori dispari: {count_dispari}\n'
      f'La lista completa: {lista}')