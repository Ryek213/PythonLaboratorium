def bmi(masa, wzrost):
    bmi = masa/(wzrost/100)**2

    if bmi < 16:
        zakres = "wyglodzenie"
    elif bmi < 17:
        zakres = "wychudzenie"
    elif bmi < 18.5:
        zakres = "niedowaga"
    elif bmi < 25:
        zakres = "prawidlowa masa ciala"
    elif bmi < 30:
        zakres = "nadwaga"
    elif bmi < 35:
        zakres = "otylosc 1 stopnia"
    elif bmi < 40:
        zakres = "otylosc 2 stopnia"
    else:
        zakres = "otylosc 3 stopnia"
    print(f"Masa {masa}kg, wzrost {wzrost}cm: BMI: {bmi}, zakres: {zakres}")
    return

for i in range(50, 171, 5):
    bmi(i, 200)
