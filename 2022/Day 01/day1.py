def main():
	calories = [sum(list(map(int, cal.split('\n')))) for cal in open('input.txt').read().split('\n\n')]
	calories.sort(reverse=True)

  # Result 1
	print(calories[0])

	# Result 2
	print(sum(calories[:3]))


if __name__ == '__main__':
	main()
