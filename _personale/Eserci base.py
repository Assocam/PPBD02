# Minimo comune multiplo

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def lcm_of_list(numbers):
    if len(numbers) == 0:
        return None
    lcm_result = numbers[0]
    for num in numbers[1:]:
        lcm_result = lcm(lcm_result, num)
    return lcm_result

# Esempio di utilizzo:
lista_numeri = [3, 6, 9, 12, 15]
print("Lista di numeri:", lista_numeri)
print("Minimo comune multiplo:", lcm_of_list(lista_numeri))













