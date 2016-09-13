# Name: Word Counter
# Created By: Luke Molloy
# Date: 23/08/16
# Desc: A program that reads a txt file and counts the number of words
# then outputs the amount of times a word is used

import operator


def start(file_name):
    word_list = []
    with open(file_name, "r") as search_file:
        content = str(search_file.read().replace('\n', ''))
    words = content.lower().split()
    for each_word in words:
        word_list.append(each_word)
    clean_list(word_list)


def clean_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "!£$%^&*\"()-_=+}{][#~@':;?/>.<,'"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_word_list.append(word)
    word_dictionary(clean_word_list)


def word_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
        print("The word '" + key + "' appeared " + str(value) + " time(s)")

file = input("Please enter the filename you want to search!\n")
start(file)
