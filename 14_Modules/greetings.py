__all__ = ["greet", "greetName", "greetInteractive"]


def greet():
    print("Hi there!")

def greetName(name):
    greeting = "Hello"
    final_greeting = prepGreeting(greeting, name)
    print(final_greeting)

def prepGreeting(greeting, name):
    return greeting + " " + name + "!"

def greetInteractive():
    name = input("Enter the name: ")
    final_greeting = prepGreeting("Hi", name)
    print(final_greeting)


def Test_Full():
    greet()
    greetName("Vijay")
    print(prepGreeting("Morning", "Ramakant"))
    greetInteractive()

def Test_NonInteractive():
    greet()
    greetName("Vijay")
    print(prepGreeting("Morning", "Ramakant"))
 
if __name__ == "__main__":
    # Test_Full()
    Test_NonInteractive()

# def Test():
#     greet()
#     greetName("Vijay")
#     print(prepGreeting("Morning", "Ramakant"))
#     greetInteractive()

# # Test()

# # print(dir())

# print(type(__name__), __name__)

# if __name__ == "__main__":
#     Test()
