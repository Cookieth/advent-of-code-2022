import sys

# Define Rope Vector to be from Tail to Head

# Cases:
# Tail and Head are on top of each other:
#     Tail will stay in place
# Tail is in the direction of movement:
#     Tail will stay in place
# Tail is perpendicular to movement:
#     Tail will stay in place
# Tail is diagonal to movement:
#     Tail will move to where head is**
# Tail is in the opposite direction of movement:
#     Tail will move to where head is**

# So we want to look at DIRECTION minus HEADTAILVECTOR:
#   We only add the head location when ever the difference between NEW head and OLD tail is 2 in any direction

# We keep track a total history of all places visited, and then extract unique ones from that using set()

direction = {
    "U" : [0,  1],
    "D" : [0, -1],
    "L" : [-1, 0],
    "R" : [1,  0]
}

if __name__ == "__main__":

    tail_pos = [ [0, 0] ]
    head_pos = [ [0, 0] ]

    for line in sys.stdin:
        line = line[:-1].split(" ")
        print(line)
        for i in range(int(line[1])):
            # Move the head
            new_head_pos = [head_pos[-1][0] + direction[line[0]][0], head_pos[-1][1] + direction[line[0]][1]]
            if abs(new_head_pos[0] - tail_pos[-1][0]) > 1 or abs(new_head_pos[1] - tail_pos[-1][1]) > 1:
                tail_pos.append([head_pos[-1][0], head_pos[-1][1]])
            
            head_pos.append(new_head_pos)

    print(len(set([ (i[0], i[1]) for i in tail_pos])))
    
    