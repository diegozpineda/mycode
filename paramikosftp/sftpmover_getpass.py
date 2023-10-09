#!/usr/bin/env python3
''' Moving files with sftp'''

import paramiko
import os
import getpass

def main():
    #userdir = input('Please provide a directory where we should store file on bender: ')
    t = paramiko.Transport("10.10.2.3", 22)
    t.connect(username="bender", password=getpass.getpass())
    sftp = paramiko.SFTPClient.from_transport(t)
    #sftp.put("file_to_move.txt", userdir + "file_to_move.txt")
    sftp.put("file_to_move.txt", "file_to_move.txt")
    sftp.close()
    #for i in os.listdir("/home/student/filestocopy/"):
    #    if not os.path.isdir("/home/student/filestocopy/"+i):
    #        sftp.put("/home/student/filestocopy/"+i, "/tmp/"+i)

    #sftp.close()
    t.close()

if __name__ == "__main__":
    main()
