#!/usr/bin/env python

def contains_number():
  print("hey")

def parse():

  crates = []
  instructions = []

  with open('input.txt', 'r') as f:
    for line in f:
      if any(char.isdigit() for char in line):
        instructions.append(line.strip('\n'))
      else:
        crates.append(line.strip('\n'))
      
  return crates[:-1], instructions[1:]

if __name__ == '__main__':
  crates, instructions = parse()
  print(crates)
  print(instructions)
