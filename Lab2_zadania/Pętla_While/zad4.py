pocz = int(input("Podaj pierwszą liczbę zakesu: "))
kon = int(input("Podaj ostatnią liczbę zakresu: "))

if pocz > kon:
    pom = pocz
    pocz = kon
    kon = pom

while pocz <= kon:
    if pocz % 2 == 0:
        print(pocz)
        pocz += 1
    else:
        pocz += 1
        continue

print("Koniec!")
