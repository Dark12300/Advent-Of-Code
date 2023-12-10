from math import ceil, sqrt

with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    parse = lambda line: int(line.split(":")[1].replace(" ", ""))
    time, distance = map(parse, lines)

record_positions = [(-time + sqrt(time**2-4*distance)) // -2, ceil((-time - sqrt(time**2-4*distance)) / -2)]
options = int(record_positions[1] - record_positions[0] - 1)

print(options)