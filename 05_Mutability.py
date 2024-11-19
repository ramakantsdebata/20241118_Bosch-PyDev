# a = 10
# b = 10
# c = "Test"

# print(a)
# print(type(a))
# print(type(c))

# print(id(a), id(b), sep='\n')

# print(a is b)

############################################

a = 123412
print(id(a), a)
a = 123123
print(id(a), a)

a += 1
print(id(a), a)

s1 = "Test"
print(id(s1), s1)
s1 = "String"
print(id(s1), s1)
s1 += "Data"
print(id(s1), s1)

s1 = "Test"
print(id(s1), s1)

print(s1[0])
s1[0] = "B"

