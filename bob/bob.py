def hey(input): #MAIN
    foo = input.strip() #Strips input

    #Check input against requirements and initialize as T / F
    is_question, is_yelling, is_address = \
    checkQuestion(foo), checkYelling(foo), checkAddress(foo)

    #Get Responses
    if is_question and not is_yelling: return 'Sure.'
    elif is_yelling: return 'Whoa, chill out!'
    elif is_address: return 'Fine. Be that way!'
    else: return 'Whatever.'    

def checkQuestion(foo):
    if len(foo) > 0 and foo[-1] == '?': return True

def checkYelling(foo):
    a = ''
    letters = 'abcdefghijklmnopqrstuvwxyzäÜ'
    for x in foo:
        if x in letters:
            a += x
        elif x in letters.upper():
            a += x
    if a == a.upper() and a != '':
        return True
    elif a != a.upper(): return False

def checkAddress(foo):
	if not foo: return True