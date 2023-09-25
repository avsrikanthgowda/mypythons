# Q1: Write a function to find the missing number in a given integer array of 1 to 100.
def findMissing(myList, totalCount):
    sum1 = totalCount * (totalCount+1)/2 # --> n * (n+1)/2 is the formula
    sum2 = sum(myList)
    return sum1 - sum2
# print(f"missing number: {findMissing([1,2,3,4,6],6)}")

# Q2: Two Sum
# Given an array of integers nums and an integer target , return indices of the two numbers such that they add upto target

# brute-force way
def twoSum(numsList, target):
    res=[]
    for index in range(len(numsList)):
        for innerIndex in range(index+1, len(numsList)):
            if numsList[index] + numsList[innerIndex] == target:
                res = [index, innerIndex]
                break
        if len(res) > 0:
            break
    return res

# print(f"twoSum(BF) : {twoSum([2,7,11,15],9)}")
# print(f"twoSum(BF) : {twoSum([3,2,4],6)}")
# print(f"twoSum(BF) : {twoSum([3,3],6)}")

# two sum leet-code
def twoSumLeetCode(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

# print(f"twoSum(LC) : {twoSum([2,7,11,15],9)}")
# print(f"twoSum(LC) : {twoSum([3,2,4],6)}")
# print(f"twoSum(LC) : {twoSum([3,3],6)}")

# find an number in an array
import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

def findNumber(arr, target):
    found=False
    for num in arr:
        if num == target:
            found = True
            break
    return found

# print(f"number: {findNumber(array, 1)}")
# print(f"number: {findNumber(array, 13)}")
# print(f"number: {findNumber(array, 16)}")
# print(f"number: {findNumber(array, 10000)}")
# print(f"number: {findNumber(array, 23)}")

# Max Product of Two Integers
# Find the maximum product of two integers in an array where all elements are positive.
# Example
#     arr = [1, 7, 3, 4, 9, 5] 
#     max_product(arr) # Output: 63 (9*7)

def maxProduct(arr):
    if len(arr) == 2:
        return arr[0] * arr[1]
    elif len(arr) == 1:
        return arr[0]
    
    maxProduct = arr[0] * arr[1]

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]*arr[j] > maxProduct:
                maxProduct = arr[i]*arr[j]

    return maxProduct

# print(f"max product(BF): {maxProduct([1, 7, 3, 4, 9, 5])}")
# print(f"max product(BF): {maxProduct([1, 7, 3, 4, 9, 5,12])}")
# print(f"max product(BF): {maxProduct([1, 7])}")
# print(f"max product(BF): {maxProduct([1])}")
# print(f"max product(BF): {maxProduct([1, 7, 3])}")

def maxProductLC(arr):
    if len(arr) == 2:
        return arr[0] * arr[1]
    elif len(arr) == 1:
        return arr[0]
    
    max1, max2 = 0
    
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

    return max1 * max2

# print(f"max product(LC): {maxProduct([1, 7, 3, 4, 9, 5])}")
# print(f"max product(LC): {maxProduct([1, 7, 3, 4, 9, 5,12])}")
# print(f"max product(LC): {maxProduct([1, 7])}")
# print(f"max product(LC): {maxProduct([1])}")
# print(f"max product(LC): {maxProduct([1, 7, 3])}")
        
# Middle Function
# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
#     myList = [1, 2, 3, 4]
#     middle(myList)  # [2,3]

def middle(myList):
    if len(myList) < 3:
        return []
    
    newList = []
    for index in range(1, len(myList)-1):
        newList.append(myList[index])

    return newList

# print(f"middle(BF): {middle([1, 2, 3, 4])}")
# print(f"middle(BF): {middle([1, 2, 5, 3, 44, 56, 3, 4])}")
# print(f"middle(BF): {middle([1,  4])}")
# print(f"middle(BF): {middle([1,  4, 3])}")

def middleLC(myList):
    if len(myList) < 3:
        return []

    return myList[1:-1]

# print(f"middle(BF): {middle([1, 2, 3, 4])}")
# print(f"middle(BF): {middle([1, 2, 5, 3, 44, 56, 3, 4])}")
# print(f"middle(BF): {middle([1,  4])}")
# print(f"middle(BF): {middle([1,  4, 3])}")

