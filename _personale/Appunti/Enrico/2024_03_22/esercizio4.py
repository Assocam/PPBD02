from esercizio3 import quadrato, rettangolo, triangolo

latoQuadrato = 6

print(f'Il lato del quadrato è {latoQuadrato}')
p,a = quadrato(latoQuadrato)
print(f'Area = {a}, Perimetro = {p}')

base = 10
altezza = 7

print(f'Ora voglio calcolare un rettangolo che abbia base = {base} e altezza {altezza}')
p,a = rettangolo(base, altezza)
print(f'Area = {a}, Perimetro = {p}')

lato1 = base
lato2 = 18
lato3 = 12

print(f'Ora voglio un triangolo con i lati {lato1}, {lato2} e {lato3}')
p,a = triangolo(base, altezza, lato1, lato2, lato3)
print(f'Area = {a}, Perimetro = {p}')
