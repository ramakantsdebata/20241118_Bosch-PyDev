class Wheel:
    def __init__(self, brand, type) -> None:
        self.brand = brand
        self.type = type

    def GetTrack():
        return "Can run on slipperry roads"

class Registration:
    def __init__(self, auth, number) -> None:
        self.regAuthority = auth
        self.regNumber = number

    def __str__(self) -> str:
        return f"{self.regNumber} [{self.regAuthority}]"

class Car:
    _count = 0   # Class attribute

    def __init__(self, make, model, color, year, batch) -> None:
        self._make = make
        self._model = model
        self._color = color
        self._year = year
        self.__batch = batch
        self._wheels = [Wheel("MRF", "Alloy") for _ in range(4)]
        self.serialNo = Car.GenSerial()
        Car._count += 1

    def Start(self):
        print(f"Starting {self._color} {self._make}...")

    def Stop(self):
        print(f"Stopping {self._color} {self._make}...")

    def Register(self, reg):
        self.__registration = reg

    def __str__(self):
        return f"{self._make}, {self._model}, {self._color}, {self._year}, {self.__registration}, {self.__batch}"
    
    def __repr__(self) -> str:
        return f"{self._make}, {self._model}, {self._color}, {self._year}, {self.__registration}, WheelCount - {len(self._wheels)}, {self.serialNo}, {self.__batch}"
    
    def __eq__(self, other) -> bool:
        return self.__registration.regNumber == other.__registration.regNumber
    
    def GetRegNumber(self):
        return self.__registration.regNumber
    
    @property
    def Color(self):
        raise NotImplemented
        # return self._color
    

    @Color.setter
    def Color(self, new_color):
        if new_color == "Red":
            raise ValueError("Pick any color other than 'Red'.")
        self._color = new_color

    @classmethod
    def GetCount(cls):
        return Car._count

    @staticmethod
    def GenSerial():
        from random import randint
        return randint(1, 100000)


#################################################################


def Test1():
    reg1 = Registration("RTO", "KA 234 2 2332")
    # reg2 = Registration("RTO", "KA 234 2 2332")
    reg2 = Registration("RTO", "KA 2325 6 77")
    c1 = Car("Honda", "Accord", "Black", 2024, 5)
    c2 = Car("Toyota", "Camry", "White", 2024, 6)

    c1.Register(reg1)
    c2.Register(reg2)

    print(type(c1), dir(c1))

    c1.Start()
    c2.Start()

    # print(c1.GetDetails())
    print(c1)
    print(repr(c1))

    if c1 == c2:
        print("It's the same car")
    else:
        print("We have 2 distinct cars.")

    print(c1.GetRegNumber())
    print(">>", c1._Car__registration.regNumber)
    c1.__batch = 10
    print(c1.__batch)
    print(c1)

    c1.manual = True
    # To prevent dynamic addition/removal of members in a class, use __slots__
    print(c1.__dict__)

    # print(c1.GetColor())
    # c1.SetColor("Blue")

    # print(c1._color)
    # c1._color = "Grey"


    # print(c1.Color)       # <-- Not Implemented
    c1.Color = "Pink"

    print(c1)

    print(c1.GetCount())

    # print(c1.__class__.__name__)

    print(c1)
    print(repr(c1))
    print(repr(c2))

if __name__ == "__main__":
    Test1()