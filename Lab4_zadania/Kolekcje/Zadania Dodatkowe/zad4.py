tekst = input("Podaj zdanie: ")
znaki = set(str())
tekst = list(tekst)
for i in range(len(tekst)):
    if tekst[i] in znaki:
        tekst[i] = "@"
    else:
        znaki.add(tekst[i])

tekst = ''.join(tekst)
print(tekst)
