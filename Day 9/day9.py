from functools import reduce


def main():
  heightmap = [list(map(int, list(entry))) for entry in open('input.txt').read().splitlines()]

  # Result 1
  print(risk_level_of_low_points(heightmap))

  # Result 2
  print(find_basins(heightmap))


def find_low_points(map):
  low_points = set() # Contains tuples of indices of low points

  for i in range(len(map)):
    for j in range(len(map[0])):
      if ((i - 1 >= 0 and map[i - 1][j] > map[i][j]) or (i - 1 < 0)) \
          and ((i + 1 < len(map) and map[i + 1][j] > map[i][j]) or (i + 1 >= len(map))) \
          and ((j - 1 >= 0 and map[i][j - 1] > map[i][j]) or (j - 1 < 0)) \
          and ((j + 1 < len(map[0]) and map[i][j + 1] > map[i][j]) or (j + 1 >= len(map[0]))):
        low_points.add((i, j))
  
  return low_points
 

def risk_level_of_low_points(map):
  low_points = find_low_points(map)

  # Sum of low points + 1
  return sum(map[x][y] + 1 for x, y in low_points)


def find_basins(map):
  low_points = find_low_points(map)
  basin_sizes = []
  
  for point in low_points:
    basin_sizes.append(len(extend_basin(map, point)))
  
  largest_three = sorted(basin_sizes, reverse=True)[:3]

  # Product of lengths of 3 largest basins
  return reduce(lambda x, y: x * y, largest_three)


def extend_basin(map, point, basin=None):
  if basin is None:
    basin = [point]

  if point not in basin:
    basin.append(point)
  x, y = point
  
  # Check whether adjacent point has a valid index and a strictly greater height but not 9
  if x - 1 >= 0 and map[x - 1][y] != 9 and map[x - 1][y] > map[x][y]: extend_basin(map, (x - 1, y), basin)
  if x + 1 < len(map) and map[x + 1][y] != 9 and map[x + 1][y] > map[x][y]: extend_basin(map, (x + 1, y), basin)
  if y - 1 >= 0 and map[x][y - 1] != 9 and map[x][y - 1] > map[x][y]: extend_basin(map, (x, y - 1), basin)
  if y + 1 < len(map[0]) and map[x][y + 1] != 9 and map[x][y + 1] > map[x][y]: extend_basin(map, (x, y + 1), basin)

  return basin


if __name__ == '__main__':
  main()