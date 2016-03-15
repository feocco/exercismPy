import re 

def encode(string):
	alph = 'abcdefghijklmnopqrstuvwxyz' # [::-1] Extended slice syntax for reversing string
	resultString = ''
	counter = 0

	for letter in string:
		if re.compile(r'[a-z]').match(letter.lower()):
			index = alph[::-1].index(letter.lower())
			resultString += alph[index]
			counter += 1
		elif re.compile(r'\d').match(letter):
			resultString += letter
			counter += 1
		if counter == 5:
			counter = 0
			resultString += ' '
	if resultString[-1] == ' ':
		return resultString[:-1]
	return resultString

def decode(string):
	alph = 'abcdefghijklmnopqrstuvwxyz'
	resultString = ''

	for letter in string:
		if re.compile(r'[a-z]').match(letter.lower()):
			index = alph[::-1].index(letter.lower())
			resultString += alph[index]
		elif re.compile(r'\d').match(letter):
			resultString += letter

	return resultString