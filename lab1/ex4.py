from collections import deque


def S_func(s: str) -> str:
    return s.replace('S', 'AB', 1)


def A_func(s: str, ok: bool) -> str:
    if ok:
        return s.replace('A', 'aA', 1)
    return s.replace('A', '', 1)


def B_func(s: str, ok: bool) -> str:
    if ok:
        return s.replace('B', 'bB', 1)
    return s.replace('B', '', 1)


def generare_cuvinte(n):
    rez = []
    q = deque()
    q.append(("", False))

    while q and len(rez) < n:
        s, has_b = q.popleft()
        rez.append(s)

        if not has_b:
            q.append((s + "a", False))
        q.append((s + "b", True))

    return rez


iteratii = int(input("iteratii: "))
cuv = generare_cuvinte(iteratii)

output = []
for w in cuv:
    if w == "":
        output.append("epsilon (sirul vid)")
    else:
        output.append(w)

print(" ".join(output))