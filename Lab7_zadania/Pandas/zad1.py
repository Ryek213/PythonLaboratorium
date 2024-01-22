import pandas as pd

data = {'Nr_Albumu': ['12345', '54123', '98745', '64985'],
        'Imię':['Anna', 'Jan', 'Katarzyna', 'Tomasz'],
        'Nazwisko':['Kowalska', 'Nowak', 'Wójcik', 'Ferenc'],
        'Ocena':[4.5, 5.0, 3.5, 4.0]}
# print(data)
df = pd.DataFrame(data)
# print(df)

print(df[df['Ocena'] > 4])
# a1
for row in df[df['Ocena'] > 4]:
        print(row)

# b
print(df.sort_values('Ocena'))
