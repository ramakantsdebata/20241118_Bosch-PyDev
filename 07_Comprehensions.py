# Used to create collections from existing collections

# fruits = ["apple", "banana", "cherry", "dragonfruit", "kiwi", "mango"]
# new_bowl = []
# for fr in fruits:
#     if 'a' in fr:
#         new_bowl.append(fr)
# print(new_bowl)

# newList = [fr                for fr in fruits            if 'a' in fr]
# newSet =  {fr                for fr in fruits            if 'a' in fr}
# newDict =  {fr:len(fr)       for fr in fruits            if 'a' in fr}
# newTuple = tuple(fr               for fr in fruits            if 'a' in fr)

# print(type(newList), newList)
# print(type(newSet), newSet)
# print(type(newDict), newDict)
# print(type(newTuple), newTuple)

obj = 10
print(dir(obj))
public_members = [member      for member in dir(obj)      if member.startswith("_") is False]
print(len(public_members))
public_methods = [member      for member in dir(obj)      if member.startswith("_") is False and callable(getattr(obj, member))]
print(len(public_methods))


print(callable(getattr(str, "capitalize")))
