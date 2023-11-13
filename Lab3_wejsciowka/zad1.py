a = int(input("Podaj pierwszą liczbę zakresu: "))
b = int(input("Podaj drugą liczbę zakresu: "))

suma = 0

while a < b:
    if a % 2 == 1:
        suma += a
    a += 1

print(f"Suma wszystkich liczb nieparzystych z zakresu [{a}, {b}] wynosi: {suma}")
