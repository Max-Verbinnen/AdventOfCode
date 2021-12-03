def main():
  rate = [bits for bits in open('input.txt').read().splitlines()]

  # Result 1
  print(generate_report(rate))

  # Result 2
  print(life_support(rate))
    
def generate_report(rate):
  gamma_rate = []

  for i in range(len(rate[0])):
    col = [bit[i] for bit in rate]
    gamma_rate.append(1) if (col.count('1') > col.count('0')) else gamma_rate.append(0)
  
  epsilon_rate = list(map(lambda x: 1 - int(x), gamma_rate))
  
  gamma_rate = ''.join(str(bit) for bit in gamma_rate)
  epsilon_rate = ''.join(str(bit) for bit in epsilon_rate)
  
  return int(gamma_rate, 2) * int(epsilon_rate, 2)

def life_support(rate):
  oxygen = [sequence for sequence in rate]
  scrubber = [sequence for sequence in rate]

  for i in range(len(rate[0])):
    most_common_bit = 1 if [bit[i] for bit in oxygen].count('1') >= [bit[i] for bit in oxygen].count('0') else 0
    least_common_bit = 0 if [bit[i] for bit in scrubber].count('0') <= [bit[i] for bit in scrubber].count('1') else 1

    if len(oxygen) > 1: oxygen = list(filter(lambda x: int(x[i]) == most_common_bit, oxygen))
    if len(scrubber) > 1: scrubber = list(filter(lambda x: int(x[i]) == least_common_bit, scrubber))
  
  return int(''.join(oxygen), 2) * int(''.join(scrubber), 2)

if __name__ == '__main__':
  main()