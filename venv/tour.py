def tour(entree, mot, lettre_trouvee, lettre_essaye, mot_vide):
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
        return False