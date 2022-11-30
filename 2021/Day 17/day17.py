def main():
  min_x, max_x, min_y, max_y = 85, 145, -163, -108

  # Result 1
  print(trajectory(min_x, max_x, min_y, max_y)[0])

  # Result 2
  print(trajectory(min_x, max_x, min_y, max_y)[1])


def trajectory(min_x, max_x, min_y, max_y):
  # Assuming min_y and max_y are both negative
  all_velocities = {(x, y) for x in range(max_x + 1) for y in range(min_y, -min_y + 1)}
  possible_velocities = {}

  for vel in all_velocities:
    vel_x, vel_y = vel
    x, y = 0, 0
    y_values = set()
    within_target = False

    while x <= max_x and y >= min_y: # Otherwise probe will never reach target area
      x += vel_x
      y += vel_y
      y_values.add(y)

      # Change x velocity by 1 "towards 0"
      if vel_x != 0: vel_x = vel_x - 1 if vel_x > 0 else vel_x - 1
      vel_y -= 1

      if min_x <= x <= max_x and min_y <= y <= max_y:
        within_target = True
        break
    
    # Initial velocity that causes probe to pass through target area
    if within_target: possible_velocities[vel] = max(y_values)
    
  return max(possible_velocities.values()), len(possible_velocities)


if __name__ == '__main__':
  main()