from itertools import product


E = ['0','1','2']
def is_pal(s):
    return s == s[::-1]

def generate_pal(alf, max_length):
    for length in range(1, max_length + 1):
        print(f"Palindroame de lungime {length}:")
        palindromes = ["".join(p) for p in product(alf, repeat=length) if is_pal("".join(p))]
        print(" ".join(palindromes), "\n")

generate_pal(E, 5)