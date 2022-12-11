with open("input.txt", "r") as file:
    lines = file.read().splitlines()

cycle = 0
x = 1
to_add = False
signal_strengths = []
for line in lines:
    if "addx" in line:
        add_value = int(line.split()[1])
        to_add = True
        cycle = cycle + 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            signal_strengths.append(cycle * x)
        
    cycle = cycle + 1
    if cycle in [20, 60, 100, 140, 180, 220]:
        signal_strengths.append(cycle * x)

    if to_add:
        x = x + add_value
        to_add = False

print(sum(signal_strengths))