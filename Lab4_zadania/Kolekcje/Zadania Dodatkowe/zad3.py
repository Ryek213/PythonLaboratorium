tekst = input("Podaj zdanie: ")

tekst = " " + tekst + " "
tekst = tekst.lower()

for i in range(ord('a'), ord('z')+1):
    tekst = tekst.replace((" " + chr(i)), (" " + chr(i-32)))
    tekst = tekst.replace((chr(i) + " "), (chr(i - 32) + " "))
tekst = tekst[1:-1]
print(tekst)