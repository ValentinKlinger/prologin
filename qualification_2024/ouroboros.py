class Cellule:
    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s


class Liste:
    def __init__(self):
        self.tete = None

    def est_vide(self):
        return self.tete is None

    def ajoute(self, x):
        self.tete = Cellule(x, self.tete)

    def cracher(self):
        if self.tete is not None:
            ville = self.tete.valeur
            self.tete = self.tete.suivante
            return ville


def situation_finale(n: int, m: int, villes: list[str], actions: list[str]):
    """
    :param n: le nombre de villes autour de Midgard
    :param m: le nombre d'années avant le Ragnarök
    :param villes: le nom des villes autour de Midgard, en partant de la queue de Jörmungandr

    :param actions: la liste des actions prochaines de Jörmungandr

    >>> situation_finale(4, 2, ['Rostheim', 'Adaheim','Pascalheim','Fortrheim'], ['A', 'A'])
    ['Pascalheim', 'Fortrheim', 'Rostheim', 'Adaheim']
    >>> situation_finale(4, 4, ['Rostheim', 'Adaheim','Pascalheim','Fortrheim'], ['A', 'M', 'A', 'C'])
    ['Adaheim', 'Fortrheim', 'Rostheim', 'Pascalheim']
    >>> situation_finale(4, 1, ['Rostheim', 'Adaheim','Pascalheim','Fortrheim'], ['R'])
    ['Fortrheim', 'Pascalheim', 'Adaheim', 'Rostheim']
    >>> situation_finale(4, 5, ['Rostheim', 'Adaheim','Pascalheim','Fortrheim'], ['A', 'M', 'R', 'A', 'C'])
    ['Adaheim', 'Fortrheim', 'Pascalheim', 'Rostheim']
    >>> situation_finale(6, 6,
    ... ['Nixheim', 'Haskelheim', 'Cobolheim', 'Prologheim', 'Delpheim', 'Modulheim'], ['M', 'M', 'A', 'A', 'C', 'C'])
    ['Nixheim', 'Haskelheim', 'Delpheim', 'Modulheim', 'Cobolheim', 'Prologheim']
    >>> situation_finale(2, 2, ['Lispheim', 'Erlangheim'], ['R', 'M'])
    ['Lispheim']
    >>> situation_finale(2, 3, ['Lispheim', 'Erlangheim'], ['R', 'M', 'M'])
    []
    >>> situation_finale(2, 2, ['A', 'B'], ['R', 'C'])
    ['B', 'A']
    >>> situation_finale(2, 4, ['A', 'B'], ['R', 'R', 'R', 'R'])
    ['A', 'B']
    >>> situation_finale(3, 9, ['A', 'B', 'C'], ['R', 'A', 'A', 'A', 'A', 'M', 'R', 'C', 'R'])
    ['A', 'C', 'B']
    >>> situation_finale(3, 6, ['A', 'B', 'C'], ['R', 'A', 'A', 'A', 'A', 'M'])
    ['A', 'C']
    >>> situation_finale(3, 3, ['A', 'B', 'C'], ['R', 'A', 'M'])
    ['A', 'C']
    >>> situation_finale(1, 3, ['A'], ['M', 'C', 'C'])
    ['A']
    >>> situation_finale(1, 3, ['A'], ['M', 'M', 'C'])
    ['A']
    >>> situation_finale(6, 4, ['A', 'B', 'C', 'D', 'E', 'F'],
    ... ['A', 'A', 'R', 'M'])
    ['A', 'F', 'E', 'D', 'C']
    >>> situation_finale(6, _, ['A', 'B', 'C', 'D', 'E', 'F'],
    ... ['A', 'A', 'R', 'M', 'A', 'A', 'A', 'M'])
    ['C', 'A', 'F', 'E']
    >>> situation_finale(6, _, ['A', 'B', 'C', 'D', 'E', 'F'],
    ... ['A', 'A', 'R', 'M', 'A', 'A', 'A', 'M', 'R', 'A', 'A'])
    ['A', 'C', 'E', 'F']
    >>> situation_finale(6, _, ['A', 'B', 'C', 'D', 'E', 'F'],
    ... ['A', 'A', 'R', 'M', 'A', 'A', 'A', 'M', 'R', 'A', 'A', 'C'])
    ['D', 'A', 'C', 'E', 'F']
    >>> situation_finale(6, 16, ['A', 'B', 'C', 'D', 'E', 'F'],
    ... ['A', 'A', 'R', 'M', 'A', 'A', 'A', 'M', 'R', 'A', 'A', 'C', 'R', 'A', 'A', 'C'])
    ['B', 'C', 'A', 'D', 'F', 'E']
    >>> situation_finale(6, 16, ['A', 'B', 'C', 'D', 'E', 'F'],
    ... ['A', 'A', 'R', 'M', 'M', 'R', 'A', 'A', 'R', 'C', 'R', 'A', 'A', 'A', 'A', 'C'])
    ['B', 'A', 'E', 'F', 'C', 'D']
    >>> situation_finale(4, 17, ['A', 'B', 'C', 'D'],
    ... ['R', 'A', 'A', 'A', 'A', 'A', 'M', 'R', 'A', 'A', 'A', 'A', 'A', 'C', 'R', 'A', 'R'])
    ['A', 'C', 'B', 'D']
    >>> situation_finale(6, 7, ['A', 'B', 'C', 'D', 'E', 'F'],
    ... ['C', 'C', 'R', 'M', 'A', 'R', 'C'])
    ['F', 'E', 'A', 'B', 'C', 'D']
    """
    ventre = Liste()
    for action in actions:
        if action == "A":
            villes = villes[1:] + [villes[0]]
        elif action == "R":
            villes.reverse()
        elif action == "M" and len(villes) >= 1:
            ventre.ajoute(villes[0])
            villes = villes[1:]
        elif action == "C" and ventre.est_vide() is False:
            villes = [ventre.cracher()] + villes
    return villes


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    villes = [input() for _ in range(n)]
    actions = list(input())
    for ville in situation_finale(n, m, villes, actions):
        print(ville)
