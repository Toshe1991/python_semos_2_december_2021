# high level, general purpose, dynamic typed, interpreted programming language

# simple / immutable data types

# integer
# age = 10
#
# # float
# amount = 10.5
#
# # boolean True / False
# is_senior = True
#
# # string -> data structure
# name = "Toshe"
#
# # Data Structures

# # indexing, ordered
# print(names[0])
#
# # reverse ordered
# print(names[-1])
#
# #
# new_list = []
# for i in range(2,4):
#     new_list.append(names[i])

# Slicing [start:stop:step]
# new_names = names[2:4]
# print(new_names)

# List -> mutable
# names = ["Toshe", "Jovan", "Jovana", "Ivan"]
#
# reverse_names = names[::-1]  # reversed(names)
# print(reverse_names)


# range(start, stop, step) -> []
# range(1, 6, 2) -> [1, 3, 5]


# Time complexity
# every algorithm has time complexity

# Sets / Mnozestva  - Mutable
# Sets don't have duplicate values

# names = {"Toshe", "Goran", "Ivana", "Ivana"}
#
# # Unordered sequence of elements
# # print(names[0])
#
#
# names.add("Jovan")  # to add element
# names.remove("Ivana") # to remove element

# Dictionaries
# Collection of objects, unordered, key:value pairs
# Hash Table / Hash Map

# toshe = {"name": "Toshe", "age": 30, "gender": "male"}

# key in the dictionary is used as metadata
# print(toshe["age"])
# print(toshe.get("address", "Partizanska"))

# deleting an element from dictionary
# del toshe["name"]
# print(toshe)

# name = toshe.pop("address", None)
#
# print(name)
# print(toshe)

# Tuple
# Immutable, Ordered

# names = ("Toshe", "Ivana", "Jovan")

# advantages
# fixed number of elements, less memory usage / memory efficient


# CONTROL STRUCTURES
# Uslovi / Conditional statements
# if elif else / i od python3.9 -> switch - Structural Pattern matching

# Loops / Ciklusi
# names = ["Toshe", "Jovan", "Jovana", "Ivan"]

# For loop
# for name in names:
#     print(name)

# While Loop
# ENTRY POINT , EXIT/TERMINATION POINT
# Infinite Loop - Never ending cycle of execution
# count = 0
#
# while count < len(names):
#     print(names[count])
#     count += 1

# CONTROL FLOW
# SUBROUTINES / PROCEDURES -> Functions

# VALUE RETURNING FUNCTIONS
# def multiply(x, y):
#     return x * y
#
# total = multiply(10, 10)
# print(total)
#

# VOID FUNCTIONS
# def print_welcome(name):
#     print(f"Welcome {name}")
#
# total = print_welcome("Toshe")
# print(total)
# GLOBAL SCOPE AND LOCAL SCOPE

# LOCAL SCOPE
# def multiply(x, y):
#     total = x * y
#     print(total)
#
# multiply(10, 10)
#
# print(total)


# Parameters -> Positional and Keyword - Arguments

# def multiply(x, y=5):
#     return x * y
#
# # multiply(20, 10)  # positional arguments
#
# # multiply(y=20, x=10)  # keyword arguments
#
# # print(multiply(10, 20))
#
# print(multiply(10, y=20))  # positional and keyword argument