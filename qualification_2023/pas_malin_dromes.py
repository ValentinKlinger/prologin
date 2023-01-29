def nb_pas_malin_drome(n, mots):
    nb_pas_malin_drome = 0
    for mot in mots:
        chiffres = ''
        majuscules = ''
        minuscules = ''
        for caractere in mot:
            if caractere in [str(i) for i in range(10)]:
                chiffres += caractere
            elif caractere in [chr(i) for i in range(97, 123)]:
                minuscules += caractere
            elif caractere in [chr(i) for i in range(65, 91)]:
                majuscules += caractere
        if chiffres == ''.join(reversed(chiffres)) and majuscules == ''.join(reversed(majuscules)) and minuscules == ''.join(reversed(minuscules)):
            nb_pas_malin_drome += 1
    return nb_pas_malin_drome


if __name__ == "__main__":
    n = int(input())
    mots = [input() for _ in range(n)]
    print(nb_pas_malin_drome(n, mots))
