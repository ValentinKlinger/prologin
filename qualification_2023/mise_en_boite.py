def mise_en_boite(restes, boites):
    max_restes = 0
    to_rm = []
    for boite in boites:

        for r in to_rm:
            print(to_rm)
            restes.pop(r)
            to_rm = []

        for reste in range(len(restes)):

            if boite >= restes[reste]:
                max_restes += 1
                to_rm.insert(0, reste)
                break
            to_rm.insert(0, reste)
    return max_restes


n = int(input())
restes = sorted(list(map(int, input().split())), reverse=True)
boites = sorted(list(map(int, input().split())), reverse=True)
print(mise_en_boite(restes, boites))
