def phibonacci(n, x):
    xa = x
    while len(xa) > 2:
        xa[-2] += xa[-1]
        xa[-3] += xa[-1]
        xa.pop(-1)
    sortie = ""
    for i in range(len(xa)):
        sortie += str(xa[i] % 1000000007) + " "
    return sortie[:-1]


if __name__ == "__main__":
    n = int(input())
    x = list(map(int, input().split()))
    print(phibonacci(n, x))
