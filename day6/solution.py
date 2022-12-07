import sys

# Template for AOC

char_freq = {}
unique_count = 0

# solution for 4: 1262
# solution for 14: 3444
n = 14

if __name__ == "__main__":
    # Just one line
    for line in sys.stdin:
        for i, char in enumerate(line):
            # print("add:", char)
            # Setup first 4
            if char not in char_freq:
                char_freq[char] = 1
                unique_count += 1
            else:
                char_freq[char] += 1
            # Remove the trailing end
            if i > n - 1:
                # print("remove:", line[i - n])
                char_freq[line[i - n]] -= 1
                if(char_freq[line[i - n]] == 0):
                    char_freq.pop(line[i - n])
                    unique_count -= 1
                # print("unique:", unique_count)
            if unique_count == n:
                print(i+1)
                break
