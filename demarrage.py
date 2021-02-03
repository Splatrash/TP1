import random

def demarrageJeu(banque_mots):
    mot = str(random.choice(list(banque_mots.keys())))
    print()
    print("Bienvenue au bonhomme pendu!")
    print("Essayer de deviner le mot en entrant une lettre à la fois!")
    print()

    return mot