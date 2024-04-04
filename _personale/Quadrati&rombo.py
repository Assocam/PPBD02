def ask_input():
    question = input("inserisci un numero intero: ")
    while True:
        if question.isdigit():
            return question
        else:
            print(f'Il valore inserito non è una cifra numerica! {question}')
#- Main()

input = int(ask_input())
counter = 0
counter2 = 0


while counter < input: # quadrato
    print('*' * input)
    counter += 1
counter = 0

while counter < (input-1): # 0++ < input
    if not(counter2 % 2): 
        counter2 += 1
    print(' ' * ((input - counter) - 1) + '*' * counter2)
    counter += 1
    counter2 += 1 

counter = 0
counter2 += 1

while counter < input:
    if not(counter2 % 2):
        counter2 -= 1
    print(' ' * (counter) + '*' * counter2)
    counter += 1
    counter2 -= 1