from ast import literal_eval
import re
import math


def main():
  numbers = [literal_eval(x) for x in open('Day 18\input.txt').read().splitlines()]

  # Result 1
  print(magnitude_of_sum(numbers))

  # Result 2
  print(largest_magnitude_of_2(numbers))


def explode_pair(string, idx):
  numbers = list(re.finditer("\d+", string))
  num_1 = num_2 = left_num = right_num = None

  for num in numbers:
    value = int(num.group())
    start_idx, end_idx = num.span()
    info = {"value": value, "start": start_idx, "end": end_idx}

    if end_idx < idx: left_num = info
    if start_idx == idx + 1: num_1 = info
    if num_1 and start_idx == num_1["end"] + 2: num_2 = info
    if num_2 and start_idx > num_2["end"]: right_num = info; break
  
  new_str = string

  # Order of 3 operations is important; otherwise indices will change e.g. 7 -> 11 (1 -> 2 digits)
  if right_num: new_str = string[:right_num["start"]] + str(num_2["value"] + right_num["value"]) + string[right_num["end"]:]
  new_str = new_str[:num_1["start"] - 1] + "0" + new_str[num_2["end"] + 1:]
  if left_num: new_str = new_str[:left_num["start"]] + str(num_1["value"] + left_num["value"]) + new_str[left_num["end"]:]

  return new_str
    

def split_number(string, idx):
  # Replace number with pair: x / 2 (rounded down), x / 2 (rounded up)
  start, end = idx
  number = int(string[start:end])
  substitution = str([math.floor(number / 2), math.ceil(number / 2)])

  return string[:start] + substitution + string[end:]


def reduce(number):
  string = str(number)

  while True:
    # Check if pair is nested inside 4 pairs
    explode = (False, 0) # Second value represents index in string
    open = 0
    for i, char in enumerate(string):
      if char == "[": open += 1
      elif char == "]": open -= 1

      if open == 5:
        explode = (True, i)
        break
    
    if explode[0] is True:
      string = explode_pair(string, explode[1])
      continue

    # Check if number should be splitted
    split = (False, 0)
    for match in re.finditer("\d+", string):
      if int(match.group()) >= 10:
        split = (True, match.span())
        break
    
    if split[0] is True:
      string = split_number(string, split[1])
      continue

    # If this point is reached, string cannot be reduced any more
    break

  return literal_eval(string)


def magnitude(pair):
  # Base case: regular number instead of list
  if type(pair) != list:
    return pair
  
  return 3 * magnitude(pair[0]) + 2 * magnitude(pair[1])

  
def magnitude_of_sum(numbers):
  temporary_sum = numbers[0]

  for num in numbers[1:]:
    temporary_sum = reduce([temporary_sum, num])
  
  return magnitude(temporary_sum)


def largest_magnitude_of_2(numbers):
  largest_magnitude = 0

  # All permutations of 2 numbers
  for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
      sum_of_2 = [numbers[i], numbers[j]]
      magn = magnitude(reduce(sum_of_2))
      if magn > largest_magnitude: largest_magnitude = magn

      # Addition is not commutative i.c.
      sum_of_2_reverse = [numbers[j], numbers[i]]
      magn_reverse = magnitude(reduce(sum_of_2_reverse))
      if magn_reverse > largest_magnitude: largest_magnitude = magn_reverse
  
  return largest_magnitude


if __name__ == '__main__':
  main()