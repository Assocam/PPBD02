def calcola_media(voti):
    return round(sum(voti) / len(voti), 2)

def main():
    num_studenti = int(input("Inserisci il numero di studenti: "))
    pagella = []

    for i in range(num_studenti):
        nome = input("Inserisci il nome dello studente: ")
        cognome = input("Inserisci il cognome dello studente: ")
        classe = input("Inserisci la classe dello studente: ")
        matematica = int(input("Inserisci il voto in matematica (0-100): "))
        italiano = int(input("Inserisci il voto in italiano (0-100): "))
        inglese = int(input("Inserisci il voto in inglese (0-100): "))
        storia = int(input("Inserisci il voto in storia (0-100): "))

        media_matematica = calcola_media([matematica])
        media_italiano = calcola_media([italiano])
        media_inglese = calcola_media([inglese])
        media_storia = calcola_media([storia])

        media_globale = round(sum([media_matematica, media_italiano, media_inglese, media_storia]) / 4)

        voti = [matematica, italiano, inglese, storia]
        voto_massimo = max(voti)
        voto_minimo = min(voti)

        pagella.append({
            'nome': nome,
            'cognome': cognome,
            'classe': classe,
            'media_matematica': media_matematica,
            'media_italiano': media_italiano,
            'media_inglese': media_inglese,
            'media_storia': media_storia,
            'media_globale': media_globale,
            'voto_massimo': voto_massimo,
            'voto_minimo': voto_minimo
        })

    for studente in pagella:
        print(f"Nome alunno: {studente['nome']} {studente['cognome']}")
        print(f"Classe alunno: {studente['classe']}")
        print(f"Media per Matematica: {studente['media_matematica']}")
        print(f"Media per Italiano: {studente['media_italiano']}")
        print(f"Media per Inglese: {studente['media_inglese']}")
        print(f"Media per Storia: {studente['media_storia']}")
        print(f"Media globale dell'alunno: {studente['media_globale']}")
        print(f"Il voto più alto dell'alunno: {studente['voto_massimo']}")
        print(f"Il voto più basso dell'alunno: {studente['voto_minimo']}")
        print("\n")

if __name__ == "__main__":
    main()
