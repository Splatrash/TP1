# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

banque_Mot = {
    "manette": "Appareil utilisé pour jouer à certains jeux vidéo.",
    "bouteille": "Conteneur conçue pour tenir un liquide.",
    "bureau": "Surface de travail.",
    "panier": "Conteneur qui peut contenir des objets solides.",
    "plancher": "On marche dessus."
}

lettre_essaye = []


def demarrageJeu():
    mot = str(random.choice(list(banque_Mot.keys())))
    print()
    print("Bienvenue au bonhomme pendu!")
    print("Essayer de deviner le mot en entrant une lettre à la fois!")
    print("N.B: Ne pas mettre d'accent sur les lettre!")
    print()

    return mot


mot = demarrageJeu()

mot_vide = list("_" * int(len(mot)))
for i in range(0, int(len(mot_vide))):
    print(mot_vide[i], end='')
print("")

lettre_trouvee = 0


def tour(entree, mot, lettre_trouvee, lettre_essaye):
    entree = entree.strip()
    if any(entree in s for s in lettre_essaye):
        print("Vous avez déja essayé la lettre: " + entree)
        return False
    elif entree.isalpha() and int(len(entree)) == 1:
        lettre_essaye.append(entree)
        for j in range(0, int(len(mot))):
            if entree == mot[j]:
                mot_vide[j] = entree
                lettre_trouvee += 1

        if lettre_trouvee == 0:
            print("Cette lettre n'est pas dans ce mot.")
            return True
        else:
            return False

    elif entree == "lettre":
        stop = False
        while not stop:
            position = random.randint(0, int(len(mot)) - 1)
            indice = mot[position]
            if any(indice in s for s in lettre_essaye):
                stop = False
            else:
                stop = True
                print(indice)

        for i in range(0, int(len(mot))):
            if indice == mot[i]:
                mot_vide[i] = indice
                lettre_essaye.append(indice)

        return False
    elif entree == "desc":
        print()
        print("Description: " + banque_Mot[mot])
        print()
        return False
    else:
        print("Veuillez vous assurer d'entrer une lettre ou une méthode d'aide.")
        print("N.B: N'oublier pas que les lettre n'ont pas d'accents.")
        return False


def stage(stage):
    if stage == 0:
        print()
        print("Pour avoir une lettre gratuite écrivez 'lettre'.")
        print("Pour avoir la description du mot écrivez 'desc'.")
        print()
        print(" __________")
        print(" |        |")
        print(" |         ")
        print(" |         ")
        print(" |         ")
        print(" |         ")
        print(" |         ")
        print("_|____________")
        print("")
    elif stage == 1:
        print()
        print("Pour avoir une lettre gratuite écrivez 'lettre'.")
        print("Pour avoir la description du mot écrivez 'desc'.")
        print()
        print(" __________")
        print(" |        |")
        print(" |        o")
        print(" |         ")
        print(" |         ")
        print(" |         ")
        print(" |         ")
        print("_|____________")
        print()
    elif stage == 2:
        print()
        print("Pour avoir une lettre gratuite écrivez 'lettre'.")
        print("Pour avoir la description du mot écrivez 'desc'.")
        print()
        print(" __________")
        print(" |        |")
        print(" |        o")
        print(" |        | ")
        print(" |         ")
        print(" |         ")
        print(" |         ")
        print("_|____________")
        print()
    elif stage == 3:
        print()
        print("Pour avoir une lettre gratuite écrivez 'lettre'.")
        print("Pour avoir la description du mot écrivez 'desc'.")
        print()
        print(" __________")
        print(" |        |")
        print(" |        o")
        print(" |       -| ")
        print(" |         ")
        print(" |         ")
        print(" |         ")
        print("_|____________")
        print()
    elif stage == 4:
        print()
        print("Pour avoir une lettre gratuite écrivez 'lettre'.")
        print("Pour avoir la description du mot écrivez 'desc'.")
        print()
        print(" __________")
        print(" |        |")
        print(" |        o")
        print(" |       -|- ")
        print(" |         ")
        print(" |         ")
        print(" |         ")
        print("_|____________")
        print()
    elif stage == 5:
        print()
        print("Pour avoir une lettre gratuite écrivez 'lettre'.")
        print("Pour avoir la description du mot écrivez 'desc'.")
        print()
        print(" __________")
        print(" |        |")
        print(" |        o")
        print(" |       -|- ")
        print(" |       / ")
        print(" |         ")
        print(" |         ")
        print("_|____________")
        print()



etape = 0
gagner = True
while any("_" in s for s in mot_vide) and etape != 7:
    stage(etape)
    print("")
    if etape < 6:
        entree = str(input("Entrer une lettre ou demandez un indice: "))
        print()
        erreur = tour(entree, mot, lettre_trouvee, lettre_essaye)
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
