import sys

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.headval = None
        self.tailval = None

    def append(self, node):
        if self.tailval is not None:
            self.tailval.nextval = node
        else:
            self.headval = node
        self.tailval = node
    
    def push_front(self, node):
        if self.headval is not None:
            node.nextval = self.headval
            self.headval = node
        else:
            self.headval = node
            self.tailval = node
    
    def pop_front(self):
        node = self.headval
        if self.headval is not None:
            if self.headval.next is None:
                self.tailval = None
            self.headval = self.headval.next
        return node

    def print_list(self):
        node = self.headval
        while node is not None:
            print(node.dataval, end = "->")
            node = node.nextval
        print("")

indices = [1, 5, 9, 13, 17, 21, 25, 29, 33]

# Set up linked lists
linkedlists = [LinkedList()]
for i in range(8):
    linkedlists.append(LinkedList())

if __name__ == "__main__":

    # Setup
    for i, line in enumerate(sys.stdin):
        if i == 8:
            break
        for column, index in enumerate(indices):
            if line[index] != " ":
                linkedlists[column].append(Node(line[index]))
    
    for list in linkedlists:
        list.print_list()

    for line in sys.stdin:
        if line != "\n":
            line = line.split(" ")
            num_to_move = int(line[1])
            src = int(line[3]) - 1
            dst = int(line[5]) - 1
            print(num_to_move, src + 1, dst + 1)

            src_ll = linkedlists[src]
            dst_ll = linkedlists[dst]

            src_ll.print_list()

            node = src_ll.headval
            for i in range(num_to_move - 1):
                node = node.nextval
            
            print("LAST ITEM:", node.dataval)

            # Move the pointers around
            tmp_node = node.nextval
            node.nextval = linkedlists[dst].headval
            linkedlists[dst].headval = linkedlists[src].headval
            linkedlists[src].headval = tmp_node

            # Remove debug
            src_ll = linkedlists[src]
            print("src: ", end="")
            src_ll.print_list()
            dst_ll = linkedlists[dst]
            print("dst: ", end="")
            dst_ll.print_list()

        print("")

    for list in linkedlists:
        list.print_list()

    for list in linkedlists:
        # list.print_list()
        if list.headval is not None:
            print(list.headval.dataval, end="")
    print("")
                


    