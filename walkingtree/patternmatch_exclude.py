#!/usr/bin/env python3

import os
import fnmatch

EXCLUDE = ['/usr', '/home', '/var'] ## dont search in these locations

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path, topdown=True):
        if root in EXCLUDE:
            dirs[:] = []
            files[:] = []
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def main():
    """runtime code"""
    lookfor = input("What pattern am I looking for (Example: *.txt or *.cfg) ")
    lookwhere = input("What is the path in which I should search? ")
    print("Results: ", find(lookfor, lookwhere)) # call function

main()
