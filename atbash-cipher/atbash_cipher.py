import re 

def encode(string):
	alph = 'abcdefghijklmnopqrstuvwxyz' # [::-1] Extended slice syntax for reversing string
	resultString = ''

	for letter in string:
		if re.compile(r'[a-z]').match(letter.lower()):
			index = alph[::-1].index(letter.lower())
			resultString += alph[index]
		elif re.compile(r'\d').match(letter):
			resultString += letter

	return ' '.join([resultString[i:i+5] for i in range(0, len(resultString), 5)]) 

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