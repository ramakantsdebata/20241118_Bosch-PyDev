class SimpleList:
    def __init__(self, items) -> None:
        self.items = list(items)

    def  add (self, data):
        self.items.append(data)

    def __getitem__(self, idx):
        return self.items[idx]
    
    # def __getitem__(self, idx, value):
    #     self.items[idx] = value
    
    def __len__(self):
        return len(self.items)
    
    def __repr__(self) -> str:
        return f"[{self.__class__.__name__}]({self.items!r})"
    
    def SortData(self):
        self.items.sort()


#----------------------------------------

class SortedList(SimpleList):
    def __init__(self, items) -> None:
        super().__init__(items)
        self.items.sort()

    def add(self, data):
        super().add(data)
        self.items.sort()


#----------------------------------------

class IntegerList(SimpleList):
    def __init__(self, items) -> None:
        for data in items:
            IntegerList.validate_data(data)
        super().__init__(items)

    def add(self, data):
        IntegerList.validate_data(data)
        return super().add(data)
    
    @staticmethod
    def validate_data(val) -> bool:
        if isinstance(val, int) == False:
            raise TypeError(f"'{val}' is not an integer")


class SortedIntList(IntegerList, SortedList):
    pass

###################################################################

def Test1():
    sl1 = SimpleList((21, 4, 7, 89, 10))
    sl1.add(6)
    print(len(sl1))
    sl1.SortData()
    print(sl1)
    print(sl1[2])

def Test2():
    sl1 = SortedList((21, 4, 7, 89, 10))
    sl1.add(6)
    print(sl1)
    # sl1[2] = 70
    print(sl1)

def Test3():
    sl1 = IntegerList((21, 4, 7, 89, 10))
    sl1.add(6)
    try:
        sl1.add("7")
    except TypeError as ex:
        print(f"{ex!r}")
    print(sl1)
    # sl1[2] = 70
    print(sl1)


def Test4():
    sil1 = SortedIntList((21, 4, 7, 89, 10))
    print(sil1)
    sil1.add(77)
    print(sil1)


    try:
        sil1.add("78")
    except TypeError as ex:
        print(f"{ex!r}")
    
    try:
        sil2 = SortedIntList([54, 23, 78, "34"])
    except TypeError as ex:
        print(f"{ex!r}")


def Test5():
    sil1 = SortedIntList((21, 4, 7, 89, 10))
    print(f"{sil1.__class__.__bases__=}")
    print(f"{sil1.__class__.__mro__=}")


if __name__ == "__main__":
    Test5()