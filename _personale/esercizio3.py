def quadrato(lato):

    perimetro = lato * 4
    area = lato * lato

    return perimetro, area
#------------------------------------------------------------------------

# print('dati di un quadrato di lato 3')
# 
# p,a = quadrato(3)
# 
# print('Perimetro' , p , 'area' , a)

def rettangolo(base, altezza):

    perimetro = (base + altezza) * 2
    area = base * altezza 

    return perimetro, area

def triangolo (base, altezza, l1 , l2 , l3):

    perimetro = l1 + l2 + l3
    area = (base * altezza) /2

    return perimetro , area 

