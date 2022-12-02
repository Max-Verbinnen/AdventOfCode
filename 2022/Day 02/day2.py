scores = {'A X': 4, 'A Y': 8, 'A Z': 3, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 7, 'C Y': 2, 'C Z': 6}
scores_v2 = {'A X': 3, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7}

def main():
  rounds = [round for round in open('input.txt').read().splitlines()]

  # Result 1
  print(sum(map(lambda round: scores[round], rounds)))

  # Result 2
  print(sum(map(lambda round: scores_v2[round], rounds)))


if __name__ == '__main__':
  main()
