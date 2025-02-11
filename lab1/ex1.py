A = ['a','b','c']
B = ['x','y','z']
C = ['1','2','3']

def concatenate(s1,s2):
    return s1+s2

def invers(s):
    return s[::-1]

def substitute(s,a,b):
    return s.replace(a,b)

def lungime(s):
    return len(s)

cuv1="abc"

cuv2="yxz xx"

cuv3="3213 123"

print(concatenate(cuv2,cuv3))

print(invers(cuv3))

print(substitute(cuv2,'x','a'))

print(lungime(cuv3))