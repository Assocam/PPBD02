class animale:

# Serve un COSTRUTTORE per dare i parametri della sua esistenza (__init__).
    
    def __init__(self, pelo, ali):

        self.HaPelo = pelo               # Variabili di istanza
        self.HaAli = ali

    def Descrizione(self):               # Metodo descrizione
        if self.HaPelo:                  # Se è vero che ha il pelo
            spelo = 'ha il pelo'
        else:
            spelo = 'non ha pelo'
        if self.HaAli:                   # Se è vero che ha le ali
            sali = 'ha le ali'
        else:
            sali = 'non ha le ali'

        return f'Questo animale {spelo} e {sali}.'


# Introduciamo delle sottoclassi senza scrivere nuovi metodi, che verranno ereditati dalla classe animale.

class cane(animale):                      # Deriva la descrizione da animale               

    # def __init__(self, p, a):
    #     super().__init__(p, a)            # Diamo i falso e vero tramite l'inizializzatore degli attributi superiori pelo e ali
    def Verso(self, verso):
        self.verso = verso


class uccello(animale):

    # def __init__(self, p, a):
    #     super().__init__(p, a)      # Diamo direttamente i falso e vero agli attributi superiori pelo e ali
    def Verso(self, verso):
        self.verso = verso


class pesce(animale):
    # def __init__(self, p, a):
    #     super().__init__(p, a)
    pass

# <------------------------------------------ Fine descrizione classi -------------------------------------------------->

# Qui comincia lo script

bestia = animale(True, False)     # Ha il pelo? True - Ha le ali? False
# hp = bestia.HaPelo
# ha = bestia.HaAli

bau = cane(True, False)
rondine = uccello(False, True)
trota = pesce(False, False)

bau.Verso = 'Bau bau'
rondine.Verso = 'Cip Urrrrrr Cip'

print('Bestia:', bestia.Descrizione())
print('Bau:', bau.Descrizione())
print('Rondine:', rondine.Descrizione())
print('Trota:', trota.Descrizione())

print('Il cane fa:', bau.Verso)
print('La rondine fa:', rondine.Verso)


# def prova(w:animale):              # prova tratta tutto ugualmente come animale
#     print(w.Descrizione())
#     print(w.Verso)                 # questo non va perché non è presente in classe animale, ovvero polimorfismo

# prova(bestia)

# prova(bau)

# prova(rondine)

# prova(trota)

def cucu(w:cane):                    # prova tratta tutto ugualmente come cane
    print(w.Verso)

# cucu(bestia)
cucu(bau)
cucu(rondine)
# cucu(trota)
