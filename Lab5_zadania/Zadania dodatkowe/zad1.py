def znajdz_plec(plec):
    if plec[-1] == "a":
        return "kobieta"
    else:
        return "mężczyzna"


imiona = ["Martyna", "Marcin", "Kacper", "Anastazja", "Wojtek"]
osoby = dict()

for imie in imiona:
    osoby.update({imie: znajdz_plec(imie)})

print(osoby)
