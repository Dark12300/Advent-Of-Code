with open("input.txt", "r") as file:
    text = file.read()

temporary = []
character = 0
for x in range(0, len(text)):
    temporary = [text[x], text[x+1], text[x+2], text[x+3]]
    if len(set(temporary)) == 4:
        character = x + 4
        break
    else:
        temporary = []

print(character)