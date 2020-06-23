def scrambler(listnum,listlet):
	counter = 0
	output = ''
	while counter < len(listnum):
		output = output + listnum[counter]
		output = output + listlet[counter]
		counter += 1
	return output