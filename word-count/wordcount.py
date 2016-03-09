def word_count(foo):
	listA = foo.split()
	dictA = {}
	for wordA in listA:
		accum = 0
		for x in range(len(listA)):
			if wordA == listA[x]:
				accum += 1
		dictA[wordA] = accum
	return dictA