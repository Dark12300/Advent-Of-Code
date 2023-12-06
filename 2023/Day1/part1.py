with open("input.txt", "r") as file:
    lines = file.read().splitlines()

total = 0
for line in lines:
    number = ""
    for x in range(0, len(line)):
        if line[x].isnumeric():
            number += line[x]
            break

    for x in range(len(line)-1, -1, -1):
        if line[x].isnumeric():
            number += line[x]
            break

    total += int(number)

print(total)