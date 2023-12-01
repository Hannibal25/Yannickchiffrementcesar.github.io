def est_nombre_premier(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def chiffrement_affine(phrase, a, b):
    if not est_nombre_premier(a):
        print("La valeur de 'a' n'est pas un nombre premier. Veuillez entrer un nombre premier.")
        return None

    resultat = ""
    for caractere in phrase:
        if caractere.isalpha():
            if caractere.islower():
                resultat += chr((a * (ord(caractere) - ord('a')) + b) %
                                26 + ord('a'))
            else:
                resultat += chr((a * (ord(caractere) - ord('A')) + b) %
                                26 + ord('A'))
        else:
            resultat += caractere
    return resultat


def dechiffrement_affine(phrase_chiffree, a, b):
    if not est_nombre_premier(a):
        print("La valeur de 'a' n'est pas un nombre premier. Impossible de déchiffrer.")
        return None

    a_inverse = 0
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inverse = i
            break

    if a_inverse == 0:
        print("Impossible de trouver l'inverse de 'a'.")
        return None

    resultat = ""
    for caractere in phrase_chiffree:
        if caractere.isalpha():
            if caractere.islower():
                resultat += chr((a_inverse * (ord(caractere) -
                                ord('a') - b)) % 26 + ord('a'))
            else:
                resultat += chr((a_inverse * (ord(caractere) -
                                ord('A') - b)) % 26 + ord('A'))
        else:
            resultat += caractere
    return resultat


phrase_a_chiffrer = input('Entrez la phrase à chiffrer : ')
a = int(input('Entrez la valeur de a (nombre premier) : '))
while not est_nombre_premier(a):
    print("La valeur de 'a' n'est pas un nombre premier.")
    a = int(input('Entrez à nouveau la valeur de a (nombre premier) : '))
b = int(input('Entrez le décalage : '))
phrase_chiffree = chiffrement_affine(phrase_a_chiffrer, a, b)
if phrase_chiffree:
    print("Phrase chiffrée:", phrase_chiffree)

# Déchiffrement
phrase_chiffree_input = input('Entrez la phrase chiffrée à déchiffrer : ')
phrase_dechiffree = dechiffrement_affine(phrase_chiffree_input, a, b)
if phrase_dechiffree:
    print("Phrase déchiffrée:", phrase_dechiffree)
