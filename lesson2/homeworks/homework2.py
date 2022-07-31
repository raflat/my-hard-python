"""
    Immaginiamo di dover creare un registro di utenti per un Casinò.
    Creare uno script che chieda da terminale i dati di N utenti
    (N è una variabile) e salvare ogni utente in un dizionario.
    I dizionari relativi ad ogni utente devono essere contenuti in una lista.
    Il programma deve rifiutare una inserizione (e terminare)
    se il nickname di uno degli utenti è già presente nel sistema.
    Non terminare il programma usando la funzione exit()
    ma assicurarsi che sia il flow del programma a gestire questo caso.

    I dati dell'utente sono: nickname, eta, gender (per semplicità solo M o F).
    Si dia per scontato che l'utente inserisca sempre dati coerenti
    (non sono da implementare i controlli di validità dei dati inseriti).

    Si cerchi di rendere l'interfaccia testuale il più comprensibile possibile,
    ad esempio, anziché chiedere semplicemente "Inserire nickname" si chieda
    "Inserire nickname" per account i-esimo
    dove i sarà naturalmente compreso fra 1 ed N.
    Aggiungere anche stampe quali "Utente i-esimo inserito!" e
    poi procedere con il prossimo.

    Terminato l'inserimento degli N utenti si stampi un resoconto.
    Alcuni esempi possono essere: la quantità di utenti maschi e femmine,
    il massimo, minimo e media di età, e la lunghezza media dei nickname.
    In python esistono funzioni built-in per fare queste cose:
    evitare di usarle e re-implementare il codice per trovare
    massimo, minimo e media.

    Si suggerisce di utilizzare le strutture di supporto adatte
    alla risoluzione del problema, come ad esempio liste temporanee.
"""

print("SISTEMA DI INSERIMENTO UTENTI DEL CASINÒ")

users_number = int(input("> Numero di utenti: "))
valid_input = True

if users_number <= 0:
    print("Il numero di utenti deve essere maggiore di zero")
    valid_input = False

users = []
i = 0
while valid_input and i < users_number:
    user = {}
    print("\nInserire dati ", i + 1, "-esimo utente", sep="")
    user["Nickname"] = input("> Nickname: ")
    user["Eta"] = int(input("> Età: "))
    user["Gender"] = input("> Gender: ")

    for u in users:
        if u["Nickname"] == user["Nickname"]:
            print("\n", user["Nickname"], " è un nickname già usato", sep="")
            valid_input = False

    if valid_input:
        users.append(user)
        print("Utente inserito correttamente")

        i += 1

if i == users_number:
    males_number = 0
    max_age = min_age = users[0]["Eta"]
    sum_ages = sum_nick_len = 0
    for u in users:
        if u["Gender"] == "M":
            males_number += 1

        u_age = u["Eta"]
        if u_age > max_age:
            max_age = u_age
        if u_age < min_age:
            min_age = u_age

        sum_ages += u_age
        sum_nick_len += len(u["Nickname"])

    print("\nResoconto")
    print("- utenti maschi:", males_number)
    print("- utenti femmine:", users_number - males_number)
    print("- età massima:", max_age)
    print("- età minima:", min_age)
    print("- età media:", round(sum_ages / users_number))
    print("- lunghezza media nickname:", round(sum_nick_len / users_number))
