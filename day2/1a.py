# 12 red, 13 green, 14 blue

input = open("day2/input.txt", "r")
sum = 0

for line in input:
    game = line.split(":")[0].strip("Game ")
    