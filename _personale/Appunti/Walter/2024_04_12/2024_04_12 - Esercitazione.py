# Esercitazione INF_PR_PY_E04
# Denominazione: Programma Pagella con le liste

# Definizione studente:
nome = input('Inserire il nome dello studente: ')
cognome = input('Inserire il cognome dello studente: ')
classe = input('Inserire la classe frequentata dallo studente: ')

# Materie - Liste vuote
matematica = []
italiano = []
inglese = []
storia = []

voti = input('Indicare quanti voti vuoi inserire per materia: ')
voti = int(voti)

print(f'Pagelle: inserire {voti} voti per materia in CENTESIMI - Voto tra 1 e 100.')


for m in range (1,voti+1):
    math = input(f'Inserire il voto {m} di matematica: ')
    math = int(math)
    matematica.append(math)


print('Attenzione, cambio materia: Italiano!')

for it in range (1,voti+1):
    ita = input(f'Inserire il voto {it} di italiano: ')
    ita = int(ita)
    italiano.append(ita)

print('Attenzione, cambio materia: Inglese!')

for ing in range (1,voti+1):
    ingle = input(f'Inserire il voto {ing} di Inglese: ')
    ingle = int(ingle)
    inglese.append(ingle)

print('Attenzione, cambio materia: Storia!')

for s in range (1,voti+1):
    sto = input(f'Inserire il voto {s} di storia: ')
    sto = int(sto)
    storia.append(sto)

print(f'Ecco la lista di voti inseriti per lo studente {nome} {cognome} della classe {classe}: \n'
      f'Matematica: {matematica}\n'
      f'Italiano: {italiano}\n'
      f'Inglese: {inglese}\n'
      f'Storia: {storia}')

media_matematica = sum(matematica)/len(matematica)
media_italiano = sum(italiano)/len(italiano)
media_inglese = sum(inglese)/len(inglese)
media_storia = sum(storia)/len(storia)

print(f'La media dello studente {nome} {cognome} della classe {classe} in ogni materia è:\n'
      f'Matematica: {media_matematica:.2f}\n'
      f'Italiano: {media_italiano:.2f}\n'
      f'Inglese: {media_inglese:.2f}\n'
      f'Storia: {media_storia:.2f}')

media_globale = (media_matematica + media_italiano + media_inglese + media_storia)/4

print(f'La media globale dello studente {nome} {cognome} è: {round(media_globale)}')

megalista = matematica + italiano + inglese + storia

print(f'Il voto più alto registrato è {max(megalista)}\n'
      f'Il voto più basso registrato è {min(megalista)}.')