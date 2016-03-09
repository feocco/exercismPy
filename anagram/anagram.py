def detect_anagrams(word, arg):
	returnList = []
	for phrase in arg:
		if word.lower() == phrase.lower():
			pass
		elif len(word) == len(phrase):
			if sorted(word.lower()) == sorted(phrase.lower()):
				returnList.append(phrase)
	return returnList