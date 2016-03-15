import re 

def encode(string):
	alph = 'abcdefghijklmnopqrstuvwxyz'
	resultString = ''
	counter = 0

	for letter in string:
		#print('letter: ', letter)
		if re.compile(r'[a-z]').match(letter.lower()): # If alphanumeric
			#print('alpha match')
			index = alph.index(letter.lower())
			resultString += alph[-(index + 1)]
			counter += 1
		elif re.compile(r'\d').match(letter): # If digit
			resultString += letter
			counter += 1
		if counter == 5:
			counter = 0
			resultString += ' '

	return resultString

def decode(string):
	alph = 'abcdefghijklmnopqrstuvwxyz'