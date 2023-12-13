tekst = input("Podaj zdanie: ")
tekst = tekst.lower()
tekst = sorted(tekst)
print(tekst)

alfabet = []

for i in range(ord('a'), ord('z')+1):
    f = True
    for k in tekst:
        if chr(i) == k:
            f = False
            break
    if f:
        alfabet.append(chr(i))

print(alfabet)
