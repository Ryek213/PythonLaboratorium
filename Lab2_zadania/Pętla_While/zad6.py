punkty = 0

i = 0
while True:
    pom = int(input(f"Podaj liczbę punktów {i+1}. studenta: "))
    if not 0 <= pom <= 100:
        break
    punkty += pom
    i += 1

print(f"Średnia punktów {i} studentów: {punkty/i}")
