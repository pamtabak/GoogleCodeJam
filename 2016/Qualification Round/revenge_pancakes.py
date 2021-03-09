# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer

for execution in range(1, t + 1):
	result = 0 # the minimum amount of times needed to flip all pancakes
	pancakes_input = input() # read a sequence of pancake's state
	listPancake = list(pancakes_input)
	for index in reversed(range(0, len(listPancake))):
		if listPancake[index] == "+":
			continue
		if listPancake[index] == "-":
			result+=1
			#invert the rest of the sequence
			for invert in range(0, index+1):
				if (listPancake[invert] == "+"):
					listPancake[invert] = "-"
				else:
					listPancake[invert] = "+"
	print("Case #{}: {}".format(execution, result))	