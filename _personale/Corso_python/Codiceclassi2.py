#-------------------------DEFINIZIONI DELLE CLASSI-----------------------------

class animale:                              # Una classe deve far entrare qualcosa e far uscire

    def __init__(self, pelo, ali):          # Costruttore

        self.hapelo = pelo
        self.haali = ali

    def Descrizione(self):                  # Descrizione e gestione
        if self.hapelo:
            spelo = 'ha il pelo'
        else:
            spelo = 'non ha il pelo'
        if self.haali:
            sali = 'ha le ali'
        else:
            sali = 'non ha le ali'

        return f'Questo animale {spelo} e {sali}'
    
class cane(animale):
    pass 
    def verso(self, verso):
        self.verso = verso                  # richiama la classe sopra del costruttore

class uccello(animale):
    def verso(self, verso):
        self.verso = verso
    pass
    
class pesce(animale):
    pass
    
#----------------------------------SCRIPT--------------------------------------       

bestia = animale(True, False)
bau = cane(True, False)
rondine = uccello(False, True)
trota = pesce(False, False)

# per il verso

bau.verso = 'Bau Bau'
rondine.verso = 'Cip uuuuuuuuuurw Cip'

print('Bestia:' , bestia.Descrizione())
print('Cane:' , bau.Descrizione())
print('Uccello:' , rondine.Descrizione())
print('Trota:' , trota.Descrizione())

print('Il cane fa' , bau.verso)
print('La rondine fa' , rondine.verso)

def prova(w : animale):                                          # Polimorfismo attributi ereditati da una classe ad un'altra
    print(w.Descrizione)

def cucu(w : cane):
    print(w.verso)

prova(bestia)
prova(bau)
prova(rondine)
prova(trota)

cucu(bau)
cucu(rondine)



