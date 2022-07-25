"""
    Creare uno script di python che simuli il login ad un sito di casinò.
    Si chieda all'utente: nome, cognome ed età.
    Si verifichi che il nome e il cognome siano più lunghi di un carattere e che l'età sia almeno
    18 anni.
    Se tutto è corretto stampare una stringa di conferma, altrimenti comunicare l'errore all'utente.
    Si consideri che l'utente fornità sempre dati di tipo corretto.
    Stampare il resoconto dei dati, assicurandosi che nome e cognome inizino con la maiuscola.
"""

print("Inserire dati utente casinò")
nome = input("> nome: ")
cognome = input("> cognome: ")
eta = int(input("> età: "))

errore = True
if len(nome) < 2:
    print("Errore: il nome deve almeno avere 2 caratteri.")
elif len(cognome) < 2:
    print("Errore: il cognome deve almeno avere 2 caratteri.")
elif eta < 18:
    print("Errore: l'età deve almeno essere 18 anni.")
else:
    errore = False

if not errore:
    print("\nResoconto dati")
    print("> nome: ", nome.capitalize())
    print("> cognome: ", cognome.capitalize())
    print("> età: ", eta)
