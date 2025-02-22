import re


def read_file():
    path = input("path: ")
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        print("File not found")
        exit(1)


def verificare(linii):
    pattern_client = r"^Client: [A-Za-z]+ [A-Za-z]+$"
    pattern_data = r"^Data: \d{2}-\d{2}-\d{4}$"
    pattern_produs = r"^Produs: .+, Cantitate: \d+, Pret: \d+\.\d{2}, TVA: \d+%$"

    erori = 0

    if not re.match(pattern_client, linii[0].strip()):
        erori += 1
    if not re.match(pattern_data, linii[1].strip()):
        erori += 1
    for i, linie in enumerate(linii[2:]):
        if not re.match(pattern_produs, linie.strip()):
            erori += 1

    return erori

linii = read_file()

erori = verificare(linii)
if erori == 0:
    print("Formatul facturii este corect")
else:
    print("Formatul facturii nu este corect")