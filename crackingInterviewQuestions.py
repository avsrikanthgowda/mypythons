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