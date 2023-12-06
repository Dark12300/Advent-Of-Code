with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    
numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

total = 0
for line in lines:
    number = ""
    
    section = ""
    breaker = False
    for x in range(0, len(line)):
        if line[x].isnumeric():
            number += line[x]
            break

        section += line[x]
        for word in numbers.keys():
            if word in section:
                number += numbers[word]
                breaker = True
                break

        if breaker:
            break

    section = ""
    breaker = False
    for x in range(len(line)-1, -1, -1):
        if line[x].isnumeric():
            number += line[x]
            break

        section = line[x] + section
        for word in numbers.keys():
            if word in section:
                number += numbers[word]#
                breaker = True
                break

        if breaker:
            break

    total += int(number)

print(total)