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

# def FibGen(num):
#     a, b = 0, 1
#     for i in range(num):
#         yield a
#         a, b = b, a+b

# def Main():
#     for val in FibGen(15):
#         print(val, end=" | ")
#     print()

#     gen = FibGen(10)
#     print(type(gen))
#     print(dir(gen))

# Main()

################################################

def MyGen():            # This is a generator, which will return an iterator when called
    print("Initiating the Generator")
    x = 0
    yield x

    x += 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

    print("Generator Returning")

def IsIterable(obj):
    try:
        iter(obj)
        return True
    except Exception:
        return False

def Main():
    gen  = MyGen()
    print(type(gen))
    print(f"{IsIterable(gen)=}") # Establish if this is an 'Iterable'
    x = 10
    print(f"{IsIterable(x)=}")

    # res = next(gen)
    # print(type(res), res)

    # try:
    #     print(next(gen))
    #     print(next(gen))
    #     print(next(gen))
    #     print(next(gen))
    #     print(next(gen))    # After this, the generator will produce no more values
    #     print(next(gen))
    #     print(next(gen))
    #     print(next(gen))
    #     print(next(gen))
    #     print(next(gen))
    # except StopIteration:
    #     print("Done Iterating")

    # try:
    #     while True:
    #         print(next(gen))
    # except StopIteration:
    #     print("Done Iterating")

    for val in gen:   # 'gen' should be an iterable
        print(val)

    lst = [1, 2, 3]
    for val in lst:     # gets the iterator by using the iter() method --> iter(lst)
        print(val)

Main()