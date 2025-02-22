def switch_position(actual_position, ok):
    if actual_position == 'q0':
        if ok == 0:
            actual_position = 'q1'
        else:
            actual_position = 'q2'
    elif actual_position == 'q1':
        if ok == 0:
            actual_position = 'q3'
        else:
            actual_position = 'q0'
    elif actual_position == 'q2':
        if ok == 0:
            actual_position = 'q1'
        else:
            actual_position = 'q3'
    elif actual_position == 'q3':
        print("S-a ajuns la punctul final.")
    return actual_position


def start_model(word: str):
    start_position = 'q0'
    while word:
        print("pozitia actuala e " + start_position)
        ok = word[-1]
        start_position = switch_position(start_position, ok)
        word = word[:-1]
    print("S-a ajuns la punctul final.")


word = input("word: ")
start_model(word)