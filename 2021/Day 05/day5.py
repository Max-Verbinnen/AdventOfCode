def main():
  lines = [line.split(' -> ') for line in open('input.txt').read().splitlines()]
  
  # Result
  print(overlapping_points(lines))


def overlapping_points(lines):
  grid = {}
  
  for line in lines:
    x1, y1 = int(line[0].split(',')[0]), int(line[0].split(',')[1])
    x2, y2 = int(line[1].split(',')[0]), int(line[1].split(',')[1])
    
    if x1 == x2:
      for i in range(min(y1, y2), max(y1, y2) + 1):
        grid[(x1, i)] = 1 if (x1, i) not in grid else grid[(x1, i)] + 1
    
    elif y1 == y2:
      for i in range(min(x1, x2), max(x1, x2) + 1):
        grid[(i, y1)] = 1 if (i, y1) not in grid else grid[(i, y1)] + 1
    
    # Descending diagonal
    elif x1 - x2 == y1 - y2:
      for i in range(min(x1, x2), max(x1, x2) + 1):
        pos = (i, min(y1, y2) + (i - min(x1, x2)))
        grid[pos] = 1 if pos not in grid else grid[pos] + 1

    # Ascending diagonal
    elif x1 - x2 == -(y1 - y2):
      for i in range(min(x1, x2), max(x1, x2) + 1):
        pos = (i, max(y1, y2) - (i - min(x1, x2)))
        grid[pos] = 1 if pos not in grid else grid[pos] + 1
  
  overlapping = {point for point in grid if grid[point] >= 2}
  
  return len(overlapping)

if __name__ == '__main__':
  main()