def batiments(n: int, r: int, k: int, villes: list[int]) -> list[int]:
    """
    :param n: le nombre de villes
    :param r: le nombre de mouvements du serpent
    :param k: le nombre de villes impliquées dans chaque mouvement
    :param villes: le nombre de bâtiments cassés dans chaque ville

    >>> batiments(5, 2, 3, [2, 4, 3, 6, 8])
    [4, 6, 3, 6, 8]
    >>> batiments(5, 2, 4, [2, 4, 3, 6, 8])
    [6, 8, 3, 6, 8]
    >>> batiments(5, 6, 3, [5, 4, 3, 2, 1])
    [5, 4, 3, 5, 5]
    >>> batiments(10, 6, 3,
    ... [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [3, 4, 5, 6, 7, 8, 7, 8, 9, 10]
    >>> batiments(20, 42, 3,
    ... [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    [7, 8, 7, 8, 9, 10, 10, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 4, 5, 6]
    """
    nb_bat_derniere_ville = villes[0]
    villes[0] = max([villes[i % n] for i in range(k)])
    if r > n:
        for mouv in range(1, n):
            if nb_bat_derniere_ville == villes[mouv - 1]:
                nb_bat_derniere_ville = villes[mouv]
                villes[mouv] = max([villes[(mouv + i) % n] for i in range(k)])
            else:
                nb_bat_derniere_ville = villes[mouv]
                villes[mouv] = max(villes[mouv - 1], villes[(mouv + k - 1) % n])

        for mouv in range(r - n):
            villes[mouv % n] = max(villes[mouv % n], villes[(mouv + k - 1) % n])

    else:
        for mouv in range(1, r):
            if nb_bat_derniere_ville == villes[mouv - 1]:
                nb_bat_derniere_ville = villes[mouv]
                villes[mouv] = max([villes[(mouv + i) % n] for i in range(k)])
            else:
                nb_bat_derniere_ville = villes[mouv]
                villes[mouv] = max(villes[mouv - 1], villes[(mouv + k - 1) % n])
    return villes


if __name__ == "__main__":
    n = int(input())
    r = int(input())
    k = int(input())
    villes = list(map(int, input().split()))
    bat = batiments(n, r, k, villes)
    for i in range(n - 1):
        print(bat[i], end=" ")
    print(bat[-1])
