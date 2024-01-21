import random
import math


def losuj_elementy(m, n, ile):
    if m > n:
        pom = m
        m = n
        n = pom

    elementy = list()
    for i in range(ile):
        elementy.append(random.randint(m, n))

    return tuple(elementy)


def srednia_geometryczna(krotka):
    wynik = 1
    for i in krotka:
        wynik = wynik * i

    if wynik < 0:
        print("Nie można obliczyć średniej geometrycznej z liczby ujemnej")
        return

    return math.pow(wynik, 1 / len(krotka))


a = int(input("Podaj początek przedziału: "))
b = int(input("Podaj koniec przedziału: "))

elem = losuj_elementy(a, b, 10)

print(f"Elementy krotki: {', '.join(map(str, elem))}")
print(f"Średnia geometryczna: {srednia_geometryczna(elem)}")
