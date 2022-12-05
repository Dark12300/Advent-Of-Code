with open("input.txt", "r") as file:
    crates, moves = file.read().split("\n\n")
    crate_lines = crates.splitlines()
    move_lines = moves.splitlines()
    
supply_stacks = [[] for x in range(0, max(map(int, crate_lines[-1].split())))]
current_stack = -1
for line in crate_lines[:-1]:
    for x in range(0, len(line)):
        character = line[x]
        
        if (x + 3) % 4 == 0:
            current_stack = current_stack + 1

        if x == len(line) - 1:
            current_stack = -1
            
        if character.isalpha():
            supply_stacks[current_stack].insert(0, character)

for line in move_lines:
    moves_list = line.split()
    moves_list = [int(moves_list[1]), int(moves_list[3]), int(moves_list[5])]

    for x in range(moves_list[0]):
        supply_stacks[moves_list[2]-1].append(supply_stacks[moves_list[1]-1][-1])
        del supply_stacks[moves_list[1]-1][-1]

for stack in supply_stacks:
    print(stack[-1])