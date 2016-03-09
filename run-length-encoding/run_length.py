import re 

def encode(string):
	newString = ''
	pattern = re.compile(r'(.)(\1*)')

	for first, letters in re.findall(pattern, string):
		if letters:
			newString += str(len(letters) + 1) + first
		else:
			newString += first

	return newString

def decode(string):
	newString = ''
	pattern = re.compile(r'(\d*)(.)')
	
	for quantity, letter in re.findall(pattern, string):
		if quantity:
			newString += int(quantity) * letter
		else:
			newString += letter

	return newString