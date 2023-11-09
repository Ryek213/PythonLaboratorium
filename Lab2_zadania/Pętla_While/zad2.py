pocz = -4
kon = 4
krok = 0.5

while pocz <= kon:
    print(f"x = {pocz}: y = {2 * pocz ** 2 - 5 * pocz - 8}")
    pocz += krok

print("Koniec!")
