def switch_position(vector, actual_position, ok):
    new_positions = []

    if actual_position == 'q0':
        if ok.isspace():
            new_positions.extend(['q1', 'q13'])
    elif actual_position == 'q1':
        if ok.isspace():
            new_positions.extend(['q2', 'q4'])
    elif actual_position == 'q2':
        if ok == 'a':
            new_positions.append('q3')
    elif actual_position == 'q3':
        if ok.isspace():
            new_positions.append('q6')
    elif actual_position == 'q4':
        if ok == 'b':
            new_positions.append('q5')
    elif actual_position == 'q5':
        if ok.isspace():
            new_positions.append('q6')
    elif actual_position == 'q6':
        if ok.isspace():
            new_positions.extend(['q7', 'q12'])
    elif actual_position == 'q7':
        if ok.isspace():
            new_positions.extend(['q8', 'q10'])
    elif actual_position == 'q8':
        if ok == 'a':
            new_positions.append('q9')
    elif actual_position == 'q9':
        if ok.isspace():
            new_positions.append('q12')
    elif actual_position == 'q10':
        if ok == 'b':
            new_positions.append('q11')
    elif actual_position == 'q11':
        if ok.isspace():
            new_positions.append('q12')
    elif actual_position == 'q12':
        if ok.isspace():
            new_positions.extend(['q7', 'q15'])
    elif actual_position == 'q13':
        if ok == 'a':
            new_positions.append('q14')
    elif actual_position == 'q14':
        if ok.isspace():
            new_positions.append('q15')
    elif actual_position == 'q15':
        if ok.isspace():
            new_positions.append('qF')

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
