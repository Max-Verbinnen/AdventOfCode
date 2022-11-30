from heapq import heappop, heappush


def main():
  risk_levels = [list(map(int, list(entry))) for entry in open('Day 15\input.txt').read().splitlines()]

  # Result 1
  print(lowest_risk_dijkstra(risk_levels))

  # Result 2
  print(extend_area_and_calculate_lowest_risk(risk_levels))


def lowest_risk_dijkstra(grid): # (see https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/)
  all_indices = {(i, j) for i in range(len(grid)) for j in range(len(grid))}
  distances = {idx: (0 if idx == (0, 0) else float("inf")) for idx in all_indices}
  goal = (len(grid) - 1, len(grid) - 1)

  # Priority queue
  pq = [(0, (0, 0))]
  
  while len(pq) > 0:
    current_distance, current_pos = heappop(pq)

    if current_distance > distances[current_pos]:
      continue
    
    # Retrieve child nodes
    neighbours = set()
    x, y = current_pos
    
    if x - 1 >= 0: neighbours.add((x - 1, y))
    if x + 1 < len(grid): neighbours.add((x + 1, y))
    if y - 1 >= 0: neighbours.add((x, y - 1))
    if y + 1 < len(grid): neighbours.add((x, y + 1))

    # Calculate distance through current node to unvisited neighbours
    for neighbour in neighbours:
      distance = current_distance + grid[neighbour[0]][neighbour[1]]
      
      if distance < distances[neighbour]:
        distances[neighbour] = distance
        heappush(pq, (distance, neighbour))
  
  return distances[goal]


def extend_area_and_calculate_lowest_risk(grid):
  extended = []
  for i in range(len(grid) * 5):
    row = list(map(lambda x: x % 9 if x > 9 else x, # Everything > 9 should wrap back around to 1
      [grid[i % len(grid)][j % len(grid)] + i // len(grid) + j // len(grid) for j in range(len(grid) * 5)]
    ))
    extended.append(row)
  
  return lowest_risk_dijkstra(extended)


if __name__ == '__main__':
  main()