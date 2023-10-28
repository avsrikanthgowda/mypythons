# import requests
# resp = requests.get("http://olympus.realpython.org")
# html = resp.text
# print(html[86:132])

# str1="fig pie"
# print(str1[::-100])

# str2="bazinga"
# print(str2[2:6])

# str1 = "SRIKANTH"
# print(str1.lower())

# str2 = "srikanth"
# print(str2.upper())

# name = "    Jean-Luc Picard     "
# print(name.rstrip())
# print(name.lstrip())
# print(name.strip())

# starship = "Enterprise"
# print(starship.startswith("En"))
# print(starship.endswith("se"))

# var = input()
# print(var)
# print(type(var))
# print(int(var))
# print(float(var))
# print(str(var))
# var2=input("enter number: \n")
# print(var2)

# phrase = "the surprise is in here somewhere"
# print(phrase.find("surprise"))

# print('a,b,c'.split(','))
# str1="i am good as you are"
# print(str1.split())
# print(str1.split("g"))
# print(str1.split(" "))

input_string = """Name,Phone,Address
Mike Smith,15554218841,123 Nice St, Roy, NM, USA
Anita Hernandez,15557789941,425 Sunny St, New York, NY, USA
Guido van Rossum,315558730,Science Park 123, 1098 XG Amsterdam, NL"""

res=[]
for ls in input_string.split('\n')[1:]:
    res.append(ls.split(',',maxsplit=2))

# print(res)

# strings = ['do','re','mi']
# print(','.join(strings))


inputVar = [
    ['Boston', 'MA', '76F', '65% Precip', '0.15 in'],
    ['San Francisco', 'CA', '62F', '20% Precip', '0.00 in'],
    ['Washington', 'DC', '82F', '80% Precip', '0.19 in'],
    ['Miami', 'FL', '79F', '50% Precip', '0.70 in']
]

outputStr=""
for ls in inputVar:
    outputStr = outputStr + ",".join(ls) + '\n'
# print(outputStr)

joined = [','.join(ls) for ls in inputVar]
# print(joined)

# print("\n".join(joined))

ls=[1, 2, 3, 4, 5]

# print(sum(ls))

names = ['Harry', 'Suzy', 'Al', 'Mark']

# print(sorted(names, reverse=True))

words = ['banana', 'pie', 'Washington', 'book']

# print(sorted(words,key=lambda x: x[::-1]))

# print((lambda x,y,z: x+y+z)(1,2,3))

ls=[1,2,3,4]
ls2=['a','b','c']
ls3=['apple',"banana"]
ls4=[11,22,33,44]

# print(list(zip(ls,ls2)))
# print(dict(zip(ls,ls2)))
# print(tuple(zip(ls,ls2)))
# print(set(zip(ls,ls2)))
# print(list(zip(ls,ls3)))

a=['a','b']
a.extend([1,2,3])
# print(a)

a.insert(1,'aa')
# print(a)

a.remove('b')

# print(a)

tup=tuple((1,2,3,4))
# print(tup)

tup2=('a',"bv")
# print(tup2)

tup3=(1,2,"a","b")
# print(tup3)

# tup3.append(12) //since immutable no append,extend,pop,remove methods
# print(tup3)

# set
# set1=set([1,2,3,4])
# print(set1)
# print(type(set1))
# set2=set(['a','b','c'])
# print(set2)
# print(type(set2))



# set2.insert(4)
# print(set2)

lst = [1,2,3]
lst2 = list([4,5,6])
# print(lst, lst2)

tup = (1,2,3)
tup2 = tuple((4,5,6))
# print(tup, tup2)

set1 = {1,2,4}
set2 = set({1,2,4})

# print(set1,set2)

dict1 = {'a':1, 'b':2,'c':3}
dict2 = dict({'a':1, 'b':2,'c':3})
# print(dict1,dict2)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# print(car.get("size", '8 GB'))

lst = [1,2,3]
# print(lst[0:1])

# lst2 = [1 ,2, 3 ,-2, 5]
# print(len(lst2))
# for i in range(len(lst2)):
#     for j in range(i, len(lst2)):
#         print(lst2[i:j+1])



#Back-end complete function Template for Python 3
#optimized solution
class Solution:
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,a,size): 
           
        max_so_far = -9999999 - 1
        max_ending_here = 0
        
        #Iterating over the array. 
        for i in range(0, size): 
            #Updating max sum till current index.
            max_ending_here = max_ending_here + a[i]
            
            #Storing max sum so far by choosing maximum between max 
            #sum so far and max sum till current index.
            if (max_so_far < max_ending_here): 
                max_so_far = max_ending_here 
        
            #If max sum till current index is negative, we do not need to add
            #it to result so we update it to zero.
            if max_ending_here < 0: 
                max_ending_here = 0   
        
        #returning the result.
        return max_so_far

# brute force
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        if N == 1:
            return arr[0]

        maximum = arr[0]
        for i in range(N):
            for j in range(i+1, N):
                if sum(arr[i:j+1]) > maximum:
                    maximum = sum(arr[i:j+1])

        arr.extend([maximum])
        arr.sort()
        return max(arr)

intmax= -999999 -1
print(intmax)
intmax2 = -1000000
print(intmax2)