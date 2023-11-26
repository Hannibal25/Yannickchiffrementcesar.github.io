<!-- Introduction -->
print("CHIFFREMENT DE CESAR")
print("Ce programme permet de chiffrer et de déchiffrer des messages.")

# Ces deux lignes sont des instructions d’impression qui affichent une introduction à l’utilisateur. Elles expliquent que le programme est une implémentation du chiffrement de César, qui peut chiffrer et déchiffrer des messages.

<!-- Entrée du texte à chiffrer -->
message_a_coder = input("Rentrez votre texte à chiffer :")

# Cette ligne demande à l’utilisateur d’entrer le texte qu’il souhaite chiffrer. La fonction input() est utilisée pour obtenir l’entrée de l’utilisateur, qui est ensuite stockée dans la variable message_a_coder.

<!-- Entrée de la clé  -->
while True:
    try:
        clef = int(input("Rentrez votre clé :"))
        break
    except ValueError:
        print("Veuillez entrer un nombre entier valide pour la clé.")
# Ces lignes demandent à l’utilisateur d’entrer une clé, qui est un nombre entier. Cette clé sera utilisée pour décaler les caractères dans le texte à chiffrer. Si l’utilisateur n’entre pas un nombre entier, le programme affiche un message d’erreur et continue de demander une clé jusqu’à ce qu’un nombre entier valide soit entré.

<!-- Chiffrement  -->

message_chiffré = [(ord(i)+clef) for i in message_a_coder]
message_chiffré_final = "".join([chr(i) for i in message_chiffré])
print("Message chiffré : ", message_chiffré_final)

# Ces lignes chiffrent le texte en décalant chaque caractère du texte par la valeur de la clé. Elles utilisent la fonction ord() pour obtenir la valeur ASCII de chaque caractère, puis ajoutent la clé à cette valeur. Le résultat est converti en caractère avec la fonction chr() et ajouté à une liste. Cette liste est ensuite convertie en une chaîne et affichée à l’utilisateur.

<!-- Entrée du texte à déchiffrer -->

message_a_coder = input("Rentrez votre texte à déchiffrer :")

# Cette ligne demande à l’utilisateur d’entrer le texte qu’il souhaite déchiffrer.

<!-- Déchiffrement  -->

message_déchiffré = [(ord(i)-clef) for i in message_chiffré_final]
message_déchiffré_final = "".join([chr(i) for i in message_déchiffré])
print("Message déchiffré : ", message_déchiffré_final)

# Ces lignes déchiffrent le texte en décalant chaque caractère du texte dans la direction opposée par la valeur de la clé. Elles utilisent la fonction ord() pour obtenir la valeur ASCII de chaque caractère, puis soustraient la clé de cette valeur. Le résultat est converti en caractère avec la fonction chr() et ajouté à une liste. Cette liste est ensuite convertie en une chaîne et affichée à l’utilisateur.

#  En résumé, ce programme est une implémentation simple du chiffrement de César en Python. Il permet à l’utilisateur de chiffrer et de déchiffrer des messages en utilisant une clé de décalage spécifiée par l’utilisateur.