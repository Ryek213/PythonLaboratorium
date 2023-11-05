droga = int(input("Podaj drogę pokonaną przez samochód (km): "))
spalanie = int(input("Podaj średnie spalanie samochodu (l/100km): "))

zuzycie = droga * spalanie / 100
koszty = zuzycie * 6.5

print("Przewidywanie zużycie paliwa:", zuzycie, "litrów")
print("Szacowane koszty podróży:", koszty, "złotych")