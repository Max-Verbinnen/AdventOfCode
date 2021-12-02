def main():
  depths = [int(depth) for depth in open('input.txt').read().splitlines()]

  # Result 1
  print(calculate_increases(depths))

  # Result 2
  print(sliding_window(depths))

# Calculate the amount of increases in depth
def calculate_increases(depths):
  amount = 0

  for i in range(1, len(depths)):
    if depths[i] > depths[i - 1]: amount += 1
  
  return amount

# Calculate the amount of increases on 3-sliding window level
def sliding_window(depths):
  amount = 0
  som_three = sum(depths[:3])

  for i in range(1, len(depths)):
    som_next_three = sum(depths[i:i+3])
    if som_next_three > som_three: amount += 1
    som_three = som_next_three
  
  return amount


if __name__ == '__main__':
  main()