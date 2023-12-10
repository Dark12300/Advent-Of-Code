with open("input.txt", "r") as file:
    line_groups = file.read().split("\n\n")

def get_location_number(seed):
    source = seed
    for current_map in maps:
        for numbers in current_map:
            if numbers[1] <= source < (numbers[1] + numbers[2]):
                source = source - numbers[1] + numbers[0]   #source - (numbers[1] - numbers[0])
                break

    return source

initial_seeds = list(map(int, line_groups[0].split(":")[1].strip().split(" ")))
line_groups.pop(0)

#parse map inputs
maps = []   #will be a 3D array containing each map (in respective order) and their respective ranges
for group in line_groups:
    current_map = []
    for line in group.splitlines()[1:]:
        numbers = list(map(int, line.split(" ")))
        current_map.append(numbers)

    maps.append(current_map)

#main loop
lowest = get_location_number(initial_seeds[0])
for seed in initial_seeds:
    location_number = get_location_number(seed)
    if location_number < lowest:
        lowest = location_number

print(lowest)