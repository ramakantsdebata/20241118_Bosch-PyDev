# def square(num):
#     return num**2

# print(square(2))


# sq = lambda num : num**2
# print(sq(2))


# tools = []
# tools.append(lambda num : num**2)
# tools.append(lambda num: num%2 == 0)

# print(tools[1](17))


####################################################

PowerOf = []

for val in range(11):
    PowerOf.append(lambda num, exp=val: num**exp)
print(PowerOf[0])
print(PowerOf[7](10))
