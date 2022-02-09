def main():
  octopuses = [list(map(int, list(entry))) for entry in open('Day 11\input.txt').read().splitlines()]

  # Result 1
  print(amount_of_flashes(octopuses))

  # Result 2
  print(simultaneous_flashes(octopuses))


def is_within_bounds(octopuses, position):
  x, y = position

  return x >= 0 and x < len(octopuses) and y >= 0 and y < len(octopuses)
  

def flash(octopuses, position):
  x, y = position

  # All directions (even diagonal)
  if is_within_bounds(octopuses, (x - 1, y)) and octopuses[x - 1][y] != 10: octopuses[x - 1][y] += 1
  if is_within_bounds(octopuses, (x + 1, y)) and octopuses[x + 1][y] != 10: octopuses[x + 1][y] += 1
  if is_within_bounds(octopuses, (x, y - 1)) and octopuses[x][y - 1] != 10: octopuses[x][y - 1] += 1
  if is_within_bounds(octopuses, (x, y + 1)) and octopuses[x][y + 1] != 10: octopuses[x][y + 1] += 1
  if is_within_bounds(octopuses, (x - 1, y - 1)) and octopuses[x - 1][y - 1] != 10: octopuses[x - 1][y - 1] += 1
  if is_within_bounds(octopuses, (x - 1, y + 1)) and octopuses[x - 1][y + 1] != 10: octopuses[x - 1][y + 1] += 1
  if is_within_bounds(octopuses, (x + 1, y - 1)) and octopuses[x + 1][y - 1] != 10: octopuses[x + 1][y - 1] += 1
  if is_within_bounds(octopuses, (x + 1, y + 1)) and octopuses[x + 1][y + 1] != 10: octopuses[x + 1][y + 1] += 1

  # Increment flasher itself
  octopuses[x][y] += 1


def contains_flashers(octopuses):
  for i in range(len(octopuses)):
    for j in range(len(octopuses)):
      if octopuses[i][j] == 10:
        return (i, j)
  
  return False


def amount_of_flashes(octopuses):
  amount_of_flashes = 0

  for _ in range(100):
    # Increase level of each octopus by 1
    octopuses = [[energy + 1 for energy in row] for row in octopuses]

    # If energy > 9 -> flash!
    while contains_flashers(octopuses):
      i, j = contains_flashers(octopuses)
      flash(octopuses, (i, j))
    
    # Set energy of flashed octopuses to 0
    for i in range(len(octopuses)):
      for j in range(len(octopuses)):
        if octopuses[i][j] > 9:
          octopuses[i][j] = 0
          amount_of_flashes += 1
  
  return amount_of_flashes


def not_simultaneous(octopuses):
  for row in octopuses:
    for energy in row:
      if energy != 0:
        return True
  
  return False


def simultaneous_flashes(octopuses):
  step = 0

  while not_simultaneous(octopuses):
    # Increase level of each octopus by 1
    octopuses = [[energy + 1 for energy in row] for row in octopuses]

    # If energy > 9 -> flash!
    while contains_flashers(octopuses):
      i, j = contains_flashers(octopuses)
      flash(octopuses, (i, j))
    
    # Set energy of flashed octopuses to 0
    for i in range(len(octopuses)):
      for j in range(len(octopuses)):
        if octopuses[i][j] > 9:
          octopuses[i][j] = 0
    
    step += 1
  
  return step


if __name__ == '__main__':
  main()