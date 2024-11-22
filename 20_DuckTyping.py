class Animal:
    def Speak(self):
        print("speaking...")

class Dog:#(Animal):
    def Speak(self):
        print("Woof")

class Cat:#(Animal):
    def Speak(self):
        print("Meow")

class Cow:#(Animal):
    # def Speak(self):
    #     print("Moo")
    pass


def Communicate(obj:Animal):
    obj.Speak()

class Bird:
    def Speak(self):
        print("Chirp")

def Test1():
    d = Dog()
    c = Cat()
    cw = Cow()

    b = Bird()

    Communicate(d)
    Communicate(c)
    # Communicate(cw)   ## <-- ERROR
    Communicate(b)


if __name__ == "__main__":
    Test1()