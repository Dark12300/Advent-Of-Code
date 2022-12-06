with open("input.txt", "r") as file:
    text = file.read()

temporary = []
character = 0
for x in range(0, len(text)):
    temporary = [text[x+y] for y in range(0, 14)]
    if len(set(temporary)) == 14:
        character = x + 14
        break
    else:
        temporary = []

print(character)