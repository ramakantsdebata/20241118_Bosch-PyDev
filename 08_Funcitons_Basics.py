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

# lst = [1, 2]
# a = lst[0]
# b = lst[1]

# p, q = lst      # Implicit Unpacking

# # lst = [1, 2, 3]
# # a, b = lst

# # lst = [ [1, 2] ]
# # a, b = lst


# ## Unpacking in the arg list, while making a call
# def add(a, b):
#     return a + b

# lst = [1, 2]

# print(add(*lst))            # ' *' prepended to a collection in the CALL unpacks the collection



# # Packing 
# lst = [1, 2, 3]
# a, _, b = lst
# print(a, b)

# # for _ in range(5):
# #     print("Hi")


# lst = [1, 2, 3, 4]
# a, *ignore, b = lst

# print(a, b)
# print(type(ignore), ignore)

# a, *_, b = lst



# # # st = {1, 2, 3, 4}
# # # a, *ignore, b = st
# # # print(ignore)
# # # print(a, b)



# lst = [1, 2, 3, 4, 5, 6, 7]
# # a, *ig1, c, *ig2, b = lst   # <-- Error: Only one permitted


# def add(a, b, *data):         # Variable arg list
#     print(type(data), data)
#     sum = a + b
#     for val in data:
#         sum += val

#     return sum

# # print(add())
# # print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(1, 2, 3, 4))
# print(add(1, 2, 3, 4, 5))

# # (Pos, Kw, VarArg, KwVarArgs)

# def PrintEmp(ProjMgr, AccMgr, *names, **emps):
#     print(f"{ProjMgr=}, {AccMgr=}")
#     print(type(names), f"{names=}")
#     print(type(emps), f"{emps=}")
#     for name in emps.values():
#         print(name)

# PrintEmp("Manish", "Rakesh")
# PrintEmp(ProjMgr="Manish", AccMgr="Rakesh")
# PrintEmp(ProjMgr="Manish", AccMgr="Rakesh", SalesHead="Abhijeet")
# PrintEmp("Manish", "Rakesh", "Abhijeet")
# PrintEmp("Manish", AccMgr="Rakesh", SalesHead="Abhijeet")


# def Func(*args, **kwArgs):
#     print(f"{args=}", f"{kwArgs=}")

# Func()
# Func(1, 2)
# Func(1, 2, x=3)


# ## Special args
# # '/' - args to left of this have to be positional
# # '*' - args to right of this have to be keyworded

# def Print(a, b, /, c, d, *, e, f):
#     print(f"{a=}, {b=}, {c=}, {d=}, {e=}, {f=}")

# # Print(1, 2, 3, 4, 5, 6)
# Print(1, 2, 3, d=4, e=5, f=6)
# # Print(a=1, b=2, c=3, d=4, e=5, f=6)

# def KwFn(*, a, b=0, c):
#     print(f"{a=}, {b=}, {c=}")

# KwFn(a=1, b=2, c=3)
# KwFn(a=1, c=3)

#endregion

#region Recursion

# num = 5
# res = 5 * 4 * 3 * 2 * 1

# def FactIterative(num):
#     prod = 1
#     for i in range(1, num+1):
#         prod *= i
#     return prod

# def FactRec(num):

#     # Termination condition
#     if num == 1:
#         return 1
    
#     prod = num * FactRec(num-1)
#     return prod

# # print(FactIterative(num))

# print(FactRec(num))

#endregion


#region Scopes

# LEGB

####################################################
# def Outer():
#     # global s1
#     s1 = "Outer String"
#     def Inner():
#         # global s1
#         nonlocal s1
#         s1 = "Inner String"
#         print("Inner -->", s1)

#     Inner()
#     print("Outer -->", s1)

# s1 = "Global String"
# Outer()

# print("Global -->", s1)
########################################



########################################
# def Outer():
#     # global s1
#     s1 = "Outer String"
#     print("Outer -->", s1)
#     print(f"{locals()=}")
#     print(f"{globals()=}")

#     x = 10
#     print(f"{locals()=}")

#     globals()['s1'] = "Modified String"

# s1 = "Global String"
# Outer()

# print("Global -->", s1)
########################################


# def Outer():
#     s1 = "Outer String"
#     print("Outer -->", s1)

#     def Inner():
#         # s1 = "Inner String"
#         print("Inner -->", s1)

#     return Inner

# fn = Outer()
# fn()


##################################
# Closures

def PowerOf(exponent):
    def worker(num):
        return num**exponent
    
    return worker

sq = PowerOf(2)
cube = PowerOf(3)

print(sq(2))
print(cube(2))
print(sq(2))

#endregion