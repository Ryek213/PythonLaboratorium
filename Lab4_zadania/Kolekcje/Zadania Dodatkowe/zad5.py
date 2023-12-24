tekst = input("Podaj zdanie: ")
slowa = tekst.split(" ")

s = str()
for i in slowa:
    if len(i) > len(s):
        s = i
        
print(f"Najdłuższe słowo: {s}, długość: {len(s)}")
