def switch_position(actual_position, bautura):
    if actual_position == 'q0':
        if bautura == 'C':
            return 'q1'
        elif bautura == 'T':
            return 'q2'
        elif bautura == 'A':
            return 'q3'
        elif bautura == 'H':
            return 'q4'
    elif actual_position in ['q1', 'q2', 'q3','q4']:
        if bautura == 'OK':
            return 'q0'
    return actual_position


def selectare_bautura(bautura):
    position = 'q0'
    position = switch_position(position, bautura)
    print(position)
    ok = str(input("Sunteti sigur? "))
    position = switch_position(position, ok)
    print(position)


word = str(input("Selectati Bautura:\n\tC - cafea\n\tT - ceai\n\tA - cappuccino\n\tH - ciocolata calda\n"))
selectare_bautura(word)
