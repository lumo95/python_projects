# Find Module
# Author: Luke Molloy
# Desc: This module takes in an list of integers and finds
# the missing numbers from the range of numbers in the list

# Note: call by using find.findnum(x)


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
