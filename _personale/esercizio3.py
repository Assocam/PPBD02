def quadrato(lato):         # simbolo(parametro)
    
    perimetro = 4*lato
    area = lato**2

    return perimetro, area                   
    
# <------- Qui finisce la definizione ------->

# print('dati di un quadrato di lato 5')

# p,a = quadrato(5)

# print('Perimetro', p, 'area', a)

# <----------------------------------------->

def rettangolo(base, altezza):
    
    perimetro = (base + altezza) * 2
    area = base * altezza

    return perimetro, area


def triangolo(base, altezza, l1, l2, l3):

    perimetro = l1 + l2 + l3
    area = (base*altezza)/2

    return perimetro, area

