import sys

PART = 2

if __name__ == "__main__":

    total_sum = 0

    group_num = 0
    group_rucksack = [{}]

    group_set = {}

    for line_num, line in enumerate(sys.stdin):

        if(PART == 1):
            size = int(len(line)/2)
            rucksack = {}
            item = ""

            # First pass, register all in first rucksack
            for i in range(size):
                char = line[i]
                # Create a frequency graph
                if char in rucksack:
                    rucksack[char] += 1
                else:
                    rucksack[char] = 1

            # Second pass, register all in second rucksack
            for i in range(size):
                char = line[i + size]
                # Create a frequency graph
                if char in rucksack:
                    item = char
                    break
            
            # Convert number to integer
            if(ord(item) <= 90):
                total_sum += ord(item) - 65 + 27
            else:
                total_sum += ord(item) - 97 + 1
        else:
            # Create a set, keep intersecting
            if line_num % 3 == 0:
                group_set = set(line[:-1])
            else:
                curr_set = set(line[:-1])
                group_set = curr_set.intersection(group_set)

            # Determine the badge
            if line_num % 3 == 2:
                badge = group_set.pop()
                if(ord(badge) <= 90):
                    total_sum += ord(badge) - 65 + 27
                else:
                    total_sum += ord(badge) - 97 + 1
                group_num += 1  

    print(f"Sum: {total_sum}")
        
