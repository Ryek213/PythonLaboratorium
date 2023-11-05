import random

droga = random.randint(1, 100000)
print(f"Pokonana droga: {droga}km")
spalanie = float(input("Podaj średnie spalanie samochodu (l/100km): "))

zuzycie = droga * spalanie / 100
koszty = zuzycie * 6.5

print(f"Przewidywanie zużycie paliwa: {zuzycie}litrów")
print(f"Szacowane koszty podróży: {koszty}złotych")
