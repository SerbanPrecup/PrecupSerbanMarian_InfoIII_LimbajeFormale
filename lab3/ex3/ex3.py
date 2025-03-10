def switch_position(vector, actual_position, ok):
    if actual_position in vector:
        if actual_position == 'q0':
            if ok == '0':
                vector.append('q1')
                vector.append('q2')
            elif ok == '1':
                vector.append('q1')
                vector.append('q2')
            elif ok == '2':
                vector.append('q2')
        if actual_position == 'q1':
            if ok == '1':
                vector.append('q2')
        if actual_position == 'q2':
            print("S-a ajuns la un punct final")

def start_model(word: str):
    vector = ['q0']
    while word:
        print(f"pozitiile actuale sunt:{vector}")
        ok = word[0]
        switch_position(vector , 'q0' , ok)
        word = word[1:]
    print(f"S-a ajuns la final si starile finale sunt:{vector} ")


word = input("word: ")
start_model(word)
