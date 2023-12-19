def przedstaw(imie, wiek = 20):
    print(f"Imie: {imie}, wiek: {wiek}")
    return


przedstaw.__doc__ = "Funkcja wypisuje wpisane imie i wiek"


przedstaw("Marcin", 50)
przedstaw("Wojtek")
print(przedstaw.__doc__)
