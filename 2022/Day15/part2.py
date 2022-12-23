with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    sensor_positions = [(int(line[line.find("x")+2:line.find(",")]), int(line[line.find("y")+2:line.find(":")])) for line in lines]
    beacon_positions = [(int(line[line.rfind("x")+2:line.rfind(",")]), int(line[line.rfind("y")+2:])) for line in lines]

def distance(sensor, beacon):
    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

positive_lines = []
negative_lines = []

for x in range(0, len(sensor_positions)):
    sensor_position = sensor_positions[x]
    beacon_position = beacon_positions[x]
    current_distance = distance(sensor_position, beacon_position)

    positive_lines.extend([sensor_position[0] - sensor_position[1] - current_distance, sensor_position[0] - sensor_position[1] + current_distance])
    negative_lines.extend([sensor_position[0] + sensor_position[1] - current_distance, sensor_position[0] + sensor_position[1] + current_distance])

for i in range(len(sensor_positions) * 2):
    for j in range(i + 1, len(sensor_positions) * 2):
        a, b = positive_lines[i], positive_lines[j]

        if abs(a - b) == 2:
            positive = min(a, b) + 1

        a, b = negative_lines[i], negative_lines[j]

        if abs(a - b) == 2:
            negative = min(a, b) + 1

x, y = (positive + negative) // 2, (negative - positive) // 2
answer = x * 4000000 + y
print(answer)