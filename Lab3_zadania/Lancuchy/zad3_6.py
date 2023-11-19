tekst1 = input("Podaj pierwszy tekst: ")
tekst2 = input("Podaj drugi tekst: ")
tekst3 = tekst1[slice(len(tekst1)//2)] + tekst2[slice(len(tekst2)//2, len(tekst2))]
print(tekst3)
