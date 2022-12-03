def main():
  sacks = [sack for sack in open('input.txt').read().splitlines()]
  
  # Result 1
  print(find_common_items(sacks))

  # Result 2
  print(find_badges(sacks))

def find_common_items(sacks):
  priorities = 0
  for sack in sacks:
    half = int(len(sack) / 2)
    char = set(sack[:half]).intersection(sack[half:]).pop()
    priorities += priority(char)

  return priorities

def find_badges(sacks):
  priorities = 0
  for i in range(0, len(sacks), 3):
    char = set(sacks[i]).intersection(sacks[i + 1]).intersection(sacks[i + 2]).pop()
    priorities += priority(char)
  
  return priorities

def priority(char):
  return ord(char) - ord('A') + 1 + (26 if char.isupper() else -32)


if __name__ == '__main__':
  main()
