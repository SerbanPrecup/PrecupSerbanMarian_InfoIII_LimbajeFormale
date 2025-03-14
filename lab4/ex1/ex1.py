def switch_position(vector, actual_position, ok):
    new_positions = []
    if actual_position == 'q0':
        if ok == 'a':
            new_positions.append('q1')
    elif actual_position == 'q1':
        if ok.isspace():
            new_positions.append('q2')
    elif actual_position == 'q2':
        if ok == 'a' or ok == 'b':
            new_positions.append('q3')
        if ok == 'b':
            new_positions.append('q2')
    elif actual_position == 'q3':
        if ok.isspace():
            new_positions.append('q4')
        elif ok == 'b':
            new_positions.append('q1')
    elif actual_position == 'q4':
        print("S-a ajuns la un punct final")


    if not new_positions:
        new_positions.append(actual_position)

    return new_positions


def start_model(word: str):
    vector = ['q0']
    while word:
        print(f"Pozitiile actuale sunt: {vector}")
        ok = word[0]
        new_vector = []

        for actual_position in vector:
            new_vector.extend(switch_position(vector, actual_position, ok))

        vector = new_vector
        word = word[1:]

    print(f"S-a ajuns la final si starile finale sunt: {vector}")


word = input("word: ")
start_model(word)