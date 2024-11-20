def square(num):
    return num**2

print(square(2))


sq = lambda num : num**2
print(sq(2))


tools = []
tools.append(lambda num : num**2)
tools.append(lambda num: num%2 == 0)

print(tools[1](17))