def licz_znaki(tekst):
    liczba_znakow = {"wielkie": int(), "male": int(), "inne": int()}

    for i in tekst:
        if ord(i) in range(ord("A"), ord("Z")+1):
            liczba_znakow["wielkie"] += 1
        elif ord(i) in range(ord("a"), ord("z")+1):
            liczba_znakow["male"] += 1
        else:
            liczba_znakow["inne"] += 1

    return liczba_znakow


print(licz_znaki(input("Wpisz tekst: ")))
