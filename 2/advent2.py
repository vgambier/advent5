#!/usr/bin/env python

def parse_input():
    parsed_rounds = []
    with open('input.txt', 'r') as f:
        for line in f:
            parsed_rounds.append(line.strip('\n').split())
    return parsed_rounds


if __name__ == '__main__':

    # Part 1
    rounds = parse_input()
    scoring = {
        "A": {"X": 4, "Y": 8, "Z": 3},
        "B": {"X": 1, "Y": 5, "Z": 9},
        "C": {"X": 7, "Y": 2, "Z": 6}
    }
    score = 0
    for _round in rounds:
        score += scoring[_round[0]][_round[1]]
    print(f"Incorrect score is {score}")

    # Part 2

    true_scoring = {
        "A": {"X": 3, "Y": 4, "Z": 8},
        "B": {"X": 1, "Y": 5, "Z": 9},
        "C": {"X": 2, "Y": 6, "Z": 7}
    }
    true_score = 0
    for _round in rounds:
        true_score += true_scoring[_round[0]][_round[1]]
    print(f"Correct score is {true_score}")
