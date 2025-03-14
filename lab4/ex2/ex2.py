def switch_position(actual_position, ok):
    if ok == 'A':
        actual_position = 'S1'
        print('O1')
    elif ok == 'B':
        actual_position = 'S2'
        print('O2')

    return actual_position



def start_model(word: str):
    start_position = 'S1'
    while word:
        print("pozitia actuala e " + start_position)
        ok = word[0]
        start_position = switch_position(start_position, ok)
        word = word[1:]
    print("S-a ajuns la punctul final si starea finala este " + start_position)


word = input("word: ")
start_model(word)