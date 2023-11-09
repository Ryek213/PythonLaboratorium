n = int(input("Podaj liczbę studentów: "))
punkty = 0

i = 0
while i in range(n):
    punkty += int(input(f"Podaj liczbę punktów {i+1}. studenta: "))
    i += 1

print(f"Średnia punktów: {punkty/n}")
