def main():
	# Vars
	horizontal = 0
	depth = 0
	aim = 0

	# open the file
	with open('input.txt') as file:
		# iterate through each line
		for line in file.readlines():
			# split direction and amount
			direction, amount = line.split()[0], int(line.split(" ")[1])
			# edit position based on direction and amount
			if (direction == "forward"): 
				horizontal += amount
				depth += amount * aim 
			if (direction == "down"): aim += amount 
			if (direction == "up"): aim += amount * -1
	# print the final answer
	print("answer: {}".format(horizontal * depth))
	
if __name__ == "__main__":
	main()
