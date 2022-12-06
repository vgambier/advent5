#!/usr/bin/env python

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

def improve_crates(crates, nb_crates):
  data_crates = [[] for i in range(nb_crates)]
  for crate_line in crates:
    for i in range(nb_crates):
      candidate = crate_line[i*4+1]
      print(candidate)
      if candidate != ' ':
        data_crates[i].append(candidate)
  return data_crates

if __name__ == '__main__':

  crates, instructions, nb_crates = parse()
  
  # modify data structure for crates
  data_crates = improve_crates(crates, nb_crates)
  print(data_crates)

