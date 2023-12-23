enemies = [(0, 1), (2, 3), (2, 4), (3, 4)]
coins = [(1, 1), (2, 0), (3, 3), (5, 3)]
area = list()

for x in range(6):
    area.insert(x, list(str()))
    for y in range(5):
        if y == 2:
            area[x].insert(y, "=")
        elif (x, y) in enemies:
            area[x].insert(y, 'x')
        elif (x, y) in coins:
            area[x].insert(y, '*')
        else:
            area[x].insert(y, '.')


game_map = str()
for y in range(5):
    for x in range(6):
        game_map = game_map + area[x][y] + " "
    game_map += '\n'
print("Y z góry do dołu")
print(game_map)

game_map = str()
for y in range(5-1, -1, -1):
    for x in range(6):
        game_map = game_map + area[x][y] + " "
    game_map += '\n'
print("Y z dołu do góry")
print(game_map)
