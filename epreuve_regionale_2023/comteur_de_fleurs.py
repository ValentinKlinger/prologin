def compteur_de_fleurs(champ):
    compteur = 0
    for i in range(len(champ) - 2):
        if champ[i] == "B" and champ[i + 1] == "J" and champ[i + 2] == "R":
            compteur += 1
    return compteur


if __name__ == "__main__":
    champ = list(input())
    print(compteur_de_fleurs(champ))
