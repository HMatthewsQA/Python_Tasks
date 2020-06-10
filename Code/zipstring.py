def zipstring(stringone,stringtwo):
    mylist = []
    counter = 0
    newstring = ""
    for i in range(len(stringone)):
        mylist.insert(counter,stringone[i])
        counter += 1
        mylist.insert(counter,stringtwo[i])
        counter += 1
    for x in mylist:
        newstring = newstring + x
    return newstring