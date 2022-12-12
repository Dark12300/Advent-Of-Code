with open("input.txt", "r") as file:
    monkeys = file.read().split("\n\n")

monkey_properties = []
for monkey in monkeys:
    lines = monkey.splitlines()
    starting_items = list(map(int, lines[1][lines[1].find(":")+2:].split(",")))
    operation = lines[2][lines[2].find("=")+2:]
    test = lines[3][lines[3].find(":")+2:].replace("divisible", "").replace("by", "").strip()
    test_true = int(lines[4][lines[4].find("monkey")+7])
    test_false = int(lines[5][lines[5].find("monkey")+7])

    monkey_properties.append([starting_items, operation, test, test_true, test_false])

monkey_inspection_count = [0 for x in range(0, len(monkey_properties))]
for i in range(0, 20):
    for x in range(0, len(monkey_properties)):
        monkey = monkey_properties[x]
        items, operation, test, test_true, test_false = monkey
        for worry_level in items:
            monkey_inspection_count[x] = monkey_inspection_count[x] + 1
            
            new_worry_level = eval(operation.replace("old", str(worry_level))) // 3
            test_outcome = new_worry_level % int(test)

            monkey_properties[test_true if test_outcome == 0 else test_false][0].append(new_worry_level)

        monkey_properties[x][0] = []

monkey_business = sorted(monkey_inspection_count, reverse=True)[0] * sorted(monkey_inspection_count, reverse=True)[1]
print(monkey_business)