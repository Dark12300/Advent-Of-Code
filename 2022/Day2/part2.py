with open("input.txt", "r") as file:
    rounds = [line.split(" ") for line in file.read().splitlines()]

letter_to_score = {"X": 1, "Y": 2, "Z": 3}

total_score = 0
for round in rounds:
    if round[1] == "X":
        if round[0] == "A":
            total_score = total_score + letter_to_score["Z"]
        elif round[0] == "B":
            total_score = total_score + letter_to_score["X"]
        elif round[0] == "C":
            total_score = total_score + letter_to_score["Y"]
        
    elif round[1] == "Y":
        if round[0] == "A":
            total_score = total_score + 3 + letter_to_score["X"]
        elif round[0] == "B":
            total_score = total_score + 3 + letter_to_score["Y"]
        elif round[0] == "C":
            total_score = total_score + 3 + letter_to_score["Z"]

    elif round[1] == "Z":
        if round[0] == "A":
            total_score = total_score + 6 + letter_to_score["Y"]
        elif round[0] == "B":
            total_score = total_score + 6 + letter_to_score["Z"]
        elif round[0] == "C":
            total_score = total_score + 6 + letter_to_score["X"]

print(total_score)