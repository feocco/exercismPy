def slices(string, length):
	counter = 0
	resultList = []

	if length > len(string) or length <= 0:
		raise ValueError("The length is too large or less than or equal to Zero")

	while length <= len(string):
		results = [int(i) for i in list(string)[counter:length]]
		resultList.append(results)
		counter += 1
		length += 1

	return resultList