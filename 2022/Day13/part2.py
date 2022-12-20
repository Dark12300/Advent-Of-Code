import json
from functools import cmp_to_key

with open("input.txt", "r") as file:
    packets = list(map(json.loads, file.read().replace("\n\n", "\n").splitlines()))

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

divider_packets = [[[2]], [[6]]]
packets.extend(divider_packets)

sorted_packets = sorted(packets, key=cmp_to_key(compare), reverse=True)
decoder_key = 1
for index, packet in enumerate(sorted_packets):
    if packet in divider_packets:
        decoder_key = decoder_key * (index + 1)

print(decoder_key)