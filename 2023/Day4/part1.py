with open("input.txt", "r") as file:
    lines = file.read().splitlines()

total = 0
for line in lines:
    number_lists = line.replace("  ", " ").split(":")[1].split("|")
    winning_numbers = number_lists[0].strip().split(" ")
    numbers_received = number_lists[1].strip().split(" ")

    matches = 0
    for number in numbers_received:
        if number in winning_numbers:
            matches += 1
    
    if matches > 0:
        total += 2 ** (matches - 1)

print(total)