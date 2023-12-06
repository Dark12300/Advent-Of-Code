with open("input.txt", "r") as file:
    lines = file.read().splitlines()

def parse_line(line):
    game_info, information = line.split(":")
    subsets_id = game_info.split(" ")[1]
    subsets = information.split(";")

    subsets_info = {"red": 0, "green": 0, "blue": 0}   #r, g, b max values out of all subsets
    for subset in subsets:
        pairs = subset.split(",")
        for pair in pairs:
            count, colour = pair.strip().split(" ")

            if subsets_info[colour] < int(count):
                subsets_info[colour] = int(count)

    return int(subsets_id), subsets_info

total = 0
for line in lines:
    subsets_id, subsets_info = parse_line(line)
    if subsets_info["red"] <= 12 and subsets_info["green"] <= 13 and subsets_info["blue"] <= 14:
        total += subsets_id
        
print(total)