import datetime

day = int(input("Podaj dzień: "))
month = int(input("Podaj miesiąc: "))
year = int(input("Podaj rok: "))

data = datetime.date(year, month, day)
print(f"Dzień roku: {int(data.strftime('%j'))}")
print(f"Numer tygodnia: {int(data.strftime('%W')) + 1}")
print(f"Dwa tygodnie przed: {data - datetime.timedelta(days=14)}")
print(f"Dwa tygodnie po: {data + datetime.timedelta(days=14)}")

sunday = data
while True:
    if int(sunday.strftime('%w')) == 0:
        break
    else:
        sunday = sunday + datetime.timedelta(days=1)

print(f"Data następnej niedzieli: {sunday}")
teraz = datetime.datetime.now()
print(f"Czas unixowy: "
      f"{int(datetime.datetime(data.year, data.month, data.day, teraz.hour, teraz.minute, teraz.second).timestamp())}")
