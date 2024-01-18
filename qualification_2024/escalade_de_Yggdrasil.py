def le_plus_grand_saut(n: int, differences: list[int]) -> int:
    """
    :param n: le nombre de branches de l'arbre moins 1
    :param differences: la liste des différences en hauteur des branches consécutives

    >>> le_plus_grand_saut(4, [3, 2, -5, 4])
    3
    >>> le_plus_grand_saut(7, [2, 9, 18, 12, 9, 19, 1])
    19
    >>> le_plus_grand_saut(6, [1, 6, -7, 9, 10, -15])
    10
    >>> le_plus_grand_saut(4, [-2, -9, 10, -3])
    0
    >>> le_plus_grand_saut(1, [2])
    2
    >>> le_plus_grand_saut(4, [2, 9, -15, 30])
    30
    """
    hauteurs = [1]
    for difference in range(len(differences)):
        hauteurs.append(hauteurs[difference] + differences[difference])

    plus_haute_branche = hauteurs.index(max(hauteurs))

    if plus_haute_branche == 0:
        return 0
    return max(differences[: plus_haute_branche + 1])


if __name__ == "__main__":
    n = int(input())
    differences = list(map(int, input().split()))
    print(le_plus_grand_saut(n, differences))
