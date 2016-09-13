# Name: Read_write_files
# Created By: Luke Molloy
# Date: 20/08/16
# Desc: A program that allows the user to read and write text files


name = input("Please enter the name of your file\n")
file = open(name + '.txt', 'w')  # create the file and write to it with 'w'
content = input("Enter some text\n")
file.write(content + '\n')
file.close()

read_file = open(name + '.txt', 'r')  # read files with 'r'
text = read_file.read()  # store the files contents

print(text)
read_file.close()
