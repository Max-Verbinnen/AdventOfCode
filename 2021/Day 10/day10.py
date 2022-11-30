def main():
  lines = open('input.txt').read().splitlines()

  # Result 1
  print(syntax_error_scores(lines))

  # Result 2
  print(autocomplete_scores(lines))


score_mapping = {")": 3, "]": 57, "}": 1197, ">": 25137}
autocomplete_mapping = {")": 1, "]": 2, "}": 3, ">": 4}
inverse_character = {"(": ")","[": "]","{": "}","<": ">"}


def invalid_character(line):
  should_close_with = []

  for char in line:
    if char in inverse_character.keys(): # If character is 'open' (e.g. "<")
      should_close_with.append(inverse_character[char])
    else: # If character is 'closed' (e.g. ">")
      if char == should_close_with[-1]:
        should_close_with.pop()
      else:
        return char


def syntax_error_scores(lines):
  scores = 0

  for line in lines:
    score = invalid_character(line)
    scores += score_mapping[score] if score else 0
  
  return scores


def autocomplete_line(line):
  if invalid_character(line): return False

  should_close_with = []

  for char in line:
    if char in inverse_character.keys(): # If character is 'open' (e.g. "<")
      should_close_with.append(inverse_character[char])
    else: # If character is 'closed' (e.g. ">")
      if char == should_close_with[-1]:
        should_close_with.pop()
  
  return ''.join(list(reversed(should_close_with)))


def autocomplete_scores(lines):
  scores = []

  for line in lines:
    addition = autocomplete_line(line)

    score = 0
    if addition:
      for char in addition:
        score *= 5
        score += autocomplete_mapping[char]
    
    if score != 0: scores.append(score)

  # Middle score
  return sorted(scores)[len(scores) // 2]


if __name__ == '__main__':
  main()