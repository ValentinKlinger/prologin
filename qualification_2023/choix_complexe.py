def nombre_films(adore, deteste):
    uniquement_adore = 0
    for film in adore:
        if film not in deteste:
            uniquement_adore += 1
    return uniquement_adore


if __name__ == "__main__":
    adore = set([input() for _ in range(6)])
    deteste = set([input() for _ in range(6)])
    nombre_films(adore, deteste)
