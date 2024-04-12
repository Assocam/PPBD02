def saluta(**kwargs):
    print(kwargs)

# Da praticamente un dizionario
saluta(sdf= 345, pippo = 'pluto', nm = None)    # --> {'sdf': 345, 'pippo': 'pluto', 'nm': None}

# Da praticamente una tupla
saluta(345, 'pippo', 'nm')                      # --> (345, 'pippo', 'nm')
