from math import lcm

with open("input.txt", "r") as file:
    instructions, nodes = file.read().split("\n\n")
    nodes = nodes.splitlines()

mappings = {}
for elements in nodes:
    mappings[elements[:3]] = [elements[7:10], elements[12:15]]

current_nodes = list(filter(lambda node: node[-1] == "A", mappings.keys()))
current_node_steps = []
for node in current_nodes:
    current = node
    instruction_index = 0
    steps = 0
    while current[-1] != "Z":
        element_index = 0 if instructions[instruction_index] == "L" else 1
        current_options = mappings[current]

        steps += 1
        current = current_options[element_index]
        instruction_index = (instruction_index + 1) % len(instructions)

    current_node_steps.append(steps)

answer = lcm(*current_node_steps)

print(answer)