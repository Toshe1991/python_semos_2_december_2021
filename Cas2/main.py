# # a = 10  # a -> 0001 (10)
# # b = a  # b -> 0003 (30)
# #
# # b = 30
# #
# # print(a)
# # print(b)
#
# # a -> 0001(60)
# a = 40
# print(id(a))
#
# a = 60
# print(id(a))

## IMMUTABLE AND MUTABLE OBJECTS
# int, bool, str, float, tuple  - IMMUTABLE
# list, dict, set  - MUTABLE

# num = 10  # 0001 -> 10
# print(id(num))
# num += 5  # -> 0002 -> 15
# print(id(num))
# # num = 10
# print(id(num))

# GARBAGE COLLECTION
# REFERENCE COUNTING -> counts how many objects reference the memory address

# 0001 = 10
# 0002 = 15

# name = "Toshe"
# name2 = name
#
# name += " Petrovski"
#
# print(name)
# print(name2)


# MUTTABLE DATA TYPES
# na edna adresa mozeme da stavime eden integer

# ARRAY -> ordered list of values - [0001, 0002, 0003]
# when definining array we must define the ARRAY SIZE;

# LINKED LISTS
# l = [10, 20, 30]  # [{0001-(10), 0002-(0005) }, 0005-(20) , 0009-(30)]
# # l -> 2222 - (0001)
#
# # l.insert(50, 0)
#
#
# for i in l:
#     print(i)

# integers = [10, 20, 30]
# integers2 = integers
#
# integers.append(40)
#
# print(integers)
# print(integers2)

# PASS BY REFERENCE
# SIDE EFFECT -> callables who mutate out of local scope objects

# def test(num):
#     # global num  # -> syntaxic sugar
#     num += 10
#     print(f"From test: {num}")
#
# num = 50
# test(num)
#
# print(num)
