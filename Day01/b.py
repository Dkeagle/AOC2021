def main():
	# Vars
	lastThreeDay = 0
	answer = 0

	# open the file
	with open('input.txt') as file:
		lines = file.readlines()
		for i in range(0, len(lines)):
			# sum the actual day + the 2 next
			try:
				threeDay = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
			except IndexError:
				break
			# if bigger than the 3 previous day, then increment answer
			if threeDay > lastThreeDay:
				answer += 1
			# update the three previous day
			lastThreeDay = threeDay
			
	# print the final answer (without the first measurement)
	print("answer: {}".format(answer - 1))
	
if __name__ == "__main__":
	main()
