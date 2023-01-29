def trajets_retour(n, redirection):

    sortie = ''
    trajet = []
    for s in range(n):
        continuer = True
        val = s
        for i in range(s):
            print(trajet)
            if redirection[val] == trajet[i][0]:
                try:
                    min(trajet.index(val))
                    trajet.append([[val] + trajet[i][0], min(trajet.index(val), trajet[i][1])])
 
                except ValueError:
                    trajet.append([[val] + trajet[i][0], trajet[i][1]])
                continuer = False
                sortie += ' ' + str(trajet[i][1])
                break
        
        if continuer == True:
            trajet.append([[]])
            
            while val not in trajet[-1][0]:
                trajet[-1][0].append(val)
                val = redirection[val]
            trajet[-1][0].append(val)
            trajet[-1].append(len(trajet[-1][0]) - 1)
            sortie += ' ' + str(trajet[-1][1])

    sortie = sortie[1:]
    return sortie


if __name__ == "__main__":
    n = int(input())
    redirection = list(map(lambda x: int(x) - 1, input().split()))
    print(trajets_retour(n, redirection))



'''def trajets_retour(n, redirection):
    sortie = ''
    trajet = []
    for s in range(1, n + 1):
        continuer = True
        val = s
        for i in range(s - 1): # vérifie si le 2eme terme est dans les trajet
            if redirection[val - 1] == trajet[i][0]:
                try:
                    min(trajet.index(val - 1))
                    trajet.append([[val - 1] + trajet[i][0], min(trajet.index(val - 1), trajet[i][1])])
 
                except ValueError:
                    trajet.append([[val - 1] + trajet[i][0], trajet[i][1]])
                continuer = False
                sortie += ' ' + str(trajet[i][1])
                break
        
        if continuer == True:
            trajet.append([[]])
            
            while val not in trajet[-1][0]:
                trajet[-1][0].append(val)
                val = redirection[val - 1]
            trajet[-1].append(val)
            sortie += ' ' + str(len(trajet[-1]) - 1)
    #print(trajet)
    sortie = sortie[1:]
    return sortie


if __name__ == "__main__":
    n = int(input())
    redirection = list(map(int, input().split()))
    print(trajets_retour(n, redirection))'''
