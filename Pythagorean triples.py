# Function

def p_triples(a):
    superset = []
    li = []
    for m in range(1, a+1):
        for n in range(1, a+1):
            x = 2*m*n
            y = abs((m**2) - (n**2))
            z = (m**2) + (n**2)         # See notes for detailed mathematical explanations and derivation
            if z > a:
                return superset
            else:
                li = [x, y, z]

                li = sorted(li)
                if li not in superset and x > 0 and y > 0 and z > 0:
                    superset.append(li)
    return superset

# Testing

end = int(input("Enter the boundary range of the Pythagorean triples: "))
for item in p_triples(end):
    print(item)
