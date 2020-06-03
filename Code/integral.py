#integral = int(input("Please input a number: "))
mydict = {}

def createdict(number):
    x = 1
    while x <= number:
        mydict[x] = x*x
        x += 1
    return mydict

#createdict(integral)