wiek = int(input("Podaj wiek klienta: "))

if wiek < 0:
    print("Wprowadzono bledny wiek")
elif wiek < 4:
    print("Wejście za darmo")
elif wiek < 18:
    print("Cena biletu: 10zł")
else:
    print("Cena biletu: 20zł")
