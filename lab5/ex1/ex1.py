def switch_position(stare, pereche):
    if stare == 'S0':
        if pereche[0] == 0 and pereche[1] == 0:
            print(0)
        elif pereche[0] == 0 and pereche[1] == 1:
            stare = 'S1'
            print(1)
        elif pereche[0] == 1 and pereche[1] == 0:
            print(0)
        elif pereche[0] == 1 and pereche[1] == 1:
            stare = 'S1'
            print(1)
    elif stare == 'S1':
        if pereche[0] == 0 and pereche[1] == 0:
            print(1)
        elif pereche[0] == 0 and pereche[1] == 1:
            print(1)
        elif pereche[0] == 1 and pereche[1] == 0:
            stare = 'S0'
            print(0)
        elif pereche[0] == 1 and pereche[1] == 1:
            stare = 'S0'
            print(0)
    return stare



def start_model():
    stare = 'S0'
    while True:
        sem1 = int(input("stare semafor 1:"))
        sem2 = int(input("stare semafor 2:"))

        sem = [sem1, sem2]
        stare = switch_position(stare,sem)
        print(stare)


start_model()