import sys

# I feel like this couldbe achieved in O(n) time complexity
def process_tree_line_one_direction(line):
    # print("1:", line)
    scenic_scores = [0]
    for i in range(1, len(line)):
        value = line[i]
        num_visible = 1
        for j in reversed(range(i)):
            # Edge case: reached the end of the line
            if j == 0:
                num_visible = i
                break
            if value > line[j]:
                num_visible += 1
            else:
                break
        scenic_scores.append(num_visible)
    return scenic_scores

# O(2n) = O(n) time complexity
def process_tree_line(line):
    forward_visible = process_tree_line_one_direction(line)
    backward_visible = process_tree_line_one_direction(line[::-1])[::-1]
    # I feel like I could do this better in c++ using bit manipulation
    visible = []
    # Now MULTIPLY the scores
    for i in range(len(forward_visible)):
        visible.append(forward_visible[i] * backward_visible[i])
    # print("line   :\n", line[:20])
    # print("forward:\n", forward_visible[:20])
    # print("backwrd:\n", backward_visible[:20])
    # print("FLIPline:\n", line[-20:])
    # print("FLIPback:\n", backward_visible[-20:])
    # print("visible:\n", visible[:20])
    return visible

if __name__ == "__main__":
    tree_map = []
    for line in sys.stdin:
        tree_line = []
        for char in line[:-1]:
            tree_line.append(int(char))
        tree_map.append(tree_line)
    
    print(len(tree_map), "x", len(tree_map[0]))

    process_tree_line(tree_map[0])
    # create an array for visibility of the tree map
    #   0 = hidden
    #   1 = visible
    # Horizontal slices: O(n^2)
    horz_scenic = []
    for line in tree_map:
        horz_scenic.append(process_tree_line(line))
    # Vertical slices: O(n^2)
    vert_scenic = []
    for i in range(len(tree_map[0])):
        line = []
        for j in range(len(tree_map)):
            line.append(tree_map[j][i])
        vert_scenic.append(process_tree_line(line))

    # O(n^2)
    # Now perform a MULTIPLICATION for horz and vertical
    for i in range(len(tree_map)):
        for j in range(len(tree_map[0])):
            horz_scenic[i][j] = horz_scenic[i][j] * vert_scenic[j][i]

    # O(n^2)
    # Count number of ones in horz_visible
    print(max(max(x) for x in horz_scenic))


    