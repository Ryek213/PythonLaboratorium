import random

while True:
    n = int(input("Podaj długość listy: "))
    if n < 0:
        print("Długość listy powinna być nie mniejsza niż 0!!")
    else:
        break

while True:
    x = int(input("Podaj maksymalną liczbę znaków elementu: "))
    if x < 1:
        print("Liczba znaków musi być nie mniejsza niż 1!!")
    else:
        break

lista = []

for i in range(n):
    rand = random.randint(1, x)
    pom = ""

    for k in range(rand):
        pom += chr(random.randint(ord("a"), ord("z")))

    lista.append(pom)

krotka = tuple(lista)
print(krotka)

while True:
    cw = input("Wybierz ćwiczenie [a, b, c, d]: ")
    match cw:
        case "a":
            s = 0
            for i in krotka:
                s += len(i)
            print(f"Liczba znaków w liście: {s}")

        case "b":
            s = 0
            for i in krotka:
                for k in i:
                    if k == "k":
                        s += 1
            print(f'Liczba liter "k" w liście: {s}')

        case "c":
            s = 0
            for i in krotka:
                if i.find("kt") != -1:
                    s += 1
            print(f'Liczba wystąpień ciągu "kt" w liście: {s}')

        case "d":
            while True:
                s = int(input("Podaj długość szukanych ciągów: "))
                if s < 0:
                    print(f"Szukana długość powinna być nie mniejsza niż 0!!")
                else:
                    break
            z = 0
            for i in krotka:
                if len(i) > s:
                    z += 1
            print(f"Liczba ciągów znaków dłuższych niż ({s}): {z}")

        case _:
            break
