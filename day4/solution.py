import sys

if __name__ == "__main__":

    count = 0

    for line in sys.stdin:
        # Process Line
        pairs = line[:-1].split(",")
        elves = []
        for i, elf in enumerate(pairs):
            elves.append([int(i) for i in elf.split("-")])

        # Just check if the range is all INSIDE or OUTSIDE
        if (elves[0][0] <= elves[1][0] and elves[0][1] >= elves[1][1]) or (elves[1][0] <= elves[0][0] and elves[1][1] >= elves[0][1]):
            count += 1
        elif (elves[0][1] >= elves[1][0] and elves[0][0] <= elves[1][1]) or (elves[1][1] >= elves[0][0] and elves[1][0] <= elves[0][1]):
            count += 1

    print(f"Total Number: {count}")
    