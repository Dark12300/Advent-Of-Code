with open("input.txt", "r") as file:
    rows = file.read().splitlines()

total_trees_visible = 0
for x in range(0, len(rows)):
    row = rows[x]

    if x == 0 or x == len(rows) - 1:
        total_trees_visible = total_trees_visible + len(row)
        continue

    for y in range(0, len(row)):
        if y == 0 or y == len(row) - 1:
            total_trees_visible = total_trees_visible + 1
            continue

        current_tree = int(row[y])

        if all([True if current_tree > int(rows[i][y]) else False for i in range(0, x)]):   #trees above
            total_trees_visible = total_trees_visible + 1

        elif all([True if current_tree > int(rows[i][y]) else False for i in range(x+1, len(rows))]):   #trees below
            total_trees_visible = total_trees_visible + 1
        
        elif all([True if current_tree > int(i) else False for i in row[:y]]):   #trees to the left
            total_trees_visible = total_trees_visible + 1

        elif all([True if current_tree > int(i) else False for i in row[y+1:]]):   #trees to the right
            total_trees_visible = total_trees_visible + 1

print(total_trees_visible)