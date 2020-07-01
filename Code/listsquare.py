def listsquare(list):
	squaredlist = []
	for i in list:
		if i%2 != 0:
			x = i*i
			squaredlist.append(x)
	return squaredlist