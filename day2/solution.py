import sys

PART = 2

rock_score = 1
paper_score = 2
scissors_score = 3

win_score = 6
draw_score = 3
lose_score = 0

score_dict = {'A' : rock_score, 'B' : paper_score, 'C' : scissors_score, 'X' : rock_score, 'Y' : paper_score, 'Z' : scissors_score}

if __name__ == "__main__":

    total_score = 0
    for line in sys.stdin:
        line = line.split(" ")
        line[1] = line[1][:1]

        if PART == 1:
            beats_dict = {'X' : 'C', 'Y' : 'A', 'Z' : 'B'}
            # Add the thing you chose (part 1)
            total_score += score_dict[line[1]]

            # Draw Case
            if score_dict[line[0]] == score_dict[line[1]]:
                total_score += draw_score
            elif beats_dict[line[1]] == line[0]:
                total_score += win_score
            else:
                total_score += lose_score
        elif PART == 2:
            what_beats = {'A' : 'B', 'B' : 'C', 'C' : 'A'}
            # Draw Case
            if line[1] == 'Y':
                total_score += draw_score
                total_score += score_dict[line[0]]
            elif line[1] == 'Z':
                total_score += win_score
                total_score += score_dict[what_beats[line[0]]]
            else:
                total_score += lose_score
                total_score += score_dict[what_beats[what_beats[line[0]]]]
    
    print(f"Total Score for Part {PART}: {total_score}")

