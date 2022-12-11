with open("input.txt", "r") as file:
    lines = file.read().splitlines()

cycle = 0
x = 1
to_add = False
screen = ["" for x in range(0, 6)]
for line in lines:
    if "addx" in line:
        add_value = int(line.split()[1])
        to_add = True
        cycle = cycle + 1
        pixel = "#" if (cycle % 40) in [x, x+1, x+2] else "."
        screen[(cycle-1) // 40] = screen[(cycle-1) // 40] + pixel
        
    cycle = cycle + 1
    pixel = "#" if (cycle % 40) in [x, x+1, x+2] else "."
    screen[(cycle-1) // 40] = screen[(cycle-1) // 40] + pixel

    if to_add:
        x = x + add_value
        to_add = False

for line in screen:
    print(line)