def main():
  packet = open('input.txt').read()
  
  # Result 1 & 2
  print(first_marker(packet, 4), first_marker(packet, 14))

def first_marker(packet, n):
  for i in range(0, len(packet)):
    if len(set(packet[i:i+n])) == n:
      return i + n


if __name__ == '__main__':
  main()
