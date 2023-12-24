def czy_palindrom(tekst):
    flaga = True
    for i in range(len(tekst)):
        if not (tekst[i] == tekst[-i-1]):
            flaga = False
            break

    return flaga


print(czy_palindrom("kajak"))
print(czy_palindrom("dom"))
print(czy_palindrom("hello world"))
