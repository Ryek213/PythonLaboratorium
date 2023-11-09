x = int(input("Podaj liczbę x do wyliczenia funkcji: "))

# funkcja a(x)
if x > 0:
    a = x * 2
elif x < 0:
    a = x * (-3)
else:
    a = 0

# funkcja b(x)
if x >= 1:
    b = x**2
else:
    b = x

# funkcja c(x)
if x > 2:
    c = x + 2
elif x < 2:
    c = x - 4
else:
    c = 8

print(f"Wynik a(x): {a}\n"
      f"Wynik b(x): {b}\n"
      f"Wynik c(x): {c}")