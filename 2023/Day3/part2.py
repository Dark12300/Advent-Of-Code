with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    total_rows = len(lines)
    total_columns = len(lines[0])    

def filter_directions(start_directions, end_directions, index, value):   #filter out directions with a certain value at a certain index
    new_start = list(filter(lambda position: position[index] != value, start_directions))
    new_end = list(filter(lambda position: position[index] != value, end_directions))
    
    return new_start, new_end

def get_neighbour_positions(row, column, length):   #the start row and column of the number and its length
    start_directions = [   #neighbour directions for first index
        (row-1, column), (row-1, column-1),
        (row, column-1), (row+1, column-1), (row+1, column),
    ]

    end_directions = [   #neighbour directions for last index
        (row-1, column+(length-1)), (row-1, column+1+(length-1)),
        (row, column+1+(length-1)), (row+1, column+1+(length-1)), (row+1, column+(length-1)),
    ]

    if row == 0:   #upper bounds
        start_directions, end_directions = filter_directions(start_directions, end_directions, 0, -1)

    elif row == (total_rows - 1):   #lower bounds
        start_directions, end_directions = filter_directions(start_directions, end_directions, 0, row+1)

    if column == 0:   #left bounds
        start_directions, end_directions = filter_directions(start_directions, end_directions, 1, -1)
    
    elif (column + length) == total_columns:
        start_directions, end_directions = filter_directions(start_directions, end_directions, 1, total_columns)

    neighbour_positions = start_directions + end_directions

    for x in range(column+1, column+(length-1)):
        if row != 0:
            neighbour_positions.append((row-1, x))

        if row != (total_rows - 1):
            neighbour_positions.append((row+1, x))

    return neighbour_positions

def find_numbers(current_line):   #return a list all the number indexes and lengths in a line
    numbers = []
    column = 0
    while column < total_columns:
        character = current_line[column]
        if not character.isnumeric():
            column += 1
            continue

        start_index = column
        length = 1
        while True:
            if (column + 1) == total_columns or not current_line[column+1].isnumeric():
                break

            length += 1
            column += 1

        numbers.append((start_index, length, int(current_line[start_index:start_index+length])))
        column += 1

    return numbers

total = 0
for row in range(0, total_rows):
    current_line = lines[row]
    for column in range(0, total_columns):
        character = current_line[column]
        if character == "*":
            adjacent_numbers = []
    
            for row_offset in range(-1, 2):
                for number_info in find_numbers(lines[row+row_offset]):
                    neighbour_positions = get_neighbour_positions(row+row_offset, number_info[0], number_info[1])
                    if (row, column) in neighbour_positions:
                        adjacent_numbers.append(number_info[2])

            if len(adjacent_numbers) == 2:
                ratio = adjacent_numbers[0] * adjacent_numbers[1]
                total += ratio

print(total)