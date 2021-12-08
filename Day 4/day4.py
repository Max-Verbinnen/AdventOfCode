def main():
  numbers, boards = get_data('input.txt')

  # Result 1
  score = pick_numbers(numbers, boards)
  print(score)

  # Result 2
  min_case_score = last_board(numbers, boards)
  print(min_case_score)

def get_data(filename):
  with open(filename) as file:
    data = file.read().split('\n\n')
    numbers = data[0].split(',')
    boards = [board.split('\n') for board in data[1:]]
    
    for board in boards:
      for i in range(len(board)):
        board[i] = board[i].split()
    
    return numbers, boards


def pick_numbers(numbers, boards):
  for i in range(len(numbers)):
    if check_win(numbers[:i], boards): break
  
  nums, brd = check_win(numbers[:i], boards)
  return calculate_score(nums, brd)


def last_board(numbers, boards):
  won_boards = []
  idx = None

  for i in range(len(numbers)):
    if len(won_boards) == len(boards) - 1:
      idx = i; break

    for board in boards:
      rows = board
      cols = [[x[i] for x in rows] for i in range(len(board))]

      for row in rows:
        if set(row) <= set(numbers[:i]) and board not in won_boards: won_boards.append(board)

      for col in cols:
        if set(col) <= set(numbers[:i])and board not in won_boards: won_boards.append(board)
  
  diff = [x for x in boards if x not in won_boards]
  
  return calculate_score(numbers[:idx], diff[0])

  
def check_win(numbers, boards):
  for board in boards:
    rows = board
    cols = [[x[i] for x in rows] for i in range(len(board))]

    for row in rows:
      if set(row) <= set(numbers): return numbers, board

    for col in cols:
      if set(col) <= set(numbers): return numbers, board


def calculate_score(numbers, board):
  som = 0

  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] not in numbers:
        som += int(board[i][j])
  
  return som * int(numbers[-1])

if __name__ == '__main__':
  main()