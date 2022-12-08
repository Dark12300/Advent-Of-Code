import os

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

directory_tree = {}
file_tree = {}
current_directory = ""
read_directory_lines = False
for line in lines:   #skip the first slash
    if line[0] == "$":
        read_directory_lines = False

    if read_directory_lines:
        if "dir" not in line:
            size, filename = line.split()
            file_tree[current_directory][filename] = int(size)
        else:
            directory_tree[(current_directory + "/" + line.split()[1]).replace("//", "/")] = 0

        continue

    if "cd" in line:
        if ".." in line:
            current_directory = os.path.split(current_directory)[0]
        else:
            current_directory = (current_directory + "/" + line.split()[2]).replace("//", "/")
            if current_directory not in file_tree.keys():
                file_tree[current_directory] = {}
    
    elif "ls" in line:
        read_directory_lines = True

for directory, size in dict(sorted(directory_tree.items(), reverse=True, key=lambda x: x[0].count("/"))).items():
    directory_tree[directory] = sum(file_tree[directory].values())

outermost_directory_size = sum(size for size in directory_tree.values())
smallest_to_largest_sub_directories = dict(sorted(directory_tree.items(), key=lambda x: sum([size for directory, size in directory_tree.items() if x[0] in directory])))
for directory, size in smallest_to_largest_sub_directories.items():
    sub_directory_sum = sum([size_ for directory_, size_ in directory_tree.items() if directory in directory_])
    if (70000000 - outermost_directory_size) + sub_directory_sum >= 30000000:
        print(sub_directory_sum)
        break