def reuniune(L1, L2):
    return list(set(L1) | set(L2))


def intersectie(L1, L2):
    return list(set(L1) & set(L2))


def reverse(L):
    return list(reversed(L))


def concatenare(L1, L2):
    return [x + y for x in L1 for y in L2]


def update_vector_seturi(vector_seturi):
    while True:
        simbol_vechi = str(input("\nSimbol vechi: "))
        if simbol_vechi == "":
            break
        simbol_nou = str(input("Simbol nou: "))
        vector_seturi.append({simbol_vechi, simbol_nou})


def homomorfism(L):
    vector_seturi = []
    update_vector_seturi(vector_seturi)

    for set_elem in vector_seturi:
        simbol_vechi, simbol_nou = list(set_elem)
        for i in range(len(L)):
            L[i] = L[i].replace(simbol_vechi, simbol_nou)

    return L

L1 = []
L2 = []

print("Limbajul L1:")
while True:
    word = str(input())
    if word == "":
        break
    else:
        L1.append(word)

print("Limbajul L2:")
while True:
    word = str(input())
    if word == "":
        break
    else:
        L2.append(word)

while True:
    print("\nOperatii:")
    print("1 - Reuniune")
    print("2 - Intersectie")
    print("3 - Reverse L1")
    print("4 - Reverse L2")
    print("5 - Concatenare")
    print("6 - homomorfism L1")
    print("7 - homomorfism L2")

    optiune = int(input("Optiune: "))
    match optiune:
        case 1:
            print(reuniune(L1, L2))
        case 2:
            print(intersectie(L1, L2))
        case 3:
            print(reverse(L1))
        case 4:
            print(reverse(L2))
        case 5:
            print(concatenare(L1, L2))
        case 6:
            print(homomorfism(L1))
        case 7:
            print(homomorfism(L2))
        case default:
            print("Alege o optiune valida.")
            break
