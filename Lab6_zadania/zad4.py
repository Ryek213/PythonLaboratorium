import datetime

miesiace = (
    "Styczeń",
    "Luty",
    "Marzec",
    "Kwiecień",
    "Maj",
    "Czerwiec",
    "Lipiec",
    "Sierpień",
    "Wrzesień",
    "Październik",
    "Listopad",
    "Grudzień"
    )


lab_data = datetime.date(2024, 1, 15)
lab_dni = (datetime.date.today() - lab_data).days

print(f"Minęło {lab_dni} dni od ostatnich laboratoriów"
      f" ({lab_data.strftime("%d")} {miesiace[int(lab_data.strftime("%m"))-1]} {lab_data.strftime("%Y")})")

kol_data = datetime.datetime(2024, 2, 12, 11, 45)
czas_teraz = datetime.datetime.now()

if czas_teraz > kol_data:
    print("Juz po kolokwium!")
else:
    kol_czas = kol_data - czas_teraz
    kol_dni = kol_czas.days
    pom = kol_czas.seconds
    kol_godziny = pom//(60*60)
    pom = pom - kol_godziny * 60 * 60
    kol_minuty = pom//60
    pom = pom - kol_minuty * 60
    kol_sekundy = pom

    print(f"Pozostało {kol_dni} dni, {kol_godziny} godzin, {kol_minuty} minut i {kol_sekundy} sekund do kolokwium"
          f" ({kol_data.strftime("%d")} {miesiace[int(kol_data.strftime("%m"))-1]} {kol_data.strftime("%Y")}"
          f" {kol_data.strftime("%X")})")
