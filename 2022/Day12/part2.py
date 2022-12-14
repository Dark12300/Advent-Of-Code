with open("input.txt", "r") as file:
    data = file.read()
    #start_index = data.replace("\n", "").index("S")
    end_index = data.replace("\n", "").index("E")
    data = data.replace("S", "a").replace("E", "z")
    data = data.splitlines()

def get_neighbours(index):
    line_length = len(data[0])
    directions = {"above": index - line_length, "right": index + 1, "below": index + line_length, "left": index - 1}
    to_remove = []

    if 0 <= index <= line_length:   #top line
        to_remove.append("above")
    if line_length * (len(data) - 1) <= index <= (line_length * len(data)) - 1:   #bottom line
        to_remove.append("below")
    if index % line_length == 0:   #left side
        to_remove.append("left")
    if (index + 1) % line_length == 0:   #right side
        to_remove.append("right")

    original_data = "".join(data)
    return [neighbour for direction, neighbour in directions.items() if direction not in to_remove and ord(original_data[neighbour]) - ord(original_data[index]) <= 1]

nodes = len(data[0]) * len(data)
def solve(start, end):
    queue = [start]
    visited = [False if x != start else True for x in range(nodes)]
    previous = [None for x in range(nodes)]
    
    while previous[end] is None:
        node = queue[0]
        queue.pop(0)

        neighbours = get_neighbours(node)
        for neighbour in neighbours:
            if not visited[neighbour]:
                queue.append(neighbour)
                visited[neighbour] = True
                previous[neighbour] = node

        if len(queue) == 0:
            return None
    
    return previous

def find_path(start, end):
    previous = solve(start, end)
    if previous is None:
        return None

    path = [end]
    current_index = end
    while True:
        if previous[current_index] is None:
            break

        path.append(previous[current_index])
        current_index = previous[current_index]
        
    return list(reversed(path))

original_data = "".join(data)
a_indexes = [index for index, value in enumerate(original_data) if value == "a"]
a_indexes_steps = []
for index in a_indexes:
    steps = find_path(index, end_index)
    if steps is not None:
        a_indexes_steps.append(len(steps) - 1)
        
print(min(a_indexes_steps))