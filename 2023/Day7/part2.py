from collections import Counter

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

types = {"five": [], "four": [], "full": [], "three": [], "two": [], "one": [], "high": []}
hand_to_bid = {}
for line in lines:
    hand, bid = line.split()
    hand_to_bid[hand] = bid

    j_count = hand.count("J")
    counter = sorted(list(Counter(hand).values()))
    if 0 < j_count < 5:
        counter.remove(j_count)
        counter[-1] += j_count
    
    if counter == [5]:
        hand_type = "five"

    elif counter == [1, 4]:
        hand_type = "four"
    
    elif counter == [2, 3]:
        hand_type = "full"
    
    elif counter == [1, 1, 3]:
        hand_type = "three"

    elif counter == [1, 2, 2]:
        hand_type = "two"

    elif counter == [1, 1, 1, 2]:
        hand_type = "one"

    else:
        hand_type = "high"

    types[hand_type].append(hand)

cards = ["A", "K", "Q", "T"] + list(map(str, range(9, 1, -1))) + ["J"]
ordered_hands = []
for hand_type, hands in types.items():
    ordered_hands += sorted(hands, key=lambda hand: [cards.index(card) for card in hand])   #strongest first

total = 0
for x in range(0, len(ordered_hands)):
    rank = len(lines) - x
    bid = hand_to_bid[ordered_hands[x]]
    total += rank * int(bid)

print(total)