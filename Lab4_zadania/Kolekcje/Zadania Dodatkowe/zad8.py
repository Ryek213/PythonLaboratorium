import math

alfabet = list()

for i in range(ord('a'), ord('z')+1):
    alfabet.append(chr(i))
print(alfabet)

while True:
    n = int(input("Podaj na ile znakow podzielić listę: "))

    if n <= 0:
        print("Liczba znaków powinna być większa od 0!!")
    elif n > len(alfabet):
        print("Liczba znaków powinna być niewiększa niż długość alfabetu!!")
    else:
        break

podz_alfabet = [str()]*(math.ceil(len(alfabet)/n))

for i in range(len(alfabet)):
    podz_alfabet[i//n] += alfabet[i]

print(podz_alfabet)
