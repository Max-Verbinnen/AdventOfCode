from functools import reduce


def main():
  code = open('Day 16\input.txt').read()
  transmission = Transmission(code)
  result = transmission.decode_packet()

  # Result 1
  print(transmission.versions_sum)

  # Result 2
  print(result)
  

hex_to_bin = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}


class Transmission:
  def __init__(self, hex):
    self.code = ""
    for char in hex: self.code += hex_to_bin[char]

    self.read = 0 # Total read bits
    self.versions_sum = 0

  def get_bits(self, n):
    self.read += n
    bits = self.code[:n]
    self.code = self.code[n:]

    return bits

  def decode_bits(self, binary_code):
    return int(binary_code, 2)

  def get_literal(self):
    literal_value = ""

    while True:
      prefix = self.decode_bits(self.get_bits(1))
      literal_value += self.get_bits(4)
      if prefix == 0: break

    return self.decode_bits(literal_value)
  
  def get_value_per_type(self, id, literals):
    value = 0

    match id:
      case 0:
        value = sum(literals)
      case 1:
        value = reduce(lambda x, y: x * y, literals)
      case 2:
        value = min(literals)
      case 3:
        value = max(literals)
      case 5:
        value = int(literals[0] > literals[1])
      case 6:
        value = int(literals[0] < literals[1])
      case 7:
        value = int(literals[0] == literals[1])
    
    return value

  def decode_packet(self):
    version = self.decode_bits(self.get_bits(3))
    id = self.decode_bits(self.get_bits(3))
    self.versions_sum += version
    value = 0

    # Literal value
    if id == 4:
      value = self.get_literal()
    
    # Operator packet
    else:
      length_type_id = self.decode_bits(self.get_bits(1))
      literals = []

      if length_type_id == 0:
        total_length = self.decode_bits(self.get_bits(15))
        current = self.read

        while self.read < current + total_length:
          literals.append(self.decode_packet())

      elif length_type_id == 1:
        subpackets = self.decode_bits(self.get_bits(11))

        for _ in range(subpackets):
          literals.append(self.decode_packet())

      value = self.get_value_per_type(id, literals)
    
    return value


if __name__ == '__main__':
  main()