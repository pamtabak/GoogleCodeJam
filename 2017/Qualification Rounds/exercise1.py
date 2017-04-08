count = 0
number_of_cases = 0
file_object = open("ex1.txt", "r")
for line in file_object:
	if (count == 0):
		count += 1
		number_of_cases = int(line)
		continue
	list_pancake = line.replace("\n", "").replace(" ","")
	k = int(list_pancake[-1])
	if ("-" not in list_pancake):
		print("Case #{}: {}".format(count, 0))
		count += 1
		continue
	if ("+" not in list_pancake):
		if (len(list_pancake) % k == 0):
			print("Case #{}: {}".format(count, len(list_pancake)))
			count += 1
			continue
		else:
			print("Case #{}: {}".format(count, "IMPOSSIBLE"))
			count += 1
			continue
	if (k % 2 == 0):
		if (("-+-" in list_pancake or "+-+" in list_pancake) and len(list_pancake) % 2 != 1):
			print("Case #{}: {}".format(count, "IMPOSSIBLE"))
			count += 1
			continue


	#else:
		# impar

	count += 1