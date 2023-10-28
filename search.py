import math
custArray = [8, 9, 12, 15, 17, 19, 20, 21, 28]

def binarySearch(array, target):
    start=0
    end=len(array)-1
    middle = math.floor((start+end)/2)
    while array[middle] != target and start <=end:
        if array[middle] > target:
            end = middle-1
        else:
            start = middle+1
        middle = math.floor((start+end)/2)

    if array[middle] == target:
        return middle
    else:
        return -1

print(binarySearch(custArray, 15))