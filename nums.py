'''
    Author: Luke Molloy
    
    this program will find the missing numbers from a list
    where the list has a range of numbers (e.g 1 - 10)
    the numbers missing from the range are then displayed
    
    note: randint() includes the numbers in the range given
'''

import random


def find_num():
    
    nums = []

    for i in range(1, 11):  #filling the list
        nums.append(i)

    rand_num = random.randint(1, 10)  #random num 1 - 10
    
    random.shuffle(nums)  #shuffling the numbers in list

    nums[rand_num] = ''  #removing a random number
    
    count = 0
    
    print(nums)

    for val in nums:
        count += 1
        if count not in nums:  #checking if all numbers are in list
            print("The missing number is " + str(count))
    
find_num()




