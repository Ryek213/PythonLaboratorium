cyfry = (input("Podaj 5 cyfr rozdzielone przecinkiem: ")).split(", ")

if len(cyfry) != 5:
    print("Nie podano pięciu cyfr")
    exit()

for i in range(len(cyfry)):
    cyfry[i] = int(cyfry[i])

cyfry = set(cyfry)
print(cyfry)

a = cyfry.pop()

cyfry_min = a
cyfry_max = a
for i in cyfry:
    cyfry_min = min(cyfry_min, i)
    cyfry_max = max(cyfry_max, i)

cyfry.add(a)
print(a)
if a == cyfry_max:
    print("Wylosowana liczba jest największa")
elif a == cyfry_min:
    print("Wylosowana liczba jest najmniejsza")
else:
    print("Wylosowana liczba nie jest ani największa, ani najmniejsza")
