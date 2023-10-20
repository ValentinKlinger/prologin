def attente_minimale(n, charges):
    before = 0
    sortie = 0
    for i in range(1, n):
        sortie += charges[i - 1]
        before += sortie
    return before


if __name__ == "__main__":
    n = int(input())
    charges = sorted(list(map(int, input().split())))
    print(attente_minimale(n, charges))
