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

    positions_initiales = {}
    for idx_personne in range(len(tailles)):
        if tailles[idx_personne] in positions_initiales:
            positions_initiales[tailles[idx_personne]].append(idx_personne)
        else:
            positions_initiales[tailles[idx_personne]] = [idx_personne]

    for rang_personne in range(len(ordre_final)):
        for position_possible in range(
            len(positions_initiales[ordre_final[rang_personne]])
        ):
            if (
                (
                    rang_personne
                    - positions_initiales[ordre_final[rang_personne]][position_possible]
                )
                / k
            ).is_integer():
                positions_initiales[ordre_final[rang_personne]].pop(position_possible)
                break
        else:
            return "NON"
    return "OUI"


if __name__ == "__main__":
    k = int(input())
    n = int(input())
    tailles = list(map(int, input().split()))
    print(ordre(k, n, tailles))
