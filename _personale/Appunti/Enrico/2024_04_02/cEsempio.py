# Esempio classi

# File con codice per fare classi

# Come si fa una classe con python?

class casa:
    # Questa è la classe BASE

    def commento(self):                          # La funzione commento deve dirmi casa - è un metodo
        return ('casa')                          # self = segnaposto dell'istanza, si riferisce a se stessa, essendo la prima

    pass                                         # Non fa nulla

class appartamento(casa):                        # Che eredita da casa
    def commento(self):                          # Stesso nome ma fa cose diverse
        return ('questo è un appartamento')
    pass

class attico(appartamento):                      # Che eredita da appartamento
    def commento(self):                          # Stesso nome ma fa cose diverse
      # return ('ora questo è un attico')
        return super().commento(self)
    pass



pippo = casa                                     # Una variabile assegnata a una classe

print(pippo.commento(casa))                      # Anche pippo, pluto e topolino diranno casa come metodo ereditato da "casa"

pluto = appartamento
print(pluto.commento(appartamento))

topolino = attico
print(topolino.commento(attico))                 # Scrivono la classe commento











