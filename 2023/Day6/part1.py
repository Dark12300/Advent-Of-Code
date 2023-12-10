from math import ceil, sqrt

with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    parse = lambda line: list(map(int, line.split(":")[1].split()))
    times, distances = list(map(parse, lines))

total = 1
for time, distance in zip(times, distances):
    record_positions = [(-time + sqrt(time**2-4*distance)) // -2, ceil((-time - sqrt(time**2-4*distance)) / -2)]
    options = record_positions[1] - record_positions[0] - 1
    total *= int(options)

print(total)