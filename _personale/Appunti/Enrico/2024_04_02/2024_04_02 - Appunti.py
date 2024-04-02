# OOP - Object Oriented Programming.
# 4 pilastri fondamentali - Python usa i primi due, Java, C#, C++ li usa tutti e 4

# 1) Ereditarietà:
# Posso fare una classe e una sua sottoclasse, ereditando le caratteristiche di una classe base,
# specializzandole in classi più specifiche, ereditando le caratteristiche di cui sopra.
# Esempio: classe casa, che ha come caratteristicha m^2. Una classe attico avrà ancora
# la caratteristica m^2 ereditata dalla classe principale.

# 2) Polimorfismo:
# Si intende la possibilità di adattare una classe
# Esempio: classe casa, da cui derivo la classe attico.
# attico lo uso come attico, ma la posso usare come casa, perché attico ha tutte le caratteristiche 
# di casa, più nello specifico le sue caratteristiche. Casa invece non la posso usare come attico.
# Salendo di classe posso applicare il polimorfismo, prendendo le caratteristiche di una classe
# meno specializzata e la cosa funziona limitatamente alle caratteristiche che io trovo in casa.

# 3) Incapsulamento - (metodo incapsulato):
# Mi serve per decidere che alcune caratteristiche di una qualche classe non sono esattamente pubbliche,
# ma sono private alla classe che le ha generate. Esempio: casa e attico, oltre a m^2 hanno "millesimi",
# quota di appartenenza dell'attico al condominio. I millesimi non sono direttamente utilizzabili,
# poiché so i millesimi sommando tutti gli appartamenti del condominio, non posso usarla subito direttamente.
# Quindi millesimi è incapsulata all'interno di attico. 
# Se ho una roba tipo millesimi (è pubblica), se uso "_millesimi" è debolmente incapsulata, se la chiamo
# "__millesmi__" (due underscore) è fortemente incapsulata.

# 4) Astrazione: 
# Un metodo astratto è semplicemente una classe o un metodo di cui dichiaro l'esistenza ma non ha nessuna
# implementazione. Quando la uso il compilatore dice che non l'hai implementata, serve più a dichiarare
# quelle che sono le idee relative alla classe.


# La programmazione a oggetti può avere un'organizzazione strutturata o orientata agli eventi.
# Esempio di etichette che fanno riferimento a più aree di un'azienda, stesse voci, parametri diversi (magazzino, uffici, ecc.)



# In "cEsempio2.py" abbiamo creato una classe "Animale", con proprietà "ha le ali" (ali) e "ha il pelo" (pelo), caratteristiche
# di tutti gli animali.
# Quando creo una istanza (pippo) di classe "animali", gli devo dire che ha pelo e ali:
# pippo = animale(pelo, ali)
# Devo usare un costruttore: "__init__(self)" fa in modo che ci vada una istanza in animale.
# Nel costruttore DEVO AGGIUNGERE ali e pelo --> __init__(self, ali, pelo)
#
# la classe cane eredita le caratteristiche dalla classe animale: cane(animale)
# essendo un animale il cane ha "ali" e "pelo"

# Se scrivo pluto = cane(pelo, ali), devo comunque scrivere che ha pelo e ali
# non devo chiamare un altro costruttore, ma quello della classe precedente, ovvero super()
# super().__init__(self, ali, pelo)

# Se un domani volessi cambiare pelo e ali mi basta cambiare la classe animale,
# in cascata avranno il diverso uso del cambio pelo, ali
#
#


