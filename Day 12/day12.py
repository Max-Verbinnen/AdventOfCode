def main():
  map = open('Day 12\input.txt').read().splitlines()
  connections = build_connections(map)

  # Result 1
  print(possible_paths(connections, 1))

  # Result 2
  print(possible_paths(connections, 2))


def build_connections(map):
  connections = {} # Cave1: {cave2, ...}

  for path in map:
    x, y = path.split("-")
    if x not in connections and y != "start": connections[x] = {y}
    elif y != "start": connections[x].add(y)
    if y not in connections and x != "start": connections[y] = {x}
    elif x != "start": connections[y].add(x)
  
  return connections


def path_contains_same_small_caves(connections, path):
  # Small caves should only be visited once (= restriction 1)
  small_caves = {node for node in connections.keys() if node.islower()}
  
  return any(path.count(cave) > 1 for cave in small_caves)


def path_contains_multiple_duplicate_small_caves(connections, path):
  # 1 small cave can be visited twice and the rest only once (= restriction 2)
  small_caves = {node for node in connections.keys() if node.islower()}
  double_visit_cave = None
  
  for cave in path:
    if cave in small_caves and path.count(cave) == 2: double_visit_cave = cave
  
  return any(path.count(cave) > 1 for cave in small_caves if cave != double_visit_cave)


def possible_paths(connections, restriction, path=None, paths=None):
  if paths is None:
    paths = []
  if path is None:
    path = ["start"]

  for option in connections[path[-1]]:
    extended_path = path + [option]
    path_is_incorrect = path_contains_same_small_caves(connections, extended_path) if restriction == 1 else path_contains_multiple_duplicate_small_caves(connections, extended_path) # Condition depends on star; different with star 1 & 2

    if not path_is_incorrect:
      if extended_path[-1] == "end": paths.append(extended_path) # Full & correct path
      else: possible_paths(connections, restriction, extended_path, paths) # Partially correct path
  
  return len(paths)


if __name__ == '__main__':
  main()