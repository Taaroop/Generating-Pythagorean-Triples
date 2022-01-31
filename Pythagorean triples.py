
def p_triples(a, b):
    superset = []
    li = []
    for m in range(a, b+1):
        for n in range(a, b+1):
            x = 2*m*n
            y = abs((m**2) - (n**2))
            z = (m**2) + (n**2)
            if z > b:
                return superset
            else:
                li = [x, y, z]

                li = sorted(li)
                if li not in superset and x > 0 and y > 0 and z > 0:
                    superset.append(li)
    return superset
