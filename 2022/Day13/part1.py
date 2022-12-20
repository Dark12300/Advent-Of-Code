import json

with open("input.txt", "r") as file:
    groups = file.read().split("\n\n")
    lines = [list(map(json.loads, group.splitlines())) for group in groups]

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left > right:
            return -1
        elif left < right:
            return 1
        elif left == right:
            return 0

    if isinstance(left, int):
        left = [left]
            
    if isinstance(right, int):
        right = [right]

    index = 0
    while index < len(left) and index < len(right):
        compare_left = left[index]
        compare_right = right[index]

        comparison = compare(compare_left, compare_right)
        if comparison != 0:   #if comparison is 1 or -1
            return comparison

        index = index + 1

    if index == len(left):
        if len(left) == len(right):
            return 0
        return 1

    return -1

total = 0
for index, group in enumerate(lines):
    if compare(group[0], group[1]) == 1:
        total = total + (index + 1)

print(total)