# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

Banque_Mot = {
    "manette": "Appareil utilisé pour jouer à certains jeux vidéo.",
    "bouteille": "Conteneur conçue pour tenir un liquide.",
    "bureau": "Surface de travail.",
    "panier": "Conteneur qui peut contenir des objets solides.",
    "plancher": "On marche dessus."
}


def demarrageJeu():
    mot = str(random.choice(list(Banque_Mot.keys())))
    print("Bienvenue au bonhomme pendue!")
    print("Essayer de deviner le mot!")
    print("Pour avoir une lettre gratuite écrivez 'lettre'.")
    print("Pour avoir la description du mot écrivez 'des'.")
    print("")
    print(" __________")
    print(" |        |")
    print(" |         ")
    print(" |         ")
    print(" |         ")
    print(" |         ")
    print(" |         ")
    print("_|____________")
    print("")
    print("Lettre essayées: ")
    print("")

    return mot


mot = demarrageJeu()

mot_vide = list("_" * int(len(mot)))
for i in range(0, int(len(mot_vide))):
    print(mot_vide[i], end='')
print("")

lettre_trouvee = 0
erreur = 0

def tour(entree, mot, lettre_trouvee):
    entree = entree.strip()
    if entree.isalpha() and int(len(entree)) == 1:
        for j in range(0, int(len(mot))):
            if entree == mot[j]:
                mot_vide[j] = entree
                lettre_trouvee += 1


while lettre_trouvee != int(len(mot)) or erreur == 8:
    entree = str(input("Entrer une lettre ou demandez un indice: "))
    tour(entree, mot, lettre_trouvee)
    for i in range(0, int(len(mot_vide))):
        print(mot_vide[i], end='')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
