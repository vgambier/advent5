#!/usr/bin/env python

import re


def parse_input():
    with open('input_example.txt', 'r') as f:
        return f.readline()


def has_duplicate_characters(string):
    return len(string) != len(set(string))


def find_among_unique(size):
    i = 0
    while i < len(buffer):
        current_candidate = buffer[i:i + size]
        if not has_duplicate_characters(current_candidate):
            break
        i += 1
    return i + size  # the system required one-indexing and is looking for the end of the marker


if __name__ == '__main__':
    buffer = parse_input()

    marker_position = find_among_unique(4)
    start_of_message_marker = find_among_unique(14)

    assert marker_position == 1262
    assert start_of_message_marker == 3444

    print(f"Marker position: {marker_position}")
    print(f"Start of message position: {start_of_message_marker}")
