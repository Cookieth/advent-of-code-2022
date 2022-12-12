import sys

# O(n) time complexity
def process_tree_line_one_direction(line):
    visible = [1]
    max_height = line[0]
    for i in range(1, len(line)):
        if line[i] > max_height:
            visible.append(1)
            max_height = line[i]
        else:
            visible.append(0)
    return visible

# O(2n) = O(n) time complexity
def process_tree_line(line):
    forward_visible = process_tree_line_one_direction(line)
    backward_visible = process_tree_line_one_direction(line[::-1])
    # I feel like I could do this better in c++ using bit manipulation
    visible = []
    for i in range(len(forward_visible)):
        visible.append(forward_visible[i] or backward_visible[-i-1])
    # print("line   :\n", line[:20])
    # print("forward:\n", forward_visible[:20])
    # print("line   :\n", line[:-21:-1])
    # print("backwrd:\n", backward_visible[:20])
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

    # create a bit array for visibility of the tree map
    #   0 = hidden
    #   1 = visible
    # Horizontal slices: O(n^2)
    horz_visible = []
    for line in tree_map:
        horz_visible.append(process_tree_line(line))
    # Vertical slices: O(n^2)
    vert_visible = []
    for i in range(len(tree_map[0])):
        line = []
        for j in range(len(tree_map)):
            line.append(tree_map[j][i])
        vert_visible.append(process_tree_line(line))

    # O(n^2)
    # Now perform a logical or for horz and vertical
    for i in range(len(tree_map)):
        for j in range(len(tree_map[0])):
            horz_visible[i][j] = horz_visible[i][j] or vert_visible[j][i]

    # O(n^2)
    # Count number of ones in horz_visible
    count = 0
    for i in range(len(tree_map)):
        for j in range(len(tree_map[0])):
            if horz_visible[i][j] == 1:
                count += 1
    print(count)


    