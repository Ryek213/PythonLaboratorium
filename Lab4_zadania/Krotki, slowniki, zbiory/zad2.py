lista_zakupow = {"ryż": 10, "cukierki": 15, "chleb": 4, "woda": 12}
suma = 0

print(lista_zakupow)

for i in lista_zakupow.values():
    suma += i

print(f"Wydatki: {suma}zl")
