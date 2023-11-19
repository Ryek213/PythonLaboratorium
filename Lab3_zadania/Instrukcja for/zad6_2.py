while True:
    dana = int(input("Podaj zmienną dana: "))

    if dana >= 0:
        print(f"Pierwiastek z {dana}: {dana**0.5}")
    else:
        print("Dziękujemy za skorzystanie z naszej aplikacji")
        break
