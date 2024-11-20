# def MyFunc():
#     print("Starting off")
#     a = 10
#     yield a

#     a += 5
#     yield a

#     a += 5
#     yield a

#     a += 5
#     yield a

#     a += 5
#     yield a


# def Main():
#     gen = MyFunc()
#     print(type(gen))
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))

# Main()

#####################################

# def Numbers(num):
#     i = 0

#     while num > 0:
#         yield i
#         i += 1
#         num -= 1

# def Main():
#     gen = Numbers(3)

#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))

# def UsingInFor():
#     for i in Numbers(10):
#         print(i)

# def UsingRange():
#     gen = range(10)
#     print(next(gen))

# # Main()
# UsingInFor()

#############################################

def FibGen(num):
    a, b = 0, 1
    for i in range(num):
        yield a
        a, b = b, a+b

def Main():
    for val in FibGen(15):
        print(val, end=" | ")
    print()

    gen = FibGen(10)
    print(type(gen))
    print(dir(gen))

Main()