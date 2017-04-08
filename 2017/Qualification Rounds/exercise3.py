import operator

count = 0
file_object = open("ex3.txt", "r")
for line in file_object:
	flips = 0
	if (count == 0):
		count += 1
		continue
	line = line.replace("\n", "")
	n = int(line.split(' ')[0])
	k = int(line.split(' ')[1])

	stalls        = (n + 2) * [0] # size = n+2
	stalls[0]     = 1 # filled
	stalls[n + 1] = 1 # filled
	
	print(distance)
	#print("Case #{}: {}".format(count, "IMPOSSIBLE"))
	count += 1
