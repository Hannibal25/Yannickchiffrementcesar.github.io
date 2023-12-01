# Fonction de création de la grille de Polybe
def creer_grille_polybe():
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J est remplacé par I
    grille = {}
    for i in range(5):
        for j in range(5):
            if len(alphabet) > 0:
                grille[alphabet[0]] = (i + 1, j + 1)
                alphabet = alphabet[1:]
            else:
                grille[str(i) + str(j)] = (i + 1, j + 1)
    return grille

# Fonction de chiffrement avec Polybe
def chiffrement_polybe(message):
    grille = creer_grille_polybe()
    # Convertit en majuscules et remplace J par I
    message = message.upper().replace("J", "I")
    message_chiffre = ""
    for lettre in message:
        if lettre.isalpha() or lettre.isdigit():
            if lettre != " ":
                message_chiffre += str(grille[lettre][0]) + \
                    str(grille[lettre][1]) + " "
        else:
            message_chiffre += lettre
    return message_chiffre.strip()

# Fonction de déchiffrement avec Polybe
def dechiffrement_polybe(message_chiffre):
    grille = creer_grille_polybe()
    message_dechiffre = ""
    coordonnees = message_chiffre.split()
    for coord in coordonnees:
        ligne = int(coord[0])
        colonne = int(coord[1])
        for lettre, c in grille.items():
            if c == (ligne, colonne):
                message_dechiffre += lettre
    return message_dechiffre.replace("I", "J")

# Demander à l'utilisateur d'entrer le message à chiffrer
message_original = input("Entrez le message à chiffrer : ")

message_chiffre = chiffrement_polybe(message_original)

print("Message chiffré :", message_chiffre)

# Demander à l'utilisateur d'entrer le message chiffré pour le déchiffrer
message_chiffre_input = input("Entrez le message chiffré pour le déchiffrer : ")
message_dechiffre = dechiffrement_polybe(message_chiffre_input)

print("Message déchiffré :", message_dechiffre)
