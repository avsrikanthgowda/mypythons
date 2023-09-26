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


# Given 2D list calculate the sum of diagonal elements.
# Example
#     myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
#     diagonal_sum(myList2D) # 15

# BF way SC= O(1), TC=O(n)
def diagonal_sum(myList2D):
    sum = 0
    index = 0
    for subList in myList2D:
        sum += subList[index]
        index += 1
    return sum

# print(f"diagonal_sum : {diagonal_sum([[1,2,3],[4,5,6],[7,8,9]] )}")
# print(f"diagonal_sum : {diagonal_sum([[2,2,3],[4,5,6],[7,8,11]] )}")
# print(f"diagonal_sum : {diagonal_sum([[1,2],[4,5]] )}")
# print(f"diagonal_sum : {diagonal_sum([[1,2,3,4],[4,5,6, 5],[7,8,9,12],[12,23,24,23]] )}")

# Given a list, write a function to get first, second best scores from the list.
# List may contain duplicates.
# Example
#     myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
#     first_second(myList) # 90 87

#BF TC: O(n), SC:O(1)
def first_second(myList):
    if len(myList) < 1:
        return [0,0]

    first = myList[0]
    second = myList[0]

    for num in myList:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return [first, second]

# print(f"first_second : {first_second([84,85,86,87,85,90,85,83,23,45,84,1,2,0])}")
# print(f"first_second : {first_second([])}")
# print(f"first_second : {first_second([100,100,100,200,100,100,100])}")
# print(f"first_second : {first_second([10000])}")

# Write a function to remove the duplicate numbers on given integer array/list.
# Example
#     remove_duplicates([1, 1, 2, 2, 3, 4, 5])
#     Output : [1, 2, 3, 4, 5]

# BF way TC=O(n), SC=O(n)
def remove_duplicates(myList):
    if len(myList) <= 1:
        return myList

    seen = {}
    newList = []
    for num in myList:
        if num not in seen:
            newList.append(num)
            seen[num] = num
    return newList

# print(f"remove_duplicates : {remove_duplicates([1, 1, 2, 2, 3, 4, 5])}")
# print(f"remove_duplicates : {remove_duplicates([1])}")
# print(f"remove_duplicates : {remove_duplicates([])}")
# print(f"remove_duplicates : {remove_duplicates([1, 1])}")
# print(f"remove_duplicates : {remove_duplicates([1, 1, 2, 2, 3, 4, 5,12,-11,23,-11,23,22,25])}")

# Pairs
# Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.
# Example
#     pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
#     Output : ['2+5', '4+3', '3+4', '-2+9']
# Note:
# 4+3 comes from second and third elements from the main list.
# 3+4 comes from third and seventh elements from the main list.

#BF way TC: O(n2), SC: O(n)
def pair_sum(myList, target):
    if len(myList) < 1:
        return myList

    outputList = []
    for i in range(len(myList)):
        for j in range(i,len(myList)):
            if myList[i] + myList[j] == target:
                outputList.append(str(myList[i])+'+'+str(myList[j]))
    
    return outputList

# print(f"pair_sum : {pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)}")

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example :
#     Input: nums = [1,2,3,1]
#     Output: true
# Hint: Use sets

# TC: O(n), SC:O(n)
def checkDuplicates(myList):
    if len(myList) < 1:
        return False

    mySet = set()
    for nums in myList:
        if nums in mySet:
            return True
        mySet.add(nums)

    return False

# print(f"checkDuplicates : {checkDuplicates([1,2,3,1])}")
# print(f"checkDuplicates : {checkDuplicates([1,2,3])}")
# print(f"checkDuplicates : {checkDuplicates([1,2,3,3])}")
# print(f"checkDuplicates : {checkDuplicates([1,2,3,3,1])}")
# print(f"checkDuplicates : {checkDuplicates([])}")
# print(f"checkDuplicates : {checkDuplicates([34,34])}")
# print(f"checkDuplicates : {checkDuplicates([98])}")

# permuatation of two list or not

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    
    list1.sort()
    list2.sort()

    if list1 == list2:
        return True
    else:
        return False
    
# print(f"permutation : {permutation([1,2,3],[1,3,2])}")
# print(f"permutation : {permutation([],[1,3,2])}")
# print(f"permutation : {permutation([1,2,3,4],[1,3,2,5])}")
# print(f"permutation : {permutation(['a','b','c'],['c','a','b'])}")

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.
# Example:
# for greater understanding see image shown in udemy
#     Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#     Output: [[7,4,1],[8,5,2],[9,6,3]]

#BF way
def rotateMatrixInplace(matrix):
    if len(matrix) <= 1:
        return matrix
    
    n = len(matrix)
    
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

    return matrix

# print(f"rotateMatrixInplace: {rotateMatrixInplace([[1,2,3],[4,5,6],[7,8,9]])}")
# print(f"rotateMatrixInplace: {rotateMatrixInplace([[1,2,33],[4,5,66],[7,8,99]])}")
# print(f"rotateMatrixInplace: {rotateMatrixInplace([[1,2,33]])}")