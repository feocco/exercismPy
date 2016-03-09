def is_pangram(word):
	word = word.lower()
	letters = 'abcdefghijklmnopqrstuvwxyz'

	for x in letters:
		if x in word:
			pass
		else:
			return False

	return True