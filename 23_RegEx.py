import re

'''
1. Methods
2. Meta characters
3. Special seqences
4. Extensions notations
    * Comment
    * Named pattern
    * positive lookahead
    * negative lookahead
    * positive lookbehind
    * negative lookbehind
'''

string1 = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
    including the FTSE, fell by 11.48% - the worst day since it launched in 1998. \
    The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
    of STOXX 600 shares since its all-time peak on 19 February."

string1 = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% - the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."
string2 = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% - \nthe worst day since it launched in 1998. \nThe panic selling prompted by the coronavirus has wiped £2.7tn off \nthe value of STOXX 600 shares since its all-time peak on 19 February."


def usingModules():
    path = r"c:\Users\temp\newfile.txt"     # raw string
    print(path)

    strPttrn = r"\d{2}"
    rePttrn = re.compile(strPttrn)

    print(strPttrn)
    print(type(rePttrn))

    # res = re.findall(rePttrn, string1)
    res = re.findall(strPttrn, string1)
    print(res)

    ## Search ######################################
    # Looks for the pattern through the entire string and stops after the first match
    res = re.search(strPttrn, string1)
    print(res)
    print(string1[res.span(0)[0]:res.span(0)[1]])

    # Match #####################################
    # Looks for the pattern from the starting of the string and stops after the patterne is found, and returns re.Match obj
    # If pattern is not found, it returns 'None'
    pt1 = r"\w{4}"
    res = re.match(pt1, string1)
    print(res)
    if res is not None:
        print(string1[res.span(0)[0]:res.span(0)[1]])
    else:
        print("No match found")

    ## FullMatch ###################################
    # Similar to match(), attempts to match from the beginning of the string, but it also has to match the entire string.
    print(len(string1))
    pt1 = r".{285}"         # '.' matches any character, apart from a newline
    res = re.fullmatch(pt1, string1)
    print(res)

    ## Split #######################################
    words = string1.split(' ')
    print(len(words), words)

    words = re.split(r"\s", string1)
    print(len(words), words)

    string2 = "The Euro STOXX 600 index, \nwhich tracks all stock markets across Europe including the FTSE, fell by 11.48% - the worst day since it launched in 1998. \nThe panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."
    words = string2.split(' ')
    print(len(words), words)

    words = re.split(r"\s", string2)
    print(len(words), words)

    words = re.split(r"\d{2}", string2)
    print(len(words), words)

    ## Sub - Substitute an occurance of a pattern with a given string
    res = re.sub(r'[A-Z]{2,}', "INDEX ", string1)
    print(type(res), res)

    ## SubN - Similar to sub, but returns a tuple - (<updatedString>, <replCount>)
    res = re.subn(r'[A-Z]{2,}', "INDEX ", string1)
    print(type(res), res)
    print(res[1], "-->", res[0])

def usingGroups():
    res = re.search(r".+\s(.+ex).+(\d\d\s.+).", string1)
    print(res.groups())     # Lists out all the matched groups

    # Individual group
    print(res.group(1))
    print(res.group(2))
    print(res.group(0))
    print(res.group())      # same as group(0)

    print(res.group(1, 2))
    
    print(res.span(1))
    print(res.span(2))

    print(res.start(1), res.end(1))
    print(res.start(2), res.end(2))

def usingFlags():
    res = re.findall(r'the', string1, re.I)     # Ignorecase
    print(len(res), "-->", res)

    string2 = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% - \nthe worst day since it launched in 1998. \nThe panic selling prompted by the coronavirus has wiped £2.7tn off \nthe value of STOXX 600 shares since its all-time peak on 19 February."
    res = re.findall(r'^the', string2, re.I|re.M)       # Multiline
    print(len(res), "-->", res)

    print(len(string2))
    pt1 = r".{288}"         # '.' matches any character, apart from a newline
    res = re.fullmatch(pt1, string2, re.S)      # DOTALL - enable the '.' to match newline chars as well.
    print(res)

    res = re.search(r'''.+\s        # Some chars of no interest in the beginning
                    (.+ex)          # word ending with the substring 'ex'
                    .+              # all chars in the middle
                    (\d\d\s.+)      # the date data we're looking for
                    .               # the last insignificant character
                    ''', string1, re.X)
    print(res.groups())

def usingMetaCharacters():
    # '.' - Matches any character but the newline, unless re.S / re.DOTALL is provided as a flag
    res = re.search(r'(.+)', string2)
    print(res)
    print(res.groups())
    if string2 == res.group(1):
        print("There are no newlines")
    else:
        print("Newlines present")

    # ^ - Matches at the beginning of each line
    res = re.findall(r'^\w{3}', string2, re.M)
    print(res)

    # $ - Matches at the end of each line
    res = re.findall(r'\s\w{2,}\W*$', string2, re.M)
    print(res)

    # \A - Matches at the beginning of the entire string
    res = re.findall(r'\A\w{3}', string2, re.M)
    print(res)

    # \Z - Matches at the end of the entire string
    res = re.findall(r'\s\w{2,}\W*\Z', string2, re.M)
    print(res)

    # * - zero or more occurances of the preceeding pattern,
    #     in a manner that it attempts to capture as much as possible
    #     Hence, also known as having a GREEDY behaviour

    res = re.search(r'(.*)\s', string1)
    print(res)
    print(string1[:res.end(1)])

    # + - one or more occurances of the preceeding pattern,
    #     in a manner that it attempts to capture as much as possible
    #     Hence, also known as having a GREEDY behaviour

    res = re.search(r'(.+)\s', string1)
    print(res)
    print(string1[:res.end(1)])

    # ? - zero or one occurance of the preceeding pattern,
    #     in a manner that it attempts to capture as much as possible
    #     Hence, also known as having a GREEDY behaviour

    res = re.search(r'(.?)\s', string1)
    print(res)
    print(string1[:res.end(1)])


    print("-"*40)
    ## NON-Greedy Behaviour - Enforced by the '?'
    res1 = re.search(r'(.*?)\s', string1)
    res2 = re.search(r'(.+?)\s', string1)
    res3 = re.search(r'(.??)\s', string1)

    print(string1[:res1.end(1)])
    print(string1[:res2.end(1)])
    print(string1[res3.start(1):res3.end(1)])

    res1 = re.search(r'(.{2,})\s', string1)

def usingSpecialSeq():
    # \ - one of two meanings 
    #       1. Special sequence - \d, \w, \W, \A, \Z
    #       2. Escape the special meaning of metacharacters - \.   \[  \] \( \)

    # \A (Start of the string, not line), \Z (End of the string, not line)

    # \d - Matches any digit, \D - Matches any non-digit
    # \w - Matches any alphanumeric, \W - Matches any non-alphanumeric
    # \b - Matches non-alphanumeric characters before/after an alphanumeric character (Word Boundary)
    # \B - Anything but a word boundary

    res = re.findall(r'E\w*?\s', string1)
    print(res)

    res = re.findall(r'\bcross\s', string1)
    print(res)

    # \s -  Whitespace ( \t\n\r\f\v) - space, tab, newline, return-carriage, formfeed, vertical-tab
    # \S - Anything but a whitespace

    # Character case - [A-Z], [A-Za-z0-9], [aeiou]
    res = re.findall(r'[aeiou]', string1)
    print(res)
    st = set(res)
    print("All Vowels in place?", True if len(st) == 5 else False)

    dt = { alpha : res.count(alpha)  for alpha in "aeiou"}
    print(dt)

if __name__ == '__main__':
    usingModules()
    # usingGroups()
    # usingFlags()
    # usingMetaCharacters()
    # usingSpecialSeq()