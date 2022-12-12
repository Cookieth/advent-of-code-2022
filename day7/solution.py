import sys

class directory:
    def __init__(self, name):
        self.name = name
        self.file_sizes = 0
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self
    
    def add_file_size(self, size):
        self.file_sizes += size
        if self.parent is not None:
            self.parent.add_file_size(size)
    
    def get_file_sizes(self):
        return self.file_sizes
    
    def get_children(self):
        return self.children
    
    def print_tree(self):
        print(self.name, self.file_sizes)
        for child in self.children:
            child.print_tree()

# Traverse down through root directory, keep count of total size
#   If the file size is less than 100000, add it to the total size
#   If the file size is greater than 100000, ignore it
def process_tree(directory):
    if directory.file_sizes < 100000:
        total_size = directory.file_sizes
    else:
        total_size = 0

    for child in directory.children:
        total_size += process_tree(child)

    return total_size

if __name__ == "__main__":

    root_directory = directory("/")
    current_directory = root_directory
    processing_ls = False

    for line in sys.stdin:
        line = line[:-1].split(" ")
        
        if processing_ls:
            print("processing ls:", line)
            # process each line of the ls output.
            #   if it starts with "dir", process as a new directory (or ignore? we create one anyway for cd)
            #   if it starts with a number, add the number to the file size
            
            if line[0].isdigit():
                current_directory.add_file_size(int(line[0]))
            elif line[0] == "dir":
                # child_exists = False
                # for child in current_directory.get_children():
                #     if child.name == line[1]:
                #         child_exists = True
                #         break
                # if not child_exists:
                #     new_directory = directory(line[1])
                #     current_directory.add_child(new_directory)
                continue
            else:
                processing_ls = False
        
        if not processing_ls:
            # Process the cd command
            if line[0] == "$" and line[1] == "cd":
                print(line)
                if line[2] == "..":
                    print(current_directory.name)
                    current_directory = current_directory.parent
                else:
                    child_exists = False
                    print(current_directory.name)
                    for child in current_directory.get_children():
                        if child.name == line[2]:
                            current_directory = child
                            child_exists = True
                            break
                    if not child_exists:
                        new_directory = directory(line[2])
                        current_directory.add_child(new_directory)
                        current_directory = new_directory
            # Process the ls command
            elif line[0] == "$" and line[1] == "ls":
                print(line)
                processing_ls = True
    
    # root_directory.print_tree()

    total_size = process_tree(root_directory)
    print(total_size)


    