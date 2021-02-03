# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from demarrage import demarrageJeu
from tours import tour
from stages import stage

banque_mots = {
    "manette": "Appareil utilisé pour jouer à certains jeux vidéo.",
    "bouteille": "Conteneur conçue pour tenir un liquide.",
    "bureau": "Surface de travail.",
    "panier": "Conteneur qui peut contenir des objets solides.",
    "plancher": "On marche dessus."
}

lettre_essaye = []

mot = demarrageJeu(banque_mots)

mot_vide = list("_" * int(len(mot)))
for i in range(0, int(len(mot_vide))):
    print(mot_vide[i], end='')
print("")

lettre_trouvee = 0

etape = 0
gagner = True

while any("_" in s for s in mot_vide) and etape != 7:
    stage(etape)
    print("")
    if etape < 6:
        entree = str(input("Entrer une lettre ou demandez un indice: "))
        print()
        erreur = tour(entree, mot, lettre_trouvee, lettre_essaye, mot_vide, banque_mots)
        if erreur:
            etape += 1
        print("Lettre essayé: ", lettre_essaye)
        print("")
        for i in range(0, int(len(mot_vide))):
            print(mot_vide[i], end='')
        print()
    else:
        print()
        print()
        print(" __________")
        print(" |        |")
        print(" |        o")
        print(" |       -|- ")
        print(" |       / \\")
        print(" |         ")
        print(" |         ")
        print("_|____________")
        print()

        print("Vous avez perdu!")
        etape += 1
        gagner = False

if gagner:
    print("Vous avez gagner!")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
