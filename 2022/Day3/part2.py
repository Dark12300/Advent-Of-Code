with open("input.txt", "r") as file:
    lines = file.read().splitlines()

priority_score = 0
for x in range(0, len(lines), 3):
    for character in lines[x]:
        if character in lines[x+1] and character in lines[x+2]:
            if character.islower():
                priority_score = priority_score + (ord(character) - 96)
            elif character.isupper():
                priority_score = priority_score + (ord(character) - 38)
            break

print(priority_score)