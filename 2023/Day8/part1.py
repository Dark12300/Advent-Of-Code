with open("input.txt", "r") as file:
    instructions, nodes = file.read().split("\n\n")
    nodes = nodes.splitlines()

mappings = {}
for elements in nodes:
    mappings[elements[:3]] = [elements[7:10], elements[12:15]]

current = "AAA"
instruction_index = 0
steps = 0
while current != "ZZZ":
    element_index = 0 if instructions[instruction_index] == "L" else 1
    current_options = mappings[current]

    steps += 1
    current = current_options[element_index]
    instruction_index = (instruction_index + 1) % len(instructions)

print(steps)