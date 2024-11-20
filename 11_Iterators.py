# lst = [1, 2, 3, 4, 5]

# it1 = iter(lst)  # calling iter() on an iterable
# print(type(it1))

# it2 = iter(it1) # calling iter() on an iterator
# print(type(it2))

# print(it1 is it2)


# lst.__iter__()
# # Iterables support the iter() only (not the next())

# it1.__iter__()
# it1.__next__()
# # Iterators support both, iter() and next()


#####################################################################

# Iterator for FibGen

class FibGen:
    def __init__(self, num) -> None:
        self.num = num
        # self.a = 0
        # self.b = 1
        # self.count = 0

    def __iter__(self):
        self.a = 0
        self.b = 1
        self.count = 0
        return self
    
    def __next__(self):
        if self.count < self.num:
            self.count += 1
            temp = self.a
            self.a, self.b = self.b, self.a + self.b
            return temp
        else:
            raise StopIteration


#------------------------------------------------

def Main1():
    for val in FibGen(15):
        print(val, end=" | ")
    print()

    obj = FibGen(3)
    # print(type(obj))
    # it1 = iter(obj)
    # print(type(it1))

    it1 = iter(obj)
    print(next(it1))
    print(next(it1))
    print(next(it1))
    # print(next(it1))

    print("-"*20)
    it2 = iter(obj)
    print(next(it2))
    

def Main2():
    obj = FibGen(10)

    for val in obj:
        print(val, end=", ")
    print()

    for val in obj:
        print(val, end=", ")
    print()

Main2()