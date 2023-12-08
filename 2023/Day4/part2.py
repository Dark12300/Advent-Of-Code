with open("input.txt", "r") as file:
    lines = file.read().splitlines()

def get_match_count(winning_numbers, numbers_received):
    matches = 0
    for number in numbers_received:
        if number in winning_numbers:
            matches += 1

    return matches

card_instances = {}   #for each card, the total amount of instances that card will gain after (including itself)
for line in reversed(lines):
    card, lists = line.replace("  ", " ").split(":")
    card_number = int(card.replace("  ", " ").split(" ")[1])
    number_lists = lists.split("|")
    
    winning_numbers = number_lists[0].strip().split(" ")
    numbers_received = number_lists[1].strip().split(" ")

    matches = get_match_count(winning_numbers, numbers_received)
    iterations_left = list(range(card_number+1, card_number+matches+1))   #card numbers left to add future instance counts for
    instances = 1
    for iteration_number in iterations_left:
        instances += card_instances[iteration_number]

    card_instances[card_number] = instances

print(sum(card_instances.values()))