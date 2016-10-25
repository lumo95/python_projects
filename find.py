# Find Module
# Author: Luke Molloy
# Desc: This module takes in lists and finds missing items
# from the lists example (range of nums in list, alphabet)

# Note: call by using find.findnum(x)

import string

# finds missing numbers from the range of the list
def findnum(nums):

    missing = []
    cleaned = set(nums)
    start = int(min(cleaned))
    end = int(max(cleaned) + 1)

    count = 0

    for i in range(start, end):
        count += 1
        if count not in cleaned:
            missing.append(count)

    return missing


# find letter finds the missing alphabetical letters from a list
def findletter(letters):

    missing = []
    count = 0
    alpha = list(string.ascii_lowercase)

    for i in alpha:
        if alpha[count] in letters:
            count+=1
        else:
            missing.append(str(alpha[count]))
            count+=1

    return missing
