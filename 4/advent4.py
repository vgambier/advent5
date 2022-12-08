#!/usr/bin/env python

def parse_input():
    pairs = []
    with open('input.txt', 'r') as f:
        for line in f:
            pairs.append(line.strip('\n'))
    return pairs


def visualize(_range):
    debug = [' ' for i in range(99)]
    debug[_range[0]:_range[1] + 1] = '-' * (_range[1] - _range[0] + 1)
    return ''.join(debug)


if __name__ == '__main__':

    task_pairs = parse_input()

    nb_full_overlaps = 0
    nb_overlaps = 0

    for task_pair in task_pairs:
        sections = task_pair.split(',')
        first_range = list(map(int, sections[0].split('-')))
        second_range = list(map(int, sections[1].split('-')))
        a = first_range[0]
        b = first_range[1]
        c = second_range[0]
        d = second_range[1]

        if (a >= c and b <= d) or (a <= c and b >= d):
            nb_full_overlaps += 1

        if (a <= c <= b) or (a <= d <= b) or (c <= a <= d) or (c <= b <= d):
            nb_overlaps += 1

    assert nb_full_overlaps == 500
    assert nb_overlaps == 815

    print(f"Amount of assignment pairs where one range fully contain the other: {nb_full_overlaps}")
    print(f"Amount of assignment pairs with some overlap: {nb_overlaps}")
