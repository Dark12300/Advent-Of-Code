with open("input.txt", "r") as file:
    rounds = [line.split(" ") for line in file.read().splitlines()]

letter_to_score = {"X": 1, "Y": 2, "Z": 3}
game_results = {"AX": 3, "BX": 0, "CX": 6, "AY": 6, "BY": 3, "CY": 0, "AZ": 0, "BZ": 6, "CZ": 3}

total_score = 0
for round in rounds:
    total_score = total_score + letter_to_score[round[1]] + game_results[round[0] + round[1]]

print(total_score)