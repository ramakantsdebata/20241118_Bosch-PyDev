# def add(a:int, b:int) -> int:
#     return a+b

# def sub(a:int, b:int) -> int:
#     pass

# print(add(1, 2, 3.5, 10))
# # Name 
# # ArgList ->
# #   Number of args
# #   Types of the args
# #   Sequence of the Type 

# # Return type is NOT part of function signature

# print(sub(1, 2))

########################################################

# def add1(a, b):
#     return a + b

# def add2(a, b, c):
#     return a + b + c

# def add(*vData, **kwData):        # Packing the args
#     match len(vData):
#         case 2:
#             fn = add1
#         case 3:
#             fn = add2
#         case _:
#             print("Invalid no. of args")
#     return fn(*vData, **kwData)          # Unpacking the args


# #-------------------------------------------------------


# print(add(1, 2))
# print(add(1, 2, 3))


###################################################################


from multipledispatch import dispatch

@dispatch(int, int)
def add(a, b):
    print("add(int, int)")
    return a+b

@dispatch(int, int, int)
def add(a, b, c):
    print("add(int, int, int)")
    return a+b+c

@dispatch(str, str)
def add(a:str, b:str) -> str:
    print("add(str, str)")
    return a + b

print(add(1, 2))
print(add(1, 2, 3))
print(add("Test", "String"))