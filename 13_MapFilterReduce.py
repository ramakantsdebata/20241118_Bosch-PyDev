names = ["manish", "abhijeet", "vinayak", "shankar", "rakesh"]

## Map - Capitalize all names
resMap = list(map(str.capitalize, names))
print(type(resMap), resMap)


# Filter - Only Names that have an 'r'
def HasR(word:str):
    if 'r' in word.lower():
        return True
    return False

resFil = list(filter(HasR, names))
print(resFil)

# Reduce - Combine all names (Capitalize, add hypen)
from functools import reduce

def NameCombine(n1:str, n2:str):
    return n1 + " - " + n2.capitalize()

names = ["Manish", "abhijeet", "vinayak", "shankar", "rakesh"]

combined = reduce(NameCombine, names)
print(combined)
