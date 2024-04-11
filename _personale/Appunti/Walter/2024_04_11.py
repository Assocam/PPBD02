'''
def saluta(nome, titolo='Egr.'):     # Mai dare un parametro definito prima, sempre DOPO (titolo='Egr.', nome),
    print(titolo, nome)              # non diventerebbe più facoltativo

saluta('Rossi')  # Uso del titolo predefinito
saluta('Bianchi', 'Dott.')  # Specifica il titolo senza uso della keyword
saluta(nome='Verdi', titolo='Ing.')  # Specifica il titolo usando la keyword
'''

# Vedere lezione 5.3 - Importante    <-----------------------------------------

'''
def add_player(player, team=[]):   # questa è una roba pericolosa, perché richiamando sempre la funzione 
                                     ci sarà sempre lo stesso oggetto
'''
