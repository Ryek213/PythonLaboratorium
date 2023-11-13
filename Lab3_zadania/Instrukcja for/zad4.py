while True:
    n = int(input("Podaj liczbę kolejnych liczb ciągu arytmetycznego: "))

    if n > 0:
        break
    else:
        print("Nie podano liczby naturalnej")

a = int(input("Podaj a: "))
r = int(input("Podaj różnicę r: "))

print(f"Kolejne {n} liczb ciągu arytmetycznego {a} + n*{r}")
for i in range(n):
    print(f"{i}: {a + i*r}")
