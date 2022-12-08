DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def main():
  grid = [list(map(int, list(row))) for row in open('input.txt').read().splitlines()]
  
  # Result 1
  print(visible_trees(grid))

  # Result 2
  print(max_scenic_score(grid))

def visible_trees(grid):
  n, m = len(grid), len(grid[0])
  trees = 0
  for i in range(n):
    for j in range(m):
      for dx, dy in DIRECTIONS:
        curr_i, curr_j = i + dx, j + dy
        visible = True
        while curr_i in range(n) and curr_j in range(m):
          if grid[curr_i][curr_j] >= grid[i][j]:
            visible = False
            break
          curr_i += dx
          curr_j += dy
        if visible:
          trees += 1
          break

  return trees

def max_scenic_score(grid):
  n, m = len(grid), len(grid[0])
  max_scenic = 0
  for i in range(n):
    for j in range(m):
      scenic = 1
      for dx, dy in DIRECTIONS:
        curr_i, curr_j = i + dx, j + dy
        score = 0
        while curr_i in range(n) and curr_j in range(m):
          score += 1
          if grid[curr_i][curr_j] >= grid[i][j]:
            break
          curr_i += dx
          curr_j += dy
        scenic *= score
      max_scenic = max(max_scenic, scenic)
  
  return max_scenic


if __name__ == '__main__':
  main()
