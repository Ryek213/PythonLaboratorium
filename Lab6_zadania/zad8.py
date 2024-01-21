import math


def pole_trojkata(x, y, kat):
    if kat >= 90:
        print("Trójkąt nie jest ostrokątny")
        return
    elif kat <= 0 or x <= 0 or y <= 0:
        print("Trójkąt nie istnieje")
        return

    return round((x * y * math.sin(math.radians(kat)))/2, 8)


a = float(input("Podaj długość pierwszego boku: "))
b = float(input("Podaj długość drugiego boku: "))
alfa = float(input("Podaj szerokość kąta pomiędzy nimi: "))

print(f"Pole trójkąta wynosi: {pole_trojkata(a, b, alfa)}")
