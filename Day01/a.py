def main():
	# Vars
	lastDay = 0
	answer = 0

	# open the file
	with open('input.txt') as file:
		# iterate through each line
		for line in file.readlines():
			# increase i each time the new line is bigger than the previous one
			if int(line.rstrip('\n')) > lastDay:
				answer += 1
			# update the last day value
			lastDay = int(line.rstrip('\n'))
	# print the final answer (without the first measurement)
	print("increased: {}".format(answer - 1))
	
if __name__ == "__main__":
	main()
