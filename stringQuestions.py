def reverseWords(S):
    # code here 
    split_str = S.split('.')
    split_str.reverse()
    # print(split_str)
    # print(type(rev_str))
    final_str = ""
    for key, value in enumerate(split_str):
        final_str += value + '.'
    print(final_str)
    return final_str

# reverseWords("i.like.this.program.very.much")


# Roman Number to Integer
# EasyAccuracy: 43.31%Submissions: 156K+Points: 2

# Hack you way to glory and win from a cash pool prize of INR 15,000. Register for free now
# banner

# Given a string in roman no format (s)  your task is to convert it to an integer . Various symbols and their values are given below.
# I 1
# V 5
# X 10
# L 50
# C 100
# D 500
# M 1000

# Example 1:

# Input:
# s = V
# Output: 5

# Example 2:

# Input:
# s = III 
# Output: 3

# Your Task:
# Complete the function romanToDecimal() which takes a string as input parameter and returns the equivalent decimal number. 

# Expected Time Complexity: O(|S|), |S| = length of string S.
# Expected Auxiliary Space: O(1)

# Constraints:
# 1<=roman no range<=3999

def romanToDecimal(S): 
    # code here
    map_dict = {'I':1, "IV": 4, "V": 5, "IX":9,"X":10, "XL":40, "L":50, "XC":90,"C":100,"CD":400, "D":500, "CM":900, "M":1000}
    return_val=0
    i = 0
    
    while (len(S)-i)>0:
        if S[i:i+1] in map_dict:
            return_val += map_dict[S[i:i+1]]
            print(f"if {S[i:i+1]}: {return_val}")
            i +=2
        else:
            return_val += map_dict[S[i]]
            print(f"else {S[i]}:{return_val}")
            i += 1
            
    print(return_val)
    return return_val

romanToDecimal("XIX")
romanToDecimal("V")