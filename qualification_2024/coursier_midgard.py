from random import shuffle
from sys import setrecursionlimit

setrecursionlimit(10**9)


def afficher_chemin(n: int, dieux: list[list[str]]) -> None:
    """
    :param n: le nombre de dieux
    :param dieux: liste des prénoms et noms des dieux séparés par un espace

    >>> afficher_chemin(1, [['A', 'B']])
    [['A', 'B']]
    >>> afficher_chemin(14, [['A', 'B'], ['A', 'C'], ['E', 'C'], ['E', 'F'],
    ... ['J', 'F'], ['J', 'R'], ['D', 'R'], ['D', 'M'], ['E', 'M'], ['E', 'B'],
    ... ['X', 'Y'], ['X', 'Z'], ['Q', 'Z'], ['Q', 'Y']])
    'IMPOSSIBLE'
    >>> afficher_chemin(10, [['A', 'B'], ['A', 'C'], ['E', 'C'], ['E', 'F'],
    ... ['J', 'F'], ['J', 'R'], ['D', 'R'], ['D', 'M'], ['E', 'M'], ['E', 'B']])
    [['A', 'B'], ['A', 'C'], ['E', 'C'], ['E', 'F'], ['J', 'F'], ['J', 'R'], ['D', 'R'], ['D', 'M'], ['E', 'M'], ['E', 'B']]
    >>> afficher_chemin(7, [['A', 'B'], ['A', 'C'], ['E', 'C'], ['E', 'B'],
    ... ['E', 'D'], ['N', 'D'], ['N', 'B']])
    [['E', 'C'], ['A', 'C'], ['A', 'B'], ['E', 'B'], ['E', 'D'], ['N', 'D'], ['N', 'B']]
    >>> afficher_chemin(3, [['Alof', 'Amno'], ['Baikik', 'Brok'], ['Alof', 'Brok']])
    [['Baikik', 'Brok'], ['Alof', 'Brok'], ['Alof', 'Amno']]
    >>> afficher_chemin(5, [['0dric', 'Apik'], ['0dric', 'Brik'],
    ... ['1dric', 'Apik'], ['1dric', 'Brik'], ['Tonb', 'Apik']])
    [['Tonb', 'Apik'], ['0dric', 'Apik'], ['0dric', 'Brik'], ['1dric', 'Brik'], ['1dric', 'Apik']]
    >>> afficher_chemin(3, [['Seche', 'Plusplus'], ['Seche', 'Seche'], ['Seche', 'Harpe']])
    'IMPOSSIBLE'
    """
    # TODO S'il n'existe aucun chemin qui permette de faire passer le message
    # par tous les dieux en respectant le protocole HTTP, afficher sur une
    # ligne le message `IMPOSSIBLE`. Sinon, afficher, sur une ligne par dieu et
    # dans l'ordre désiré, les noms complets des dieux par lesquels le message
    # doit passer. Si plusieurs solutions existent, afficher n'importe laquelle
    # d'entre elles.

    def find_way_dfs(prenoms, noms, start, current_path=None, nom_ou_prenom=0):
        if current_path is None:
            current_path = []

        current_path.append(start)

        if nom_ou_prenom == 0:
            for neighbor in prenoms[start[0]]:
                if neighbor not in current_path:
                    new_path = find_way_dfs(
                        prenoms, noms, neighbor, current_path.copy(), 1
                    )
                    # print(new_path, len(new_path), n)
                    if len(new_path) == n:
                        return new_path

        else:
            for neighbor in noms[start[1]]:
                if neighbor not in current_path:
                    new_path = find_way_dfs(
                        prenoms, noms, neighbor, current_path.copy(), 0
                    )
                    # print(new_path, len(new_path), n)
                    if len(new_path) == n:
                        return new_path

        return current_path

    prenoms: dict[str, list[list[str, str]]] = dict()
    noms: dict[str, list[list[str, str]]] = dict()

    for dieu in dieux:  # Create the dicts.
        if dieu[0] in prenoms:
            prenoms[dieu[0]].append(dieu)
        else:
            prenoms[dieu[0]]: list[list[str, str]] = [dieu]

        if dieu[1] in noms:
            noms[dieu[1]].append(dieu)
        else:
            noms[dieu[1]]: list[list[str, str]] = [dieu]

    prenoms_impaires: list[str] = [
        prenoms[prenom][0][0]
        for prenom in prenoms.keys()
        if len(prenoms[prenom]) % 2 == 1
    ]
    noms_impaires: list[str] = [
        noms[nom][0][1] for nom in noms.keys() if len(noms[nom]) % 2 == 1
    ]

    tot_impaires: int = len(prenoms_impaires) + len(noms_impaires)

    if n == 1:
        return dieux

    if tot_impaires != 0 and tot_impaires != 2:
        return "IMPOSSIBLE"

    if tot_impaires == 0:
        parcours = find_way_dfs(
            prenoms, noms, dieux[0], current_path=None, nom_ou_prenom=0
        )
        if len(parcours) == n:
            return parcours

        return "IMPOSSIBLE"

    if tot_impaires == 2:
        if len(prenoms_impaires) != 0:
            dieu_depart = prenoms[prenoms_impaires[0]][0]
            parcours = find_way_dfs(
                prenoms, noms, dieu_depart, current_path=None, nom_ou_prenom=1
            )
            if len(parcours) == n:
                return parcours
            return "IMPOSSIBLE"
        if len(noms_impaires) != 0:
            dieu_depart = noms[noms_impaires[0]][0]
            parcours = find_way_dfs(
                prenoms, noms, dieu_depart, current_path=None, nom_ou_prenom=0
            )
            if len(parcours) == n:
                return parcours
            return "IMPOSSIBLE"


if __name__ == "__main__":
    n = int(input())
    dieux = [input() for _ in range(n)]
    shuffle(dieux)
    for idx_dieu in range(n):
        dieux[idx_dieu] = dieux[idx_dieu].split(" ")

    path = afficher_chemin(n, dieux)
    if path == "IMPOSSIBLE":
        print("IMPOSSIBLE")
    else:
        for dieu in path:
            print(dieu[0], dieu[1])
