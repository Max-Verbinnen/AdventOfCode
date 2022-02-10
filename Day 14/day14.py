from collections import Counter


def main():
  data = open('Day 14\input.txt').read().splitlines()
  template, insertions = data[0], {key: value for (key, value) in set(map(lambda x: tuple(x.split(" -> ")), data[2:]))}

  # Result 1
  print(grow_polymer(template, insertions, 10))

  # Result 2
  print(grow_polymer(template, insertions, 40))


def grow_polymer(template, insertions, iterations):
  # Initial pairs
  pairs = Counter()

  for i in range(len(template) - 1):
    pairs[template[i] + template[i + 1]] += 1
  
  # Update pairs in each step
  for _ in range(iterations):
    extended_pairs = Counter()

    for pair in pairs:
      extended_pairs[pair[0] + insertions[pair]] += pairs[pair]
      extended_pairs[insertions[pair] + pair[1]] += pairs[pair]
    
    pairs = extended_pairs
  
  # We need a counter of the individual letters (<-> pairs)
  letters = Counter()

  for pair in pairs:
    letters[pair[0]] += pairs[pair]
  letters[template[-1]] += 1 # Notice that the final letter is not part of a pair

  return max(letters.values()) - min(letters.values())


if __name__ == '__main__':
  main()