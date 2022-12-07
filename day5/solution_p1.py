import sys

indices = [1, 5, 9, 13, 17, 21, 25, 29, 33]

# Set up linked lists
columns = [[]]
for i in range(8):
    columns.append([])

def print_column(index):
    for item in columns[index]:
        print(item, end="-")
    print("")

def print_all_columns():
    for index in range(9):
        print_column(index)

if __name__ == "__main__":

    # Setup
    for i, line in enumerate(sys.stdin):
        if i == 8:
            break
        for column, index in enumerate(indices):
            if line[index] != " ":
                columns[column].append(line[index])
    
    for column in columns:
        for item in column:
            print(item, end = "-")
        print("")
    
    for line in sys.stdin:
        if line != "\n":
            line = line.split(" ")
            num_to_move = int(line[1])
            src = int(line[3]) - 1
            dst = int(line[5]) - 1
            print(num_to_move, src + 1, dst + 1)

            src_ll = columns[src]
            dst_ll = columns[dst]

            for i in range(num_to_move):
                columns[dst].insert(0, columns[src][0])
                columns[src].pop(0)

            # Remove debug
            print_all_columns()

        print("")

    print("")
                


    