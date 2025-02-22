def switch_position(actual_position,ok):
    if actual_position == 'q0':
        if ok == 'a':
            actual_position = 'q1'
    elif actual_position == 'q1':
        if ok == 'b':
            actual_position = 'q2'
    elif actual_position == 'q2':
        if ok == 'c':
            actual_position = 'q3'
    elif actual_position == 'q3':
        print("S-a ajuns la punctul final.")
    return actual_position

def start_model(word: str):
    start_position = 'q0'
    while word:
        print("pozitia actuala e " + start_position)
        ok = word[0]
        start_position = switch_position(start_position, ok)
        word = word[1:]
    print("S-a ajuns la punctul final si starea finala este " + start_position)
    if (start_position == 'q3'):
        print("Cuvantul face parte din limbaj")
    else:
        print("Cuvantul nu face parte din limbaj")


word = input("word: ")
start_model(word)