with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    sensor_positions = [(int(line[line.find("x")+2:line.find(",")]), int(line[line.find("y")+2:line.find(":")])) for line in lines]
    beacon_positions = [(int(line[line.rfind("x")+2:line.rfind(",")]), int(line[line.rfind("y")+2:])) for line in lines]

def distance(sensor, beacon):
    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

target_y = 2000000
scanned_positions = set()
for i in range(0, len(sensor_positions)):
    sensor_x, sensor_y = sensor_positions[i]
    beacon_x, beacon_y = beacon_positions[i]
    current_distance = distance((sensor_x, sensor_y), (beacon_x, beacon_y))

    if target_y not in range(sensor_y-current_distance, (sensor_y+current_distance)+1):
        continue

    start_x = (sensor_x - current_distance) + abs(sensor_y - target_y)
    end_x = (sensor_x + current_distance) - abs(sensor_y - target_y)
    scanned_positions.add(range(start_x, end_x+1))

ranges = []
for number_range in scanned_positions:
    ranges = ranges + list(number_range)
ranges = list(set(ranges))
for beacon_position in filter(lambda position: position[1] == target_y, beacon_positions):
    if beacon_position[0] in ranges:
        ranges.remove(beacon_position[0])

print(len(ranges))