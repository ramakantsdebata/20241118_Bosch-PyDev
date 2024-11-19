# MUTABLE
# List
# Set
# Dictionary
 
# IMMUTABLES
# Numbers
# Strings
# Tuples
# FrozenSet
# NamedTuples
 

## Strings ####################################################################

s1 = "Test"
s2 = 'Test'

s3 = "This is Kartik's notebook"
s4 = 'Kartik says, "Thank you"'
print(s3)
print(s4)

s5 = """This is
a 
multiline
comment."""
print(s5)

s6 = "First""Second"

# "fileName"."ext"
# "fileName"."."."ext"
# "fileName"".""ext"



print(s6)


## Format Strings
# This is a 'Python' training for '5' days at the 'Bangalore' campus in 'November'.
# printf("Number %d fiound", num)     <-- C-Style formatted printing

tech = "Python"
days = 5
location = "Bangalore"
month = "November"

s1 = "This is a %s training for %d days at the %s campus in %s"
print(s1 % (tech, days, location, month))

s2 = "This is a {} training for {} days at the {} campus in {}"
print(s2.format(tech, days, location, month))

s3 = f"This is a {tech} training for {days} days at the {location} campus in {month}"
print(s3)


# Raw String
path = r"c:\Users\temp\newfile"
print(path)


## String Slicing
print(s3[5:15])
print(s3[5:])
print(s3[:15])
print(s3[-1])
print(s3[-8:])
print(s3[-11:-9])
print(">>>", s3[-9:-11])
print(">>>", s3[-10:-12:-1])
print(s3[::-1])

s4 = "0123456789"
print(s4[::2])
print(s4[1::2])

# s4[Begin:End:Step]
