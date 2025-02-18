from itertools import product


E = ['0','1','2']
def is_pal(s):
    return s == s[::-1]

def generate_pal(alfabet, max_length):
    for length in range(1, max_length + 1):
        print(f"Palindroame de lungime {length}:")
        palindromes = []
        for p in product(alfabet, repeat=length):
            word = "".join(p)  # trasf in sir
            if is_pal(word):
                palindromes.append(word)
        print(" ".join(palindromes), "\n")

generate_pal(E, 5)