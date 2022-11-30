def main():
  timers = [int(timer) for timer in open('input.txt').read().split(',')]

  # Result 1
  print(amount_of_lanternfish(timers.copy(), 80))

  # Result 2
  print(efficient_solution(timers.copy(), 256))


def amount_of_lanternfish(timers, days):
  data = timers
  
  for _ in range(days):
    for j in range(len(data)):
      if data[j] != 0: data[j] -= 1
      else:
        data[j] = 6
        data.append(8)
  
  return len(data)


def efficient_solution(data, days):
  status = [data.count(i) for i in range(9)]

  for _ in range(days):
    status = status[1:] + status[:1]
    status[6] += status[-1]

  return sum(status)


if __name__ == '__main__':
  main()