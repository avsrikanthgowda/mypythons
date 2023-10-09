# Count Word Frequency
# Define a function to count the frequency of words in a given list of words.
# Example:
#     words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
#     count_word_frequency(words) 
# Output:
#      {'apple': 3, 'orange': 2, 'banana': 1}
# TC: O(n), SC:O(n)
def count_word_frequency(myList):
    if len(myList) < 0:
        return {}
    elif len(myList) == 1:
        return {myList[0]:1}
    
    output = {}

    for word in myList:
        if word in output:
            output[word] += 1
        else:
            output[word] = 1
    
    return output

# print(count_word_frequency(['apple', 'orange', 'banana', 'apple', 'orange', 'apple']))
# print(count_word_frequency(['apple']))
# print(count_word_frequency(['apple', 'orange',]))
# print(count_word_frequency(['apple', 'orange', 'banana', 'apple', 'orange', 'apple', 'kiwi']))
# print(count_word_frequency([]))

# Common Keys
# Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.
# Example:
#     dict1 = {'a': 1, 'b': 2, 'c': 3}
#     dict2 = {'b': 3, 'c': 4, 'd': 5}
#     merge_dicts(dict1, dict2)
# Output:
#     {'a': 1, 'b': 5, 'c': 7, 'd': 5}

# TC=O(n), SC=O(1)
# def mergedicts(dict1, dict2):
#     for key in dict2:
#         if key in dict1:
#             dict1[key] = dict1[key] + dict2[key]
#         else:
#             dict1[key] = dict2[key]
    
#     return dict1

def mergedicts(dict1, dict2):
    result = dict1.copy()

    for key, value in dict2.items():
        result[key]= result.get(key,0)+ value

    return result

# print(mergedicts({'a': 1, 'b': 2, 'c': 3}, {'b': 3, 'c': 4, 'd': 5}))
# print(mergedicts({'a': 1, 'b': 2, 'c': 3}, {'e': 3, 'f': 4, 'g': 5}))
# print(mergedicts({'a': 10, 'b': 2, 'c': 3}, {'b': 3, 'c': 4, 'd': 5, 'e':1234}))
# print(mergedicts({'a': 1, 'b': 2, 'c': 3}, {'e': 3, 'f': 4, 'g': 5}))

# Key with the Highest Value
# Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.
# Example:
#     my_dict = {'a': 5, 'b': 9, 'c': 2}
#     max_value_key(my_dict))
# Output:
# b

#TC:O(n), SC:O(1)
# def max_value_key(my_dict):
#     highestValue = 0
#     highestKey=None

#     for key, value in my_dict.items():
#         if value > highestValue:
#             highestValue = value
#             highestKey = key

#     return highestKey

def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)

# print(max_value_key({'a': 5, 'b': 9, 'c': 2}))
# print(max_value_key({'a': 5, 'b': 9, 'c': 2, 'd':123}))
# print(max_value_key({'a': 5, 'b': 9, 'c': 2, 'b':23}))

# Reverse Key-Value Pairs
# Define a function which takes as a parameter dictionary and returns a dictionary in which reverse the key-value pairs are reversed.
# Example:
#     my_dict = {'a': 1, 'b': 2, 'c': 3}
#     reverse_dict(my_dict)
# Output:
#     {1: 'a', 2: 'b', 3: 'c'}

# TC:O(n), SC:O(n)
# def reverse_dict(my_dict):
#     reverseDict ={}
#     for key, value in my_dict.items():
#         reverseDict[value]= key
#     return reverseDict

def reverse_dict(my_dict):
    return {value:key for key, value in my_dict.items()}

# print(reverse_dict({'a': 1, 'b': 2, 'c': 3}))

# Conditional Filter
# Define a function that takes a dictionary as a parameter and returns a dictionary with elements based on a condition.
# Example:
#     my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
#     filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0) 
# Output:
#     {'b': 2, 'd': 4}


def filter_dict(my_dict):
    return {k:v for k, v in my_dict.items() if v % 2 == 0}

# print(filter_dict({'a': 1, 'b': 2, 'c': 3, 'd': 4} ))

# Same Frequency
# Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.
# Example:
#     list1 = [1, 2, 3, 2, 1]
#     list2 = [3, 1, 2, 1, 3]
#     check_same_frequency(list1, list2)
# Output:
# False

# def check_same_frequency(list1, list2):
#     freq1 = {}
#     freq2 = {}

#     for item in list1:
#         freq1[item] = freq1.get(item, 0) + 1
#         # if item in freq1:
#         #     freq1[item] +=1
#         # else:
#         #     freq1[item] = 1
    
#     for item in list2:
#         freq2[item] = freq2.get(item, 0) + 1
#         # if item in freq2:
#         #     freq2[item] +=1
#         # else:
#         #     freq2[item] = 1
    
#     return freq1 == freq2

def check_same_frequency(list1, list2):
    freq1 = {}
    freq2 = {}
    freq1 = {item: freq1.get(item, 0) + 1 for item in list1}
    freq2 = {item: freq2.get(item, 0) + 1 for item in list2}

    # for item in list1:
    #     freq1[item] = freq1.get(item, 0) + 1
    #     # if item in freq1:
    #     #     freq1[item] +=1
    #     # else:
    #     #     freq1[item] = 1
    
    # for item in list2:
    #     freq2[item] = freq2.get(item, 0) + 1
    #     # if item in freq2:
    #     #     freq2[item] +=1
    #     # else:
    #     #     freq2[item] = 1
    
    return freq1 == freq2

# print(check_same_frequency([1, 2, 3, 2, 1], [3, 1, 2, 1, 3]))
# print(check_same_frequency([1, 2, 3], [3, 1, 2]))
# print(check_same_frequency([2, 2, 2], [2, 1, 2]))
# print(check_same_frequency([2, 2, 2], [2, 2, 2]))
# print(check_same_frequency([2, 2, 2], [2, 2]))

# Sum and Product
# Write a function that calculates the sum and product of all elements in a tuple of numbers.
# Example
#     input_tuple = (1, 2, 3, 4)
#     sum_result, product_result = sum_product(input_tuple)
#     print(sum_result, product_result)  # Expected output: 10, 24


def sum_product(input_tuple):
    if len(input_tuple) < 1:
        return (0,0)

    sum_result=0
    product_result=1

    for num in input_tuple:
        sum_result+= num
        product_result *= num

    return (sum_result, product_result)

# input_tuple = (1, 2, 3, 4)
# sum_result, product_result = sum_product(input_tuple)
# print(sum_result, product_result)
# input_tuple = (1,)
# sum_result, product_result = sum_product(input_tuple)
# print(sum_result, product_result)
# input_tuple = (4, 3, 2, 1)
# sum_result, product_result = sum_product(input_tuple)
# print(sum_result, product_result)

# Elementwise Sum
# Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.
# Example
#     tuple1 = (1, 2, 3)
#     tuple2 = (4, 5, 6)
#     output_tuple = tuple_elementwise_sum(tuple1, tuple2)
#     print(output_tuple)  # Expected output: (5, 7, 9)

# def tuple_elementwise_sum(tuple1, tuple2):
#     output_list = []
#     for index,value in enumerate(tuple2):
#         output_list.append(tuple1[index] + value)
#     return tuple(output_list)

# def tuple_elementwise_sum(tuple1, tuple2):
#     return tuple(map(sum, zip(tuple1, tuple2)))

def tuple_elementwise_sum(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError("Input tuples must have same length")

    result = tuple( a+b for a, b in zip(tuple1, tuple2))
    return result

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# output_tuple = tuple_elementwise_sum(tuple1, tuple2)
# print(output_tuple)

# tuple1 = (4, 2, 3)
# tuple2 = (4, 5, 6)
# output_tuple = tuple_elementwise_sum(tuple1, tuple2)
# print(output_tuple)

# Insert at the Beginning
# Write a function that takes a tuple and a value, and returns a new tuple with the value inserted at the beginning of the original tuple.
# Example
#     input_tuple = (2, 3, 4)
#     value_to_insert = 1
#     output_tuple = insert_value_front(input_tuple, value_to_insert)
#     print(output_tuple)  # Expected output: (1, 2, 3, 4)

def insert_value_front(input_tuple, value_to_insert):
    return (value_to_insert,) + input_tuple

# input_tuple = (2, 3, 4)
# value_to_insert = 1
# output_tuple = insert_value_front(input_tuple, value_to_insert)
# print(output_tuple)

# Concatenate
# Write a function that takes a tuple of strings and concatenates them, separating each string with a space.
# Example
#     input_tuple = ('Hello', 'World', 'from', 'Python')
#     output_string = concatenate_strings(input_tuple)
#     print(output_string)  # Expected output: 'Hello World from Python'

def concatenate_strings(input_tuple):
    return ' '.join(input_tuple)

# input_tuple = ('Hello', 'World', 'from', 'Python')
# output_string = concatenate_strings(input_tuple)
# print(output_string)  # Expected output: 'Hello World from Python'

# Diagonal
# Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.
# Example
#     input_tuple = (
#         (1, 2, 3),
#         (4, 5, 6),
#         (7, 8, 9)
#     )
#     output_tuple = get_diagonal(input_tuple)
#     print(output_tuple)  # Expected output: (1, 5, 9)

# def get_diagonal(input_tuple):
#     output_list = []
#     for index, value in enumerate(input_tuple):
#         output_list.append(value[index])
#     return tuple(output_list)

def get_diagonal(input_tuple):
    return tuple (value[index] for index, value in enumerate(input_tuple))

# input_tuple = (
#         (1, 2, 3),
#         (4, 5, 6),
#         (7, 8, 9)
#     )
# output_tuple = get_diagonal(input_tuple)
# print(output_tuple)  # Expected output: (1, 5, 9)

# input_tuple = (
#         (222, 2, 3),
#         (4, 333, 6),
#         (7, 8, 444)
#     )
# output_tuple = get_diagonal(input_tuple)
# print(output_tuple)  # Expected output: (1, 5, 9)

# Common Elements
# Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.
# Example
#     tuple1 = (1, 2, 3, 4, 5)
#     tuple2 = (4, 5, 6, 7, 8)
#     output_tuple = common_elements(tuple1, tuple2)
#     print(output_tuple)  # Expected output: (4, 5)

# def common_elements(tuple1, tuple2):
#     output_list=[]
#     for tup in tuple1:
#         if tup in tuple2:
#             output_list.append(tup)
#     return tuple(output_list)

# TC:O(n), SC:O(n)
# def common_elements(tuple1, tuple2):
#     return tuple(tup for tup in tuple1 if tup in tuple2)

def common_elements(tuple1, tuple2):
    return tuple(set(tuple1)& set(tuple2))

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)  # Expected output: (4, 5)