#region Function Syntax
# def hello():
#     print("Hello")

# hello()
# print(type(hello))


# def add(a:int, b:int)->int:
#     return a+b

# print(add(1, 2))
# print(add(1.1, 2.2))
# print(add("Test", "String"))

# class Test:
#     pass

# t1 = Test()
# t2 = Test()

# # add(t1, t2)

#endregion

#region Define earlier vs. Define higher

# def Bar():
#     print("Bar")
#     Baz()

# def Foo():
#     print("Foo")
#     Bar()

# def Main():
#     print("Main")
#     Foo()

# def Baz():
#     print("Baz")

# Main()

#endregion


#region Docstring

# def add(a, b):
#     """Adds two integers only
#     Returns the sum/concatenation of the objects depending on the type"""
#     print(type(a))
#     if isinstance(a, int) == False or isinstance(b, int) == False:
#         print(add.__doc__)
#         return
#     return a + b

# def Main():
#     """Main Function"""
#     print("Strings -->", add("Test", "String"))
#     print("Integers -->", add(1, 2))
#     print(add.__doc__)

# class Integer:
#     """This is the Integer type"""
#     pass

# Main()

#endregion


#region Passing Parameters [Positional, Keyworded, Default]

# def add(a, b):
#     print(f"{a=}, {b=}")
#     return a + b

# print(add(1, 2))    # Positional
# print(add(2, 1))

# print(add(b=2, a=1))    # Keyworded

#############

# def add(a, b=0, c=0):
#     print(f"{a=}, {b=}, {c=}")
#     return a + b + c

# print(add(1, 2, 3))
# print(add(1, 2))
# print(add(1))

#endregion


#region Variable args

lst = [1, 2]
a = lst[0]
b = lst[1]

p, q = lst      # Implicit Unpacking

# lst = [1, 2, 3]
# a, b = lst

# lst = [ [1, 2] ]
# a, b = lst


## Unpacking in the arg list, while making a call
def add(a, b):
    return a + b

lst = [1, 2]

print(add(*lst))            # ' *' prepended to a collection in the CALL unpacks the collection



#endregion