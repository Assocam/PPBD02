def ask_input():
    question = input("inserisci un numero intero: ")
    while True:
        if question.isdigit():
            return question
        else:
            print(f'Il valore inserito non è una cifra numerica! {question}')
#- Main()

input_user = int(ask_input())
counter = 0
counter2 = 0


while counter < input_user: # quadrato
    print('*' * input_user)
    counter += 1
counter = 0

while counter < (input_user-1): # 0++ < input
    if not(counter2 % 2): 
        counter2 += 1
    print('-' * ((input_user - counter) - 1) + '*' * counter2 + '-' * ((input_user - counter) - 1))
    counter += 1
    counter2 += 1 

counter = 0
counter2 += 1

while counter < input_user:
    if not(counter2 % 2):
        counter2 -= 1
    print('-' * (counter) + '*' * counter2 + '-' * (counter))
    counter += 1
    counter2 -= 1

for _ in range(input_user):
    print('*' * input_user)