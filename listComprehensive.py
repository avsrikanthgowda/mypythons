prevList = [1,2,3,4]
myList = [i*2 for i in prevList]
print(myList)

prev2List = [-10, 23,-90, 11, 23, -9]

myNewList = [i for i in prev2List if i >= 0]

print(myNewList)

newPrevList = [1,-33,45,-6,78]
newList = [number if number > 0 else 0 for number in newPrevList]
print(newList)

takeInput = int(input("give us some int number"))
print(takeInput)