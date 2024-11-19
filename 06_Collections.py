# MUTABLE
# List
# Set
# Dictionary
 
# IMMUTABLES
# Numbers
# Strings
# Tuples
# FrozenSet
# NamedTuples
 

## Strings ####################################################################

# s1 = "Test"
# s2 = 'Test'

# s3 = "This is Kartik's notebook"
# s4 = 'Kartik says, "Thank you"'
# print(s3)
# print(s4)

# s5 = """This is
# a 
# multiline
# comment."""
# print(s5)

# s6 = "First""Second"

# # "fileName"."ext"
# # "fileName"."."."ext"
# # "fileName"".""ext"



# print(s6)


# ## Format Strings
# # This is a 'Python' training for '5' days at the 'Bangalore' campus in 'November'.
# # printf("Number %d fiound", num)     <-- C-Style formatted printing

# tech = "Python"
# days = 5
# location = "Bangalore"
# month = "November"

# s1 = "This is a %s training for %d days at the %s campus in %s"
# print(s1 % (tech, days, location, month))

# s2 = "This is a {} training for {} days at the {} campus in {}"
# print(s2.format(tech, days, location, month))

# s3 = f"This is a {tech} training for {days} days at the {location} campus in {month}"
# print(s3)


# # Raw String
# path = r"c:\Users\temp\newfile"
# print(path)


# ## String Slicing
# print(s3[5:15])
# print(s3[5:])
# print(s3[:15])
# print(s3[-1])
# print(s3[-8:])
# print(s3[-11:-9])
# print(">>>", s3[-9:-11])
# print(">>>", s3[-10:-12:-1])
# print(s3[::-1])

# s4 = "0123456789"
# print(s4[::2])
# print(s4[1::2])

# # s4[Begin:End:Step]


## LIST #######################################################################
# Collection of non-homogeneous element

# lst = [1, 2, 3, 4, 5, "Test", 3.5]

# for i in range(len(lst)):
#     print(lst[i])

# # All collections are iterables
# for val in lst:
#     print(val, end=" - ")
# print()

# print(type(lst))
# it1 = iter(lst)
# print(type(it1))

# print(len(lst))

# # def len(obj):
# #     obj.__len__()

# print(dir(lst))
# print(lst.__len__())

# print(lst)
# print(str(lst))
# print(lst.__str__())

# class Test:
#     pass

# t1 = Test()
# print(t1)
# print(str(t1))
# print(t1.__str__())
# print(t1.__repr__())

# print(lst.__repr__())


# print(lst[1])

# mat1 = [[1, 2, 3], [4], [5, 6, 7, 8]]
# for row in mat1:
#     for ele in row:
#         print(ele, end='\t')
#     print()

# print(mat1[1][0])


# mat1.append(22)                     # arg has to be an object
# print(mat1)
# mat1.extend([111, 222, 333])        # Arg has to be an iterable (any collection)
# print(mat1)

# mat1.append([1111, 2222, 3333])
# print(mat1)


# print(mat1[6])
# print(3333 in mat1)

# idx = mat1.index(333)
# print(idx)

# print(3333 in mat1[7])

# s1 = "This is the second day of the training."

# l1 = []
# l2 = [1, 2, 3, 4]
# l3 = list()
# l4 = list(s1)

# print(l4)
# print(l4.count('e'))

# for ch in s1:
#     print(ch)

# l4.sort()
# print(l4)


# l5 = list(range(100))
# print(min(l5), max(l5), sum(l5))


# str1 = "TestString"
# str2 = str1
# str1 += "!"

# print(f"{str1=}")
# print(f"{str2=}")


# lst1 = [1, 2, 3, 4, 5]
# lst2 = lst1[:]
# lst1[1] = 200
# print(f"{lst1=}")
# print(f"{lst2=}")

# # print(lst1[:])

# lst1.insert(2, 25)
# print(lst1)
# print(lst1.pop(2))


## Set (Mutable) - Collection of keys (hashable types) ###################################################

lst = [1, 2, 3, 4, 5]
s1 = "Test String"
print(hash(s1))


print(hash(1234567))


st1 = set()
st2 = set(lst)
lst.append([1, 2])
print(st2)
# st3 = set(lst)


st2.add("Test")
print(st2)

st2.update(['a', 'b', 'c'])
print(st2)

st1 = {'a', 'b', 'c', 'd'}
st2 = {'c', 'd', 'e', 'f'}

print(st1 | st2, st1.union(st2))
print(st1 & st2, st1.intersection(st2))
print(st1 - st2, st1.difference(st2))

## Frozenset - Immutable set ####
fs1 = frozenset(st1)
print(fs1)

print(hash(fs1))


## Dictionary - Collections of key-values pairs ###############################

lst1 = [1, 2, 3, 4, 5]
dt1 = dict()
for val in lst1:
    sq = val**2
    dt1[val] = sq

print(dt1)

lst1.append(fs1)
dt2 = dict.fromkeys(lst1)
print(dt2)

print(dt1[3])
if 6 in dt1:
    dt1[6] = 100
else:
    print("Key not found")

# print(dt1[6])
print(dt1.get(6))

print(dt1.pop(3))           # When we know the key for which the value is required
print(dt1.popitem())        # When key is not known, just any k-v pair is required

dt2 = dict.fromkeys(st1)
dt2[4] = 400
dt2[2] = 200
dt1.update(dt2)
print(dt1)

for key in dt1.keys():
    print(key, end="  ")
print()

for value in dt1.values():
    print(value, end="  ")
print()

for key, value in dt1.items():
    print(f"[{key} --> {value}]", end="  ")

for key in dt1:
    print(key, end="  ")
print()


lst1 = list(dt1)
print(lst1)

print(dt1)
del dt1[4]
print(dt1)
