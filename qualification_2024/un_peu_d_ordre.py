def ordre(k: int, n: int, tailles: list[int]):
    """
    :param k: le nombre magique
    :param n: le nombre de personnes
    :param tailles: la liste des tailles de chaque personne
    >>> ordre(1, 5, [5, 4, 3, 2, 1])
    'OUI'
    >>> ordre(2, 5, [5, 4, 3, 2, 1])
    'OUI'
    >>> ordre(3, 5, [5, 4, 3, 2, 1])
    'NON'
    >>> ordre(3, 5, [4, 5, 3, 1, 2])
    'OUI'
    >>> ordre(2, 6, [1, 3, 5, 2, 4, 2])
    'NON'
    >>> ordre(2, 6, [1, 3, 4, 2, 2, 5])
    'OUI'
    >>> ordre(4, 4, [1, 2, 2, 4])
    'OUI'
    """
    ordre_final = sorted(tailles)
    for personne in range(len(tailles)):
        positions_final_possibles = [index for index, valeur in enumerate(ordre_final) if valeur == tailles[personne]]
        for position_possible in positions_final_possibles:
            if ((personne - position_possible) / k).is_integer():
                ordre_final[position_possible] = -1
                break
        else: 
            return 'NON'
    return 'OUI'


if __name__ == "__main__":
    k = int(input())
    n = int(input())
    tailles = list(map(int, input().split()))
    print(ordre(k, n, tailles))