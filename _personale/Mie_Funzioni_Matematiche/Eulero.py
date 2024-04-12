from math import pi
from math import e
import cmath

print(e)
print(pi)

i = complex(0.0, 1.0)
n = (e**((-i)*pi))

eulero = n.real + 1

print(f'e^(i*pi) + 1 = {eulero}')