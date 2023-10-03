#!/usr/bin/env python3
#
#
import shutil # shell utilities to move files
import os # os utilities

# Force program to start in home dir
def cd_home():
    os.chdir('/home/student/mycode/')

# move object to specified dir
def move_file():
    shutil.move('raynor.obj', 'ceph_storage/')

# prompt for a new name to rename file
def new_name():
    xname = input(f'What is the new name for kerrigan obj? ')

# Rename the current kerrigan.obj file
def rename_file():
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

def main():
    cd_home()
    move_file()
    new_name()
    rename_file()

if __name__ == "__main__":
    main()
