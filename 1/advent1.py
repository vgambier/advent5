#!/usr/bin/env python

def parse_input():
    parsed_calories = [0]
    i = 0
    with open('input.txt', 'r') as f:
        for line in f:
            if line != '\n':
                parsed_calories[i] += int(line.strip('\n'))
            else:
                i += 1
                parsed_calories.append(0)
    return parsed_calories


if __name__ == '__main__':

    calories = parse_input()
    calories.sort(reverse=True)

    max_calories = calories[0]
    top3 = max_calories + calories[1] + calories[2]

    assert max_calories == 70698
    assert top3 == 206643

    print(f"Maximum colories is {max_calories}")
    print(f"Top 3 elves carry {top3}")
