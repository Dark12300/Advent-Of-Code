with open("input.txt", "r") as file:
    lines = file.read().splitlines()

def numbers_around_position(position, without_corners=False):
    directions = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    directions_without_corners = [direction for direction in directions if direction[0] == 0 or direction[1] == 0]

    if without_corners:
        return [[sum(sublist) for sublist in list(zip(position, direction))] for direction in directions_without_corners]

    return [[sum(sublist) for sublist in list(zip(position, direction))] for direction in directions]

head_position = [0, 0]   #track the head and tail like the index numbers in a 2D array
tail_positions = [[0, 0] for x in range(0, 9)]
positions_with_9 = [[0, 0]]
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

        for y in range(0, 9):
            tail_position = tail_positions[y]
            position_to_follow = tail_positions[y-1] if y >= 1 else head_position

            if tail_position in numbers_around_position(position_to_follow) or tail_position == position_to_follow:
                continue
            
            new_position = [position for position in numbers_around_position(tail_position) if position in numbers_around_position(position_to_follow, without_corners=True)]
            if len(new_position) == 0:
                new_position = [position for position in numbers_around_position(tail_position) if position in numbers_around_position(position_to_follow)]

            new_position = new_position[0]
            tail_positions[y] = new_position

            if y == 8:
                if new_position not in positions_with_9:
                    positions_with_9.append(new_position)

print(len(positions_with_9))