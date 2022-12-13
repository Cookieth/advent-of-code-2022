import sys
import numpy as np

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

PART = 2
ROPE_SIZE = 10

direction = {
    "U" : [0,  1],
    "D" : [0, -1],
    "L" : [-1, 0],
    "R" : [1,  0]
}

# # For part 2, we have to define a very long rope, of ROPE_SIZE.
# #   0 is the head, ROPE_SIZE - 1 is the tail
# rope = [ [[0, 0]] for i in range(ROPE_SIZE)]

# def recurse_move(knot):
#     # Base case, i has surpassed rope (last knot is len(rope) - 1)
#     if knot == len(rope):
#         return
    
#     direction_vector = [rope[knot-1][-1][0] - rope[knot][-1][0], rope[knot-1][-1][1] - rope[knot][-1][1]]

#     # As per last time, only move if knot-1 is now more than 2 away
#     if abs(direction_vector[0]) > 1 or abs(direction_vector[1]) > 1:
#         new_pos = rope[knot][-1]
#         print("Knot: ", knot, "Direction: ", direction_vector, "Old Position:", new_pos, end=" ")
#         # New case: If the orientation is diagonal, and direction is too which is now possible
#         if direction_vector[0] != 0 and direction_vector[1] != 0:
#         # if rope[knot-1][-1][0] != rope[knot][-1][0] and rope[knot-1][-1][1] != rope[knot][-1][1]:
#             # new_pos[0] = new_pos[0] + (1 if direction_vector[0] > 0 else -1)
#             # new_pos[1] = new_pos[1] + (1 if direction_vector[1] > 0 else -1)
#             print("[FIRST]", end="")
#             if direction_vector[0] > 0 and direction_vector[1] > 0:
#                 rope[knot].append([new_pos[0] + 1, new_pos[1] + 1])
#             elif direction_vector[0] > 0 and direction_vector[1] < 0:
#                 rope[knot].append([new_pos[0] + 1, new_pos[1] - 1])
#             elif direction_vector[0] < 0 and direction_vector[1] > 0:
#                 rope[knot].append([new_pos[0] - 1, new_pos[1] + 1])
#             elif direction_vector[0] < 0 and direction_vector[1] < 0:
#                 rope[knot].append([new_pos[0] - 1, new_pos[1] - 1])
            
#         else:
#             # new_pos[0] = new_pos[0] + (1 if direction_vector[0] > 0 else (-1 if direction_vector[0] < 0 else 0))
#             # new_pos[1] = new_pos[1] + (1 if direction_vector[1] > 0 else (-1 if direction_vector[1] < 0 else 0))
#             print("[SECOND]", end="")
#             if direction_vector[0] > 0:
#                 new_pos[0] = new_pos[0] + 1
#                 # new_pos[1] = new_pos[1] + 0
#             elif direction_vector[0] < 0:
#                 new_pos[0] = new_pos[0] - 1
#                 # new_pos[1] = new_pos[1] + 0
#             elif direction_vector[1] > 0:
#                 # new_pos[0] = new_pos[0] + 0
#                 new_pos[1] = new_pos[1] + 1
#             elif direction_vector[1] < 0:
#                 # new_pos[0] = new_pos[0] + 0
#                 new_pos[1] = new_pos[1] - 1
            
#             rope[knot].append([new_pos[0], new_pos[1]])
#         print("New Position:", new_pos)
#         # print(f"{knot}: Has: {rope[knot]}")
    
#     recurse_move(knot + 1)

rope = [ [ [0, 0] ] for i in range(10) ]

def domove(i):
    if i == len(rope):
        return
    
    dif = [rope[i-1][-1][0] - rope[i][-1][0], rope[i-1][-1][1] - rope[i][-1][1]]
    
    if (abs(dif[0]) > 1 or abs(dif[1]) > 1):
        new_pos = rope[i][-1]
        if dif[0] != 0 and dif[1] != 0:
            if dif[0] > 0 and dif[1] > 0:
                new_pos = [new_pos[0] + 1, new_pos[1] + 1]
            elif dif[0] > 0 and dif[1] < 0:
                new_pos = [new_pos[0] + 1, new_pos[1] - 1]
            elif dif[0] < 0 and dif[1] > 0:
                new_pos = [new_pos[0] - 1, new_pos[1] + 1]
            elif dif[0] < 0 and dif[1] < 0:
                new_pos = [new_pos[0] - 1, new_pos[1] - 1]
        
        elif abs(dif[0]) > 1 or abs(dif[1]) > 1:
            if dif[0] > 0:
                new_pos = [new_pos[0] + 1, new_pos[1] + 0]
            elif dif[0] < 0:
                new_pos = [new_pos[0] - 1, new_pos[1] + 0]
            elif dif[1] > 0:
                new_pos = [new_pos[0] + 0, new_pos[1] + 1]
            elif dif[1] < 0:
                new_pos = [new_pos[0] + 0, new_pos[1] - 1]

        rope[i].append([new_pos[0], new_pos[1]])

    domove(i+1)

if __name__ == "__main__":
    if PART == 1:
        tail_pos = [ [0, 0] ]
        head_pos = [ [0, 0] ]
        for line in sys.stdin:
            line = line[:-1].split(" ")
            # print(line)
            for i in range(int(line[1])):
                # Move the head
                new_head_pos = [head_pos[-1][0] + direction[line[0]][0], head_pos[-1][1] + direction[line[0]][1]]
                if abs(new_head_pos[0] - tail_pos[-1][0]) > 1 or abs(new_head_pos[1] - tail_pos[-1][1]) > 1:
                    tail_pos.append([head_pos[-1][0], head_pos[-1][1]])
                
                head_pos.append(new_head_pos)
        print(len(set([ (i[0], i[1]) for i in tail_pos])))
    elif PART == 2:
        for line in sys.stdin:
            line = line.rstrip().split(" ")
            for i in range(int(line[1])):
                new_head_pos = [rope[0][-1][0] + direction[line[0]][0], rope[0][-1][1] + direction[line[0]][1]]
                rope[0].append(new_head_pos)
                # Start moving and propagating the movement
                domove(1)
        print(len(set([ (i[0], i[1]) for i in rope[-1]])))

    
    
    