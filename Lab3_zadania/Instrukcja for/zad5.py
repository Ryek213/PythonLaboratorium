while True:
    n = int(input("Podaj liczbę naturalną: "))

    if n > 0:
        break
    else:
        print("Podana liczba nie jest naturalna")

silnia = 1
for i in range(1, n+1):
    silnia *= i

print(f"Silnia liczby {n} wynosi: {silnia}")
