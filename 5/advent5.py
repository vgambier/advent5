#!/usr/bin/env python

import copy
def parse():
    crates = []
    instructions = []

    with open('input.txt', 'r') as f:
        for line in f:
            if any(char.isdigit() for char in line):
                instructions.append(line.strip('\n'))
            else:
                crates.append(line.strip('\n'))

    return crates[:-1], instructions[1:], int(instructions[0][-2])


def modelize_crates(crates, nb_crates):
    data_crates = [[] for i in range(nb_crates)]
    for crate_line in crates:
        for i in range(nb_crates):
            candidate = crate_line[i * 4 + 1]
            if candidate != ' ':
                data_crates[i].append(candidate)
    return data_crates


def modelize_instructions(instructions):
    cpu_instructions = []
    for instruction in instructions:
        splitted = instruction.split()
        cpu_instructions.append([splitted[1], splitted[3], splitted[5]])
    return cpu_instructions


def apply_instructions_9000(data_crates, cpu_instructions):
    for instruction in cpu_instructions:
        steps = int(instruction[0])
        origin = int(instruction[1]) - 1
        destination = int(instruction[2]) - 1
        for i in range(steps):
            data_crates[destination].insert(0, data_crates[origin].pop(0))
    return data_crates


def apply_instructions_9001(data_crates, cpu_instructions):
    for instruction in cpu_instructions:
        steps = int(instruction[0])
        origin = int(instruction[1]) - 1
        destination = int(instruction[2]) - 1
        data_crates[destination][:0] = data_crates[origin][:steps]
        data_crates[origin] = data_crates[origin][steps:]
    return data_crates


if __name__ == '__main__':

    crates, instructions, nb_crates = parse()
    data_crates = modelize_crates(crates, nb_crates)
    data_crates_copy = copy.deepcopy(data_crates)
    cpu_instructions = modelize_instructions(instructions)

    apply_instructions_9000(data_crates, cpu_instructions)
    top_9000 = ''.join(row[0] if len(row) > 0 else '' for row in data_crates)
    assert top_9000 == "ZRLJGSCTR"
    print(f"Top of crates following 9000 procedure is {top_9000}")

    apply_instructions_9001(data_crates_copy, cpu_instructions)
    top_9001 = ''.join(row[0] if len(row) > 0 else '' for row in data_crates_copy)
    assert top_9001 == "PRTTGRFPB"
    print(f"Top of crates following 9001 procedure is {top_9001}")
