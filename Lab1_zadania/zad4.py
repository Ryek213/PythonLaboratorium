import random

droga = random.randint(1, 100000)
print("Pokonana droga:", droga, "km")
spalanie = float(input("Podaj średnie spalanie samochodu (l/100km): "))

zuzycie = droga * spalanie / 100
koszty = zuzycie * 6.5

print("Przewidywanie zużycie paliwa:", zuzycie, "litrów")
print("Szacowane koszty podróży:", koszty, "złotych")