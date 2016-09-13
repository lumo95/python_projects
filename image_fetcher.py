# Name: Image Fetcher
# Created By: Luke Molloy
# Date: 19/08/16
# Desc: A program that takes in a url of an image and saves the image as a jpeg

import random
import urllib.request
import os
import getpass
import time


def get_web_img(url):
    name = random.randrange(1, 100)  # random number to name the file
    full_name = str(name) + " Image_fetcher.jpg"  # adding a file extension and watermark
    path = "C:/Users/" + getpass.getuser() + "/Pictures/"  # path with username
    complete_file = os.path.join(path, full_name)  # joining the path and filename
    urllib.request.urlretrieve(url, complete_file)  # fetching the file from url

print("Welcome to Image Fetcher!\n")
users_url = input("Please enter the image url\n")
get_web_img(users_url)
print("File downloaded. Check your Pictures folder")
time.sleep(5)
