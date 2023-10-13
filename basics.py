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

# input_string = """Name,Phone,Address
# Mike Smith,15554218841,123 Nice St, Roy, NM, USA
# Anita Hernandez,15557789941,425 Sunny St, New York, NY, USA
# Guido van Rossum,315558730,Science Park 123, 1098 XG Amsterdam, NL"""

# res=[]
# for ls in input_string.split('\n')[1:]:
#     res.append(ls.split(',',maxsplit=2))

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
set1=set([1,2,3,4])
print(set1)
print(type(set1))
set2=set(['a','b','c'])
print(set2)
print(type(set2))





