while True:
    char = input("Podaj literę: ")

    if len(char) > 1:
        print("Podaj tylko jedną literę!!!")
    elif "A" <= char <= "Z":
        char = chr(ord(char)+32)
        break
    elif "a" <= char <= "z":
        char = chr(ord(char)-32)
        break
    else:
        print("Nie podano litery")

print(f"Oto twoja litera: {char}")
