import random

while True:
    while True:
        pocz_zakr = input("Poczatek zakresu: ")
        flaga = True
        for i in pocz_zakr:
            if not ('0' <= i <= '9' or i == '-'):
                print("Podaj liczbę całkowitą!")
                flaga = False
                break
        if flaga:
            pocz_zakr = int(pocz_zakr)
            break

    while True:
        kon_zakr = input("Koniec zakresu: ")
        flaga = True
        for i in kon_zakr:
            if not ('0' <= i <= '9' or i == '-'):
                print("Podaj liczbę całkowitą!")
                flaga = False
                break
        if flaga:
            kon_zakr = int(kon_zakr)
            break

    if kon_zakr < pocz_zakr:
        print("Koniec zakresu powinien być większy niż początek!")
        continue
    elif kon_zakr - pocz_zakr + 1 <= 5:
        print("Gra będzie zbyt prosta, zwiększ zakres powyżej 5!")
    else:
        break


los = random.randint(pocz_zakr, kon_zakr)
wynik = False
print(f"Zakres liczb: [{pocz_zakr}, {kon_zakr}]")
for n in range(3):
    while True:
        liczba = input(f"Próba {n + 1}: ")
        flaga = True
        for i in liczba:
            if not ('0' <= i <= '9' or i == '-'):
                print("Podaj liczbę całkowitą!")
                flaga = False
                break
        if flaga:
            liczba = int(liczba)
            break

    if liczba == los:
        wynik = True
        break
    elif liczba > los:
        print("Za dużo")
    elif liczba < los:
        print("Za mało")

if wynik:
    print("Brawo! Wygrałeś(aś) grę!")
else:
    print(f"Przykro mi, przegrałeś(aś) :( Szukana liczba to: {los}")
