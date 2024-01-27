import pandas as pd

data = {'Nr_Albumu': ['12345', '54123', '98745', '64985'],
        'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz'],
        'Nazwisko': ['Kowalska', 'Nowak', 'Wójcik', 'Ferenc'],
        'Ocena': [4.0, 5.0, 3.5, 4.0],
        'Wiek': [18, 23, 20, 20]}

df = pd.DataFrame(data)

# a
print("a:")
print(df[df['Ocena'] > 4])
print('\n')

# b
print("b:")
print(df.sort_values('Ocena'))
print('\n')

# c
print("c:")
dfgOcena = df.groupby('Ocena')
for ocena in dfgOcena.first().index:
    suma = 0
    ile = 0
    for index in dfgOcena.get_group(ocena).index:
        suma += df.loc[index, "Wiek"]
        ile += 1
    print(f"Średnia wieku dla oceny {ocena}: {suma/ile}")

# d
print("d:")
