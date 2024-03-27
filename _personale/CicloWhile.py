def continue_method(): # cycle to ask if the user want to continue the program.
    while True: 
        answer = input ("Continue?(Y/N): ")
        answer = answer.lower()[0] if answer != '' else None
        if answer == 'y':
            break # break the cycle and return to the main restarting the current cycle if there's one.
        elif answer == 'n':
            exit () # stop the program
        else:
            print (f'valore non valido: {answer}')
            continue # restart the while

#--
#main()
while True:
 
    x = input ('Prego, inserire un numero:')

    if x.replace('.', '').isdigit():
        x = float(x)

        print (f'{x} > 0 and {x} < 100: {x > 0 and x < 100}') 
        print (f'{x} > 0 or {x} < 100: {x > 0 or x < 100}') 
        print (f'{x} > 0 or 100 < {x}: {x > 0 or x < 100}') 
        print (f'{x} > 0 and {x} < 100 or {x} == -1: {x > 0 and x < 100 or x == -1}')
        continue_method()
    else:
        print (f'Valore non valido: {x}')
        continue_method()