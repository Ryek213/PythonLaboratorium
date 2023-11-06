pocz = int(input("Podaj pierwszą liczbę zakesu: "))
kon = int(input("Podaj ostatnią liczbę zakresu: "))

if pocz > kon:
    pom = pocz
    pocz = kon
    kon = pom

while (pocz <= kon):
    print(pocz)
    pocz += 1
print("Koniec!")