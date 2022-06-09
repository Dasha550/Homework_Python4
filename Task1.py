from random import randint

with open('Task1.txt','w') as numRand:
    for i in range (5): numRand.write(str(randint(1,10))+' ')

with open('Task1.txt','r') as numSort:
    numSorted=numSort.readline().split(' ')
    numSorted.pop()
    print (sorted(map(int, numSorted))) 