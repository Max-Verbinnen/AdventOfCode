def main():
  entries = [entry.split(' ') for entry in open('input.txt').read().splitlines()]

  # Result 1
  print(unique_output_segments(entries))

  # Result 2
  print(wires_connections(entries))


def unique_output_segments(entries):
  unique_lengths = {2, 4, 3, 7}
  count = 0

  for entry in entries:
    count += len([signal for signal in entry[11:] if len(signal) in unique_lengths])

  return count
    

def wires_connections(entries):
  output = 0
  easy_numbers = {
    # Length: corresponding number
    2: 1,
    3: 7,
    4: 4,
    7: 8
  }

  for entry in entries:
    signal_mapping = {
      # Number (0 -> 9): signal
    }

    # Easy numbers with known lengths
    for signal in entry[:10]:
      if len(signal) in easy_numbers:
        signal_mapping[easy_numbers[len(signal)]] = signal
    
    # Differentiate the following numbers: 0, 6, 9
    for signal in entry[:10]:
      if len(signal) == 6:
        if not all(wire in signal for wire in signal_mapping[1]):
          signal_mapping[6] = signal
        elif all(wire in signal for wire in signal_mapping[4]):
          signal_mapping[9] = signal
        else:
          signal_mapping[0] = signal
    
    # Differentiate the following numbers: 2, 3, 5
    for signal in entry[:10]:
      if len(signal) == 5:
        if all(wire in signal for wire in signal_mapping[1]):
          signal_mapping[3] = signal
        elif all(wire in signal_mapping[6] for wire in signal):
          signal_mapping[5] = signal
        else:
          signal_mapping[2] = signal
  
    # Decode the output
    decoded = ""
    for signal in entry[11:]:
      for number, pattern in signal_mapping.items():
        if sorted(signal) == sorted(pattern):
          decoded += str(number)
          break
    
    output += int(decoded)
  
  return output


if __name__ == '__main__':
  main()