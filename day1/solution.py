import sys

if __name__ == "__main__":
    running_sum = 0
    elves = []
    for line in sys.stdin:
        if(line == "\n"):
            elves.append(running_sum)
            running_sum = 0
        else:
            running_sum += int(line)
    elves.sort()
    print("Top:", sum(elves[-1:]))
    print("Top Three:", sum(elves[-3:]))
    