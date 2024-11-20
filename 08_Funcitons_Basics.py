def hello():
    print("Hello")

hello()
print(type(hello))


def add(a:int, b:int)->int:
    return a+b

print(add(1, 2))
print(add(1.1, 2.2))
print(add("Test", "String"))

class Test:
    pass

t1 = Test()
t2 = Test()

# add(t1, t2)


## Define earlier vs. Define higher


