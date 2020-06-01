bestroute = []
newroute = []
lowest = 0
number = 0

peaks = (1,0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15)

for x in peaks:
    if x <= lowest:
        lowest = x

index = peaks.index(lowest)
newroute.append(lowest)
number = lowest

for i in peaks[index:]:
    if i > number:
        newroute.append(i)
        number = i

print(newroute)

if len(newroute) > len(bestroute):
    bestroute = newroute

print(bestroute)


