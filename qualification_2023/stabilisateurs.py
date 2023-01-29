def stabilite_maximale(n, k, p, accroches):

    if k == 0 or n < 4:
        return 0

    ecart4 = []

    for i in range(n - 3):
        ecart4.append(p - (accroches[i + 3] - accroches[i]) ** 2) 

    couple_de_1 = max(ecart4)

    if k >= 2 and n >= 8:
        couple_de_2 = []
        lst = ecart4[0: n - 7]
        lst1 = ecart4[4: n - 3]

        for i in lst:
            for j in lst1:
                couple_de_2.append(i + j)
            lst1.pop(0)
        couple_de_2 = max(couple_de_2)
    else:
        couple_de_2 = 0
    
    if k == 1 or n < 8:
        return max(couple_de_1, 0)
    elif k >= 3 and n == 12:
        return max(couple_de_1, couple_de_2, ecart4[0] + ecart4[4] + ecart4[8], 0)
    elif k >= 2 or n < 12:
        return max(couple_de_1, couple_de_2, 0)



if __name__ == "__main__":
    n = int(input())
    k = int(input())
    p = int(input())
    accroches = sorted(list(map(int, input().split())))
    print(stabilite_maximale(n, k, p, accroches))
