def main():
	# Vars
	gamma = ""
	epsilon = ""
	bits = ["", "", "", "", "", "", "", "", "", "", "", ""]

	# open the file
	with open('input.txt') as file:
		# iterate through each line
		for line in file.readlines():
			line = line.rstrip('\n')
			# split bits in different variables
			for i in range(0, len(line)):
				bits[i] += line[i]
	# calc gamma and epsilon rate for each
	for i in range(0, len(bits)):
		gamma += '1' if bits[i].count('1') > bits[i].count('0') else '0'
		epsilon += '0' if bits[i].count('1') > bits[i].count('0') else '1'
	print(gamma)
	print(epsilon)
	# convert binary values to decimal
	cGamma, cEpsilon = 0, 0
	for i, j in zip(range(0, len(gamma)), range(11, -1, -1)):
		cGamma += int(gamma[i]) * (2**j)
		cEpsilon += int(epsilon[i]) * (2**j)
	print(cGamma)
	print(cEpsilon)
	# print the final answer
	print("answer: {}".format(cGamma * cEpsilon))
	
if __name__ == "__main__":
	main()
