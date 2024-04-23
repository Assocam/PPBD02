# PROGRAMMA PAGELLA CON LISTE PPBD02-14
def calcola_media(voti):
    return round(sum(voti) / len(voti), 2)                              # Numeratore delle decine

def main():
    num_studenti = int(input("Inserisci il numero di studenti: "))      # Metti il numero degli studenti
    pagella = []

    lista_materie = ['matematica', 'italiano', 'inglese', 'storia']

    for i in range(num_studenti):             
        nome = input("Inserisci il nome dello studente: ")
        cognome = input("Inserisci il cognome dello studente: ")
        classe = input("Inserisci la classe dello studente: ")

        pagella_studente = {'nome': nome, 'cognome': cognome, 'classe': classe,}
       
        voto_max = 0
        voto_min = 101
        voti_tot = []

        for mat in lista_materie:

            voti_input = []
            
            print(f'Inserisci voto in {mat} ')
            
            for idx in range(2):                        # Metti il numero massimo dei voti tra parentesi
                voto = int(input('Inserisci voti: '))   # aggiornato il voto

                if voto > voto_max:
                    voto_max = voto
                if voto < voto_min:
                    voto_min = voto

                voti_input.append(voto)

                voti_tot.append(voto)

            media = calcola_media(voti_input)
            pagella_studente[mat] = media

        media_globale = calcola_media(voti_tot)

        pagella_studente["max"] = voto_max       
        pagella_studente["min"] = voto_min      
        pagella_studente["globale"] = media_globale      
        pagella.append(pagella_studente)

    # print(pagella)

    for pagella_studente in pagella:
        print(f"Nome alunno: {pagella_studente['nome']} {pagella_studente['cognome']}")
        print(f"Classe alunno: {pagella_studente['classe']}")
        print(f"Media per Matematica: {pagella_studente['matematica']}")
        print(f"Media per Italiano: {pagella_studente['italiano']}")
        print(f"Media per Inglese: {pagella_studente['inglese']}")
        print(f"Media per Storia: {pagella_studente['storia']}")
        print(f"Media globale dell'alunno: {pagella_studente['globale']}")
        print(f"Il voto più alto dell'alunno: {pagella_studente['max']}")
        print(f"Il voto più basso dell'alunno: {pagella_studente['min']}")
        print("\n")

if __name__ == "__main__":               # Per importare moduli successivi
    main()
