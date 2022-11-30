from collections import Counter


def main():
  data = open('Day 13\input.txt').read().splitlines()
  dots, instructions = data[:data.index("")], data[data.index("") + 1:]
  paper = build_paper(dots)

  # Result 1
  print(dots_after_first_fold(paper, instructions))

  # Result 2
  print_code_after_all_folds(paper, instructions)


def build_paper(dots):
  max_x, max_y = 0, 0

  # Find maximum dimensions
  for dot in dots:
    x, y = map(int, dot.split(","))
    if x > max_x: max_x = x
    if y > max_y: max_y = y
  
  paper = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]
  
  # Mark the dots
  for dot in dots:
    x, y = map(int, dot.split(","))
    paper[y][x] = "#"
  
  return paper


def get_dots(paper):
  dots = []

  for i in range(len(paper)):
    for j in range(len(paper[0])):
      if paper[i][j] == "#":
        dots.append(f"{j},{i}")
  
  return dots


def fold(paper, instruction):
  line_number = int(instruction.split("=")[1])

  for dot in get_dots(paper):
    x, y = map(int, dot.split(","))
    if "y" in instruction and y > line_number and x < len(paper[0]) and y < len(paper): # Fold along y-axis (up)
      paper[line_number - (y - line_number)][x] = "#"
    elif "x" in instruction and x > line_number and x < len(paper[0]) and y < len(paper): # Fold along x-axis (left)
      paper[y][line_number - (x - line_number)] = "#"

  paper = paper[:line_number] if "y" in instruction else [row[:line_number] for row in paper]
  return paper


def dots_after_first_fold(paper, instructions):
  paper = fold(paper, instructions[0])

  # Count dots (aka #'s)
  return dict(sum(map(Counter, paper), Counter()))["#"]


def print_code_after_all_folds(paper, instructions):
  for instruction in instructions:
    paper = fold(paper, instruction)
  
  for row in paper:
    print(row)


if __name__ == '__main__':
  main()