with open("input.txt", "r") as file:
    blocks = file.read().split("\n\n")
    blocks = [block.split() for block in blocks]

sorted_blocks = sorted(blocks, reverse=True, key=lambda x: sum(map(int, x)))
top_three_total = sum(map(int, sorted_blocks[0] + sorted_blocks[1] + sorted_blocks[2]))
print(top_three_total)