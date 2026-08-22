# Assignment No. 1


# Operations on List, Tuple and Dictionary


# OPERATIONS ON LISTS



print("----- LIST OPERATIONS -----")

numbers = [30, 10, 50, 20, 40]   # a list of numbers
print("Original List:", numbers)

# method 1 : APPEND 
numbers.append(60) 
print("After append:", numbers)

# method 2 : INSERT 
numbers.insert(1, 15)
print("After insert:", numbers)

# method 3 : REMOVE 
numbers.remove(50)
print("After remove:", numbers)

# method 4 : POP 
removed_element = numbers.pop()
print("After pop:", numbers , "Popped element:", removed_element,) 

# method 5 : SORT 
numbers.sort()
print("After sorting:", numbers)

print("------END OF LIST OPERATIONS ------\n")


## OPERATIONS ON TUPLES


print("----- TUPLE OPERATIONS -----")

numbers = (30, 10, 50, 20, 40)   # a tuple of numbers
print("Original Tuple:", numbers)

# method 1 : COUNT
count = numbers.count(10)
print("Count of 10:", count)

# method 2 : INDEX
index = numbers.index(20)
print("Index of 20:", index)

# method 3 : LENGTH
length = len(numbers)
print("Length of tuple:", length)

# method 4 : SLICING
print("Tuple after slicing:", numbers[1:4])  #includes index 1,2,3 but not 4

# method 5 : REPETITION
repeated_tuple = numbers * 2
print("Repeated tuple:", repeated_tuple)



print("------END OF TUPLE OPERATIONS ------\n")


## OPERATIONS ON DICTIONARY


print("----- DICTIONARY OPERATIONS -----")

numbers = {
    "name": "kriyan",
    "age": 17,
    "profession": "student"
}
print("Original Dictionary:", numbers)


# method 1 : ACCESSING VALUES
print("Name:", numbers["name"])

# method 2 : DISPLAY KEYS
print("Keys:", numbers.keys())

# method 3 : DISPLAY VALUES
print("Values:", numbers.values())

# method 4 : ADDING NEW KEY-VALUE PAIR
numbers["city"] = "Pune"
print("After adding new key-value pair:", numbers)

# method 5 : UPDATING VALUE
numbers["age"] = 18
print("After updating age:", numbers)


print("------END OF DICTIONARY OPERATIONS ------\n")






