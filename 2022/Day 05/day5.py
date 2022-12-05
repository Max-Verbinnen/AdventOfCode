import re

def main():
  crates, moves = [line.splitlines() for line in open("input.txt").read().split("\n\n")]
  stacks = parse_lines(crates[:-1])

  # Result 1 & 2
  print(move_crates(stacks, moves))

def parse_lines(lines):
  stacks = [[] for _ in range(9)]
  for line in lines:
    [stacks[i // 4].insert(0, line[i]) for i in range(1, len(line), 4) if line[i] != " "]
  
  return stacks

def move_crates(stacks, moves):
  stacks_copy = [stack[:] for stack in stacks]
  for move in moves:
    amt, src, dest = map(int, re.findall("(\d+)", move))
    for _ in range(amt):
      stacks[dest - 1].append(stacks[src - 1].pop())
    stacks_copy[dest - 1] += stacks_copy[src - 1][-amt:]
    del stacks_copy[src - 1][-amt:]
  
  return ["".join(stack[-1] for stack in stacks) for stacks in [stacks, stacks_copy]]


if __name__ == "__main__":
  main()
