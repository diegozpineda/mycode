#!/usr/bin/env python3
#
#
import shutil
import os

#cd into specified directory
def cd_home_mycode():
    os.chdir("/home/student/mycode")

# copy one file to destination
def copy_file():
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

#copy recursively to destination
def copy_dir():
    shutil.copytree("5g_research/", "5g_research_backup/")

def main():
    cd_home_mycode()
    copy_file()
    copy_dir()

if __name__ == "__main__":
    main()
