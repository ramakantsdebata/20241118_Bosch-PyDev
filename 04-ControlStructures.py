# If else
# from random import randint

# random_number = randint(1, 100)

# if random_number < 50:
#     print("Lesser", random_number)
#     print("Another message")
# elif random_number > 50:
#     print("Greater", random_number)
# else:
#     print("Equal", random_number)


# Loops
## while
# i = 0
# while i < 10:
#     # print(i, i**2, sep="-->", end="  :  ")
#     i += 1
#     if i == 5:
#         # break
#         continue
#     print(i, end=" - ")
# print()


# i = 10
# while i != 0:
# # while i:          Unpythonic
#     print(i, end=" - ")
#     i -= 1
# print()


lst = [1, 2, 3, 4, 5]
i = 0
num = 7
while i < len(lst):
    if lst[i] == num:
        #region String discussion START
        # This is a 'Python' training for '5' days at the 'Bangalore' campus in 'November'.

        # printf("Number %d fiound", num)     <-- C-Style formatted printing

        # tech = "Python"
        # days = 5
        # location = "Bangalore"
        # month = "November"
        # print(f"This is a {tech} training for {days} days at the {location} campus in {month}")

        # s1= "This is a {} training for {} days at the {} campus in {}"
        # print(s1.format(tech, days, location, month))

        # s2 = "This is a %s training for %d days at the %s campus in %s"
        # print(s2 % (tech, days, location, month))

        ## String discussion END
        #endregion

        print(f"Number {num} found")
        break
    i += 1
else:
    print(f"Number {num} NOT found")


## for
num = 11
for i in range(10):
    print(i, sep=" - ")
    if i == num:
        print("Found")
        break
else:
    print("NOT found")

print()

## do-while  <-- NOT SUPPORTED in Python

if num == 10:
    print("It matches")
else:
    pass

# Match Cases (3.10)

from random import randint
random_number = randint(1, 10)

match random_number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case 5:
        print("Five")
    case _:
        print("Out of range")
        
