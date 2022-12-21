with open("input.txt", "r") as file:
    lines = [line.replace("->", "").split() for line in file.read().splitlines()]

def find_range(a, b):
    return range(a, b+1) if a < b else range(a, b-1, -1)

taken_positions = set()
for line in lines:
    for x in range(0, len(line)-1):
        current_position = list(map(int, line[x].split(",")))
        next_position = list(map(int, line[x+1].split(",")))

        if current_position[0] == next_position[0]:
            for number in find_range(current_position[1], next_position[1]):
                taken_positions.add((current_position[0], number))

        elif current_position[1] == next_position[1]:
            for number in find_range(current_position[0], next_position[0]):
                taken_positions.add((number, current_position[1]))

max_y = max(taken_positions, key=lambda position: position[1])[1]
def update_sand():
    global taken_positions

    x, y = 500, 0
    if (x, y) in taken_positions:
            return (x, y)

    while y <= max_y:

        if (x, y+1) not in taken_positions:
            y = y + 1
            continue

        if (x-1, y+1) not in taken_positions:
            x = x - 1
            y = y + 1
            continue

        if (x+1, y+1) not in taken_positions:
            x = x + 1
            y = y + 1
            continue

        break

    return (x, y)

answer = 0
while True:
    x, y = update_sand()
    taken_positions.add((x, y))
    answer = answer + 1
    if (x, y) == (500, 0):
        break

print(answer)