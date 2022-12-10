with open("input.txt", "r") as file:
    rows = file.read().splitlines()

scenic_scores = []
for x in range(0, len(rows)):
    row = rows[x]
    for y in range(0, len(row)):
        current_tree = int(row[y])
        scenic_score = 1

        distance = 0
        for i in range(x-1, -1, -1):
            if current_tree <= int(rows[i][y]):
                distance = distance + 1
                break
            distance = distance + 1
        scenic_score = scenic_score * distance

        distance = 0
        for i in range(x+1, len(rows)):
            if current_tree <= int(rows[i][y]):
                distance = distance + 1
                break
            distance = distance + 1
        scenic_score = scenic_score * distance

        distance = 0
        for i in range(y-1, -1, -1):
            if current_tree <= int(row[i]):
                distance = distance + 1
                break
            distance = distance + 1
        scenic_score = scenic_score * distance

        distance = 0
        for i in range(y+1, len(row)):
            if current_tree <= int(row[i]):
                distance = distance + 1
                break
            distance = distance + 1
        scenic_score = scenic_score * distance

        scenic_scores.append(scenic_score)

print(max(scenic_scores))