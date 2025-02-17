A = ['a','b','c']
B = ['x','y','z']
C = ['1','2','3']

def concat(s1: str, s2: str) -> str:
    return s1+s2

def invers(s: str) -> str:
    return s[::-1]

def substitute(s: str,a: str,b: str) -> str:
    return s.replace(a,b)

def lungime(s: str) -> int:
    return len(s)

cuv1="abc"

cuv2="yxzxx"

cuv3="3213s123"

print(concat(cuv2,cuv3))

print(invers(cuv3))

print(substitute(cuv2,'x','a'))

print(lungime(cuv3))