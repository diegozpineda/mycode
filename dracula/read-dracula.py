#!/usr/bin/env python3
#
#

numlines = 0

file = '/home/student/mycode/dracula/dracula.txt'
with open(file, "r") as myfile:
    for i in myfile:
        if "vampire" in i.lower():
            print(i)
            numlines += 1
            with open("testfile.txt", "a") as writefile:
                print(i, file=writefile)

print(f'Total number of lines in file: {numlines}')
