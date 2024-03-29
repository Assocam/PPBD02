# Software di BackEnd:

from flask import Flask, request
import json

app = Flask('esercizio')


# la '@' è un decoratore di funzione, gli diciamo di rispondere alla rotta "prova"
# quindi la rotta è il percorso che voglio vedere su "internet"

# <---------------- Definizione rotte (API) --------------------------------->

# @app.route('/prova')                                   # Eseguiamo una rotta che si chiama "/prova"

@app.route('/prova', methods = ['GET','POST', 'PUT'])    # Di default il metodo è solo GET, noi specifichiamo anche gli altri
def funzioneprova():                                     # Se tolgo get, su chrome che ha solo GET compare un errore 
#                                                        # "method not allowed"    
    return 'Benvenuto nella pagina di prova'
    # return 'Benvenuto nella pagina di prova', 501      # 501 è un messaggio di errore http 
#                                                        # (https://it.wikipedia.org/wiki/Codici_di_stato_HTTP)

# @app.route('/prova2')
# def p2():

    # return 'questa è la rotta PROVA2'                  # Se adesso vado su chrome: 127.0.0.1/prova2 leggo il messaggio

# <-------------------------------------------------------------------------->

@app.route('/login', methods = ['POST'])
def faiillogin():
   
   try:
    
       datij = request.json
       dati = json.loads(datij)
       u = dati['user']
       p = dati['password']


       print(f'User: {u}, Pwd: {p}')
       codice = 200
       messaggio = 'Dati OK'

   except Exception as e:
      
      print(e)
      
      print('Dati errati')
      codice = 500
      messaggio = e.__repr__()

   return messaggio, codice


if (__name__ == '__main__'):                             # Se l'entry point dell'applicazione si chiama main
    app.run(host = '0.0.0.0', port = 80)                 # lanciala stando in ascolto di questo indirizzo ip (0.0.0.0 sono tutti
                                                         # gli indirizzi) alla porta 80

