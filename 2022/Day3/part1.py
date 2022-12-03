with open("input.txt", "r") as file:
    lines = file.read().splitlines()

priority_total = 0
for line in lines:
    for character in line[0:(len(line)//2)]:
        if line[(len(line)//2):].count(character) >= 1:
            if character.islower():
                priority_total = priority_total + (ord(character) - 96)
            elif character.isupper():
                priority_total = priority_total + (ord(character) - 38)
            break

print(priority_total)