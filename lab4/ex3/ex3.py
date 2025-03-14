def switch_position(stare, input):
    if stare == 'q1':
        if input == 'X':
            stare = 'q2'
        print("O1")
    elif stare == 'q2':
        if input == 'X':
            stare = 'q1'
        print("O2")
    return stare



def start_model(word: str):
    stare = 'q1'
    while word:
        print("pozitia actuala e " + stare)
        ok = word[0]
        stare = switch_position(stare, ok)
        word = word[1:]
    print("S-a ajuns la punctul final si starea finala este " + stare)


word = input("word: ")
start_model(word)