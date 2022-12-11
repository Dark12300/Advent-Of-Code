with open("input.txt", "r") as file:
    lines = file.read().splitlines()

def numbers_around_position(position, without_corners=False):
    directions = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    directions_without_corners = [direction for direction in directions if direction[0] == 0 or direction[1] == 0]

    if without_corners:
        return [[sum(sublist) for sublist in list(zip(position, direction))] for direction in directions_without_corners]

    return [[sum(sublist) for sublist in list(zip(position, direction))] for direction in directions]

head_position = [0, 0]   #track the head and tail like the index numbers in a 2D array
tail_position = [0, 0]
positions_with_tail = [[0, 0]]
for line in lines:
    direction, count = line.split()

    for x in range(int(count)):
        if direction == "R":
            head_position[0] = head_position[0] + 1
        elif direction == "L":
            head_position[0] = head_position[0] - 1
        elif direction == "U":
            head_position[1] = head_position[1] + 1
        elif direction == "D":
            head_position[1] = head_position[1] - 1

        if tail_position in numbers_around_position(head_position) or tail_position == head_position:
            continue

        tail_position = [position for position in numbers_around_position(tail_position) if position in numbers_around_position(head_position, without_corners=True)][0]

        if tail_position not in positions_with_tail:
            positions_with_tail.append(tail_position)

print(len(positions_with_tail))