alf1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alf2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
alf3 = ['x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4', 'x5', 'y5']


def concat(s1: str, s2: str) -> str:
    return s1 + s2


def repeat(s: str, n: int) -> str:
    return s * n


def reverse(s: str) -> str:
    return s[::-1]


def extract(s: str, i: int, j: int) -> str:
    return s[i:j+1]

def replace(s: str, sub: str, new_sub: str) -> str:
    return s.replace(sub, new_sub, 1)

def apply_operations(word: str):
    print(f"Cuvânt inițial: {word}")
    print(f"Concatenare cu 'ABC': {concat(word, 'ABC')}")
    print(f"Repetare de 2 ori: {repeat(word, 2)}")
    print(f"Inversare: {reverse(word)}")
    print(f"Extracție (2, 5): {extract(word, 2, 5)}")
    print(f"Înlocuire 'A' cu 'Z': {replace(word, 'A', 'Z')}")

apply_operations("A1b2x3")
