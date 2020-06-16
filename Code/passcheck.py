def passcheck(thelist):
	passlist = []
	for passw in thelist[0:]:
		lower = False
		upper = False
		number = False
		lowerpass = False
		upperpass = False
		numberpass = False
		charpass = False
		if len(passw) >= 6 and len(passw) <= 12:
			for letter in passw:
				lower = letter.islower()
				upper = letter.isupper()
				number = letter.isnumeric()
				if lower == True:
					lowerpass = True
					lower = False
					continue
				elif number == True:
					numberpass = True
					number = False
					continue
				elif upper == True:
					upperpass = True
					upper = False
					continue
				elif letter == '$' or letter == '#' or letter == '@':
					charpass = True
				if lowerpass == True and upperpass == True and numberpass == True and charpass == True:
					passlist.append(passw)
					break
	return passlist