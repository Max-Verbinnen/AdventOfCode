def main():
  pairs = [[list(map(int, x.split('-'))) for x in pair.split(',')] for pair in open('input.txt').read().splitlines()]
  
  # Result 1 & 2
  print(analyse_pairs(pairs))

def analyse_pairs(pairs):
  contains, overlaps = 0, 0
  for pair in pairs:
    s1, e1, s2, e2 = pair[0][0], pair[0][1], pair[1][0], pair[1][1]
    if (s1 >= s2 and e1 <= e2) or (s2 >= s1 and e2 <= e1):
      contains += 1
    if s2 <= s1 <= e2 or s1 <= s2 <= e1:
      overlaps += 1
  
  return contains, overlaps


if __name__ == '__main__':
  main()
