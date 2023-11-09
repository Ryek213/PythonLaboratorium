while True:
    char = input("Podaj literę: ")

    if len(char) > 1:
        print("Podaj tylko jedną literę")
    elif "A" <= char <= "Z":
        print("Litera jest duża")
        break
    elif "a" <= char <= "z":
        print("Litera jest mała")
        break
    else:
        print("Nie podano litery")
