t = int(input())  # read a line with a single integer


def number_is_odd(number):
	if (number % 2 != 0):
		return True
	return False

for i in xrange(1, t + 1):
	n = int(input())  # numbers per row or column
	heights = []
	allHeights = ""
	rowColumn = 2 * n - 1
	missing = []
	for j in xrange(0,rowColumn):
		s = raw_input()
		heights.append(s.split())
		# print(heights[j])
		row = []
		#print(heights[j])
		#print([words for segments in list(heights[j]) for words in segments.split()])
		allHeights += s + " "
		# str(allHeights).split()
	allHeights = allHeights.split()
	for j in xrange(0, rowColumn):
		for k in xrange(0,n):
			if (number_is_odd(allHeights.count(heights[j][k]))):
					missing.append(heights[j][k])
	
	missing = map(int, list(set(missing)))
	missing = sorted(missing)
	missing = str(missing).replace("[","").replace("]","").replace(",","")
	print("Case #{}: {}".format(i, missing))				

	

	# m = sorted(list(set(m)))
	# sorted(missing, key=lambda student: int(missing[0]))
	# print(m)
	# result = str(missing).replace("'","").replace("[","").replace("]","").replace(",","")
	# # result = ""
	# # for j in xrange(0,n):
	# # 	result += missing[j] + " "
	# # result = result[:-1]
	#sorted(heights, key=lambda student: student[0])
