tekst = input("Podaj palindrom: ")

flaga = True
for i in range(len(tekst)):
    if not (tekst[i] == tekst[-i-1]):
        flaga = False
        break

if flaga:
    print("Podany ciąg jest palindromem")
else:
    print("To nie jest palindrom!!")
