def main():
  commands = [comm for comm in open('input.txt').read().splitlines()]

  # Result 1
  print(calculate_position(commands))

  # Result 2
  print(calculate_position_with_aim(commands))

# Interpret commands & multiply final horizontal position and depth
def calculate_position(commands):
  horizontal, depth = 0, 0

  for command in commands:
    action, step = command.split(' ')

    match action:
      case 'forward': horizontal += int(step)
      case 'up': depth -= int(step)
      case 'down': depth += int(step)
  
  return horizontal * depth

# Extended with aim
def calculate_position_with_aim(commands):
  horizontal, depth, aim = 0, 0, 0

  for command in commands:
    action, x = command.split(' ')

    match action:
      case 'forward': horizontal += int(x); depth += (aim * int(x))
      case 'up': aim -= int(x)
      case 'down': aim += int(x)
  
  return horizontal * depth


if __name__ == '__main__':
  main()