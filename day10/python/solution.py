import sys

PART = 2

# The following assumed pipelining:

# if __name__ == "__main__":
#     time = 0
#     value = 1
#     events = {}

#     while True:
#         line = sys.stdin.readline()

#         time += 1
#         print(f"==={time}===")
        
#         if len(events) == 0 and line is "":
#             break
        
#         # Process operations
#         if line is not None:
#             line = line[:-1].split(" ")
#             print(line)
#             # Process Input
#             # if line[0] == "noop":
#                 # Asdf

#             if line[0] == "addx":
#                 events[time + 2] = int(line[1])
        
#         # Process Events operations
#         if len(events) != 0:
#             if time in events:
#                 event = events.pop(time)
#                 print("ADDING:", event)
#                 value += event 
        
#         # debug print:
#         print(f"Line: {line}, Time: {time}, Value: {value}, Events: {events}")
    
# The following doesn't pipeline

if __name__ == "__main__":
    time = 0
    value = 1
    scores = []

    if PART == 1:
        def tick():
            global time
            time += 1
            if time == 20 or (time - 20) % 40 == 0:
                scores.append(value * time)
                print(f"Value at: {time} is {scores[-1]}")
            print(f"Sum: {sum(scores)}")
    else:
        def tick():
            global time
            global value

            # Display
            if (time + 1) % 40 == 0:
                print("")
            elif value - 1 == time % 40 or value == time % 40 or value + 1 == time % 40:
                print("#", end="")
            else:
                print(".", end="")

            time += 1
            
    for line in sys.stdin:
        line = line[:-1].split(" ")
        # print(line)
        if line[0] == "noop":
            tick()

        if line[0] == "addx":
            tick()
            tick()
            value += int(line[1])
