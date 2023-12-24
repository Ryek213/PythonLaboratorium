def bmi(masa, wzrost):
    bmi_w = masa / (wzrost / 100) ** 2

    if bmi_w < 16:
        zakres = "wyglodzenie"
    elif bmi_w < 17:
        zakres = "wychudzenie"
    elif bmi_w < 18.5:
        zakres = "niedowaga"
    elif bmi_w < 25:
        zakres = "prawidlowa masa ciala"
    elif bmi_w < 30:
        zakres = "nadwaga"
    elif bmi_w < 35:
        zakres = "otylosc 1 stopnia"
    elif bmi_w < 40:
        zakres = "otylosc 2 stopnia"
    else:
        zakres = "otylosc 3 stopnia"
    print(f"Masa {masa}kg, wzrost {wzrost}cm: BMI: {bmi_w}, zakres: {zakres}")
    return


bmi(float(input("Podaj swoja wagę [kg]: ")), float(input("Podaj swój wzrost [cm]: ")))
