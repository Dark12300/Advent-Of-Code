with open("input.txt", "r") as file:
    blocks = file.read().split("\n\n")
    blocks = [block.split() for block in blocks]

highest_block_total = sum(map(int, max(blocks, key=lambda x: sum(map(int, x)))))
print(highest_block_total)