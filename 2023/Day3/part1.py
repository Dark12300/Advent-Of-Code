with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    total_rows = len(lines)
    total_columns = len(lines[0])    

def filter_directions(start_directions, end_directions, index, value):   #filter out directions with a certain value at a certain index
    new_start = list(filter(lambda position: position[index] != value, start_directions))
    new_end = list(filter(lambda position: position[index] != value, end_directions))
    
    return new_start, new_end

def get_neighbours(row, column, length):   #the start row and column of the number and its length
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

    neighbours = []
    #find start and end index neighbours
    for position in start_directions + end_directions:
        neighbours.append(lines[position[0]][position[1]])

    for x in range(column+1, column+(length-1)):
        if row != 0:
            neighbours.append(lines[row-1][x])

        if row != (total_rows - 1):
            neighbours.append(lines[row+1][x])

    return neighbours

total = 0
for row in range(0, total_rows):
    current_line = lines[row]
    column = 0
    while column < total_columns:
        character = current_line[column]
        if not character.isnumeric():
            column += 1
            continue

        length = 1
        while True:
            if (column + length) == total_columns or not current_line[column+length].isnumeric():
                break

            length += 1

        neighbours = get_neighbours(row, column, length)
        if any(neighbour != "." for neighbour in neighbours):
            total += int(current_line[column:column+length])

        column += length

print(total)