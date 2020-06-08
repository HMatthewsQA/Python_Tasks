def sum_of_nos(stringint):
    mylist = []
    mysum = 0
    mylist.append(stringint)
    mylist.append(stringint*2)
    mylist.append(stringint*3)
    mylist.append(stringint*4)
    mysum = int(mylist[0]) + int(mylist[1]) + int(mylist[2]) + int(mylist[3])
    return mysum