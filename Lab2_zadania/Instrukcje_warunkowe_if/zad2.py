print("Jaką operację chcesz wykonać?\n"
      "1. dodawanie\n"
      "2. odejmowanie\n"
      "3. mnożenie\n"
      "4. dzielenie\n"
      "5. potęgowanie")
operacja = int(input("Wprowadź numer operacji: "))

if 1 <= operacja <= 5:
      a = int(input("Wprowadź pierwszy argument: "))
      b = int(input("Wprowadź drugi argument: "))
      if operacja == 1:
            print(f"Wynik dodawania: {a+b}")
      elif operacja == 2:
            print(f"Wynik odejmowania: {a-b}")
      elif operacja == 3:
            print(f"Wynik mnożenia: {a*b}")
      elif operacja == 4:
            if b != 0:
                  print(f"Wynik dzielenia: {a/b}")
            else:
                  print("Nie można dzielić przez 0")
      elif operacja == 5:
            print(f"Wynik potęgowania: {a**b}")
      else:
            print("Wystąpił błąd")
else:
      print("Wprowadzono błędny numer operacji")