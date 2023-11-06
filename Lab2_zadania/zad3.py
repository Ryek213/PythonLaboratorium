print("Rozwiązywanie równania kwadratowego")
f = True

while(f):
    a = float(input("Podaj współczynnik a: "))
    if a == 0:
        print("Współczynnik a musi być rożne od 0")
    else:
        f = False
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("Równanie nie ma rozwiązań")
elif delta == 0:
    print("Równanie ma jedno rozwiązanie:\n"
          f"x = {-b / (2 * a)}")
elif delta >= 0:
    print("Równianie ma dwa rozwiązania:\n"
          f"x1 = {(-b - delta ** (1/2)) / (2 * a)}\n"
          f"x2 = {(-b + delta ** (1/2)) / (2 * a)}")