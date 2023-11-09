while True:
    pada = input("Czy pada? (Tak/Nie): ")
    if pada == "Tak" or pada == "Nie":
        break
    else:
        print("Spróbuj jeszcze raz")

while True:
    autobus = input("Czy jest autobus? (Tak/Nie): ")
    if autobus == "Tak" or autobus == "Nie":
        break
    else:
        print("Spróbuj jeszcze raz")

if pada == "Tak" and autobus == "Tak":
    print("Weź parasol\n"
          "Dostaniesz się na uczelnię")
elif pada == "Tak" and not autobus == "Tak":
    print("Nie dostaniesz się na uczelnię")
elif not pada == "Tak" and autobus == "Tak":
    print("Dostaniesz się na uczelnię\n"
          "Miłego dnia i pięknej pogody")
else:
    print("Przykro mi, program nie jest przygotowany na taką odpowiedź :(")
