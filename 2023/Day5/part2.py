with open("input.txt", "r") as file:
    line_groups = file.read().split("\n\n")

def create_range_maps():   #create mappings for seed ranges to location ranges
    new_mappings = []
    source_ranges = seed_ranges
    for current_map in maps:
        sorted_map = sorted(current_map, key=lambda numbers: numbers[1])   #sort the map into ascending order of source ranges
        new_map = []   #start, end (both inclusidve), difference (to the destination)
        for seed_start, seed_length in source_ranges:
            pointer = seed_start - 1   #seeds after the pointer havent been mapped
            for destination, source, length in sorted_map:
                map_end = source + length - 1
                seed_end = seed_start + seed_length - 1
                difference = destination - source

                if pointer >= seed_end:
                    break

                if map_end < seed_start:
                    continue

                if source > seed_end:
                    new_map.append([pointer+1, seed_end, 0])
                    break

                if source <= (pointer + 1):
                    new_map.append([pointer+1, min(map_end, seed_end), difference])
                    pointer = min(map_end, seed_end)

                elif source > (pointer + 1):
                    new_map.append([pointer+1, source-1, 0])   #unmapped seeds
                    new_map.append([source, min(map_end, seed_end), difference])
                    pointer = min(map_end, seed_end)

            if pointer < seed_end:   #no mapping ranges went past the end of the seed range
                new_map.append([pointer+1, seed_end, 0])

        new_mappings.append(new_map)
        source_ranges = list(map(lambda numbers: [numbers[0] + numbers[2], numbers[1] - numbers[0] + 1], new_map))

    return new_mappings
                
seed_ranges = []
seeds_line = line_groups[0].split(":")[1].strip().split(" ")
for x in range(0, len(seeds_line), 2):
    start, length = seeds_line[x], seeds_line[x+1]
    seed_ranges.append([int(start), int(length)])

line_groups.pop(0)

#parse map inputs
maps = []   #will be a 3D array containing each map (in respective order) and their respective ranges
for group in line_groups:
    current_map = []
    for line in group.splitlines()[1:]:
        numbers = list(map(int, line.split(" ")))
        current_map.append(numbers)

    maps.append(current_map)

#main code
range_maps = create_range_maps()
lowest_location_numbers = sorted(range_maps[-1], key=lambda numbers: numbers[0] + numbers[2])[0]
lowest_location = lowest_location_numbers[0] + lowest_location_numbers[2]

print(lowest_location)