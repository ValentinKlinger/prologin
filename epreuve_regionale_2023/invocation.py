def invocation(n, mots, m, vocabulaire):
    sortie = []
    for i in mots:
        sortie.append(0)
        for j in vocabulaire:
            if j.removeprefix(i) != j:
                sortie[-1] += m

            elif i.removeprefix(j) != i:
                for k in vocabulaire:
                    if str(j + k + j).removeprefix(i) != str(j + k + j):
                        sortie[-1] += 1

    for i in sortie:
        print(i)


if __name__ == "__main__":
    n = int(input())
    mots = [input() for _ in range(n)]
    m = int(input())
    vocabulaire = [input() for _ in range(m)]
    invocation(n, mots, m, vocabulaire)
