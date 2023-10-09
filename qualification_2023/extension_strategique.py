import math


def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])


def convex_hull_graham(points):
    stack = []
    P0 = min(points, key=lambda p: (p[1], p[0]))
    points.sort(
        key=lambda p: (math.atan2(p[1] - P0[1], p[0] - P0[0]), p[0] ** 2 + p[1] ** 2)
    )

    for point in points:
        while len(stack) > 1 and ccw(stack[-2], stack[-1], point) <= 0:
            stack.pop()
        stack.append(point)
    return stack


def in_circle(d, point):
    x, y = point
    distance = math.sqrt(x**2 + y**2)
    return distance <= d


def get_all_pairs(points):
    pairs = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            pairs.append((points[i], points[j]))
    return pairs


def est_parallelogramme(A, B, C, D):
    AB = (B[0] - A[0], B[1] - A[1])
    BC = (C[0] - B[0], C[1] - B[1])
    CD = (D[0] - C[0], D[1] - C[1])
    DA = (A[0] - D[0], A[1] - D[1])
    if AB == CD and BC == DA:
        return True
    else:
        return False


def intersection(points):
    pairs = get_all_pairs(points)
    sortie = []
    for i in range(len(pairs)):
        x1, y1 = pairs[i][0]
        x2, y2 = pairs[i][1]
        if x2 - x1 != 0:
            m1 = (y2 - y1) / (x2 - x1)
            b1 = y1 - m1 * x1
        else:
            m1 = None
        for j in range(i + 1, len(pairs)):
            x3, y3 = pairs[j][0]
            x4, y4 = pairs[j][1]
            if x4 - x3 != 0:
                m2 = (y4 - y3) / (x4 - x3)
                b2 = y3 - m2 * x3
            else:
                m2 = None
            if ((m1 == None) and (m2 == None)) or ((m1 == 0) and (m2 == 0)):
                pass
            elif (m1 == None) ^ (m2 == None):
                if m1 == None:
                    sortie.append((x1, m2 * x1 + b2))
                else:
                    sortie.append((x3, m1 * x3 + b1))
            elif not (m1 == 0 and m2 == 0):
                if m1 - m2 == 0:
                    pass
                else:
                    x = (b2 - b1) / (m1 - m2)
                    y = m1 * x + b1
                    sortie.append((x, y))
            elif (m1 == None and m2 == 0) or (m2 == None and m1 == 0):
                if m1 == 0:
                    sortie.append(x3[0], x1[1])
                else:
                    sortie.append(x1[0], x3[1])

    arondi = []
    for i in sortie:
        arondi.append(tuple([round(j, 2) for j in i]))

    return arondi


def nombre_aretes(enveloppe_convexe):
    # breakpoint()
    enveloppe_convexe = [
        enveloppe_convexe[i]
        for i in range(len(enveloppe_convexe))
        if enveloppe_convexe[i] != enveloppe_convexe[i - 1]
    ]
    somets = []
    # breakpoint()
    x1, y1 = enveloppe_convexe[-2]
    x2, y2 = enveloppe_convexe[-1]
    x3, y3 = enveloppe_convexe[0]
    if (y3 - y2) * (x2 - x1) != (y2 - y1) * (x3 - x2):
        somets.append(enveloppe_convexe[-1])
    for point in range(len(enveloppe_convexe) - 1):
        x1, y1 = enveloppe_convexe[point - 1]
        x2, y2 = enveloppe_convexe[point]
        x3, y3 = enveloppe_convexe[point + 1]
        if (y3 - y2) * (x2 - x1) != round((y2 - y1), 2) * (x3 - x2):
            somets.append(enveloppe_convexe[point])
    return len(somets)


def aretes_minimales(d, n, points_de_controles):
    convex = convex_hull_graham(points_de_controles)
    n_convex = len(convex)
    if n_convex <= 3:
        return n_convex

    points_possible = set([i for i in intersection(convex)])
    return min(
        [
            nombre_aretes(convex_hull_graham(convex + [i]))
            for i in points_possible
            if in_circle(d, i) == True
        ]
    )


if __name__ == "__main__":
    d = int(input())
    n = int(input())
    points_de_controles = [tuple(map(int, input().split())) for _ in range(n)]
    n += 1
    points_de_controles.append((0, 0))
    print(aretes_minimales(d, n, points_de_controles))
