# Name: File fetcher
# Created By: Luke Molloy
# Date: 20/08/16
# Desc: A program that downloads files from a url

from urllib import request

goog_url = 'http://www.textfiles.com/100/914bbs.txt'


def stock_data(csv_url):
    response = request.urlopen(csv_url)  # storing the connection
    csv = response.read()  # reads the data from the url
    csv_string = str(csv)  # storing the data in a string
    new_line = csv_string.split("\\n")  # splits up the string to make it more readable
    save_location = r'new_file.txt'  # r makes the string a raw string (allows explicit chars)
    fw = open(save_location, 'w')

    for line in new_line:
        fw.write(line + "\n")  # at the end of every line add a new line
    fw.close()

stock_data(goog_url)

