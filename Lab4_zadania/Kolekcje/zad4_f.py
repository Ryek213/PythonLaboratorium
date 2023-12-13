tekst1 = input("Podaj pierwszy tekst: ")
tekst2 = input("Podaj drugi tekst: ")
tekst3 = tekst1[:len(tekst1)//2] + tekst2[len(tekst2)//2:]
print(tekst3)
