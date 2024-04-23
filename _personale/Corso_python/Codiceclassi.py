# File con codice classi

class casa:
    # Questa è la classe base
    def commento(self):                                                                                 # self è la risoluzione dell'istanza
        return('casa')
    pass

class appartamento(casa):
    def commento(self):
        return('Questo è un appartamento')
    pass        

class attico(appartamento):
    def commento(self):
        return super().commento(self)
    pass

pippo = casa    

print(pippo.commento(casa))                                                                             # Istanza

pluto = appartamento 
print(pluto.commento(appartamento))

topolino = attico 
print(topolino.commento(attico))
