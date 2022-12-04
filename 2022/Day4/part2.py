with open("input.txt", "r") as file:
    lines = file.read().splitlines()

count = 0
for line in lines:
    elf1, elf2 = line.split(",")

    range1 = list(map(int, elf1.split("-")))
    range1 = range(range1[0], range1[1]+1)

    range2 = list(map(int, elf2.split("-")))
    range2 = range(range2[0], range2[1]+1)

    if any(x in range2 for x in range1) or any(x in range1 for x in range2):
        count = count + 1

print(count)