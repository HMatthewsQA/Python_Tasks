bestroute = []
newroute = []
lowest = 0
number = 0
pointer = 0

peaks = (1,0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15)
final = len(peaks) - 1

for x in peaks:
    if x <= lowest:
        lowest = x

index = peaks.index(lowest)

while index < final:
    number = lowest
    goodpath = False
    newroute.append(lowest)
    
    #code to iterate through peaks list
        
    
    print(newroute)
    for i in newroute:
        if i > number:
            number = i
            goodpath = True
        else:
            goodpath = False
            break
    
    if len(newroute) > len(bestroute) & goodpath == True:
        bestroute.clear()
        bestroute = newroute
    newroute = []
    index += 1
    
print('The best route is ', bestroute)


