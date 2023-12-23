prad_rachunki = {"Lipiec":119, "Sierpień":127, "Wrzesień":87, "Październik": 83, "Listopad": 112, "Grudzień": 134}

srednia = 0
for i in prad_rachunki.values():
    srednia += i
srednia = srednia/len(prad_rachunki)

print(f"Max: {max(prad_rachunki.values())}, Min: {min(prad_rachunki.values())}, Średnia: {srednia}")

if list(prad_rachunki.values())[-1] > srednia:
    print("Zacznij oszczędzać!!")
else:
    print("Jesteś bezpieczny :)")
