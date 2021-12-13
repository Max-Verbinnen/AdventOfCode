def main():
  positions = [int(pos) for pos in open('input.txt').read().split(',')]

  # Result 1
  print(least_fuel(positions))

  # Result 2
  print(least_fuel_linear(positions))


def least_fuel(positions):
  min_fuel = float("inf")

  for pos in range(0, max(positions) + 1):
    fuel = sum([abs(pos - val) for val in positions])

    if fuel < min_fuel:
      min_fuel = fuel
  
  return min_fuel


def least_fuel_linear(positions):
  min_fuel = float("inf")

  for pos in range(0, max(positions) + 1):
    fuel = int(sum([(abs(pos - val) * (abs(pos - val) + 1)) / 2 for val in positions]))
    
    if fuel < min_fuel:
      min_fuel = fuel
  
  return min_fuel


if __name__ == '__main__':
  main()