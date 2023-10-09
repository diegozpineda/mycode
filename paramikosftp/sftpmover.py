#!/usr/bin/env python3
''' Moving files with sftp'''

import paramiko
import os

def main():
    t = paramiko.Transport("10.10.2.3", 22)
    t.connect(username="bender", password="alta3")
    sftp = paramiko.SFTPClient.from_transport(t)
    for i in os.listdir("/home/student/filestocopy/"):
        if not os.path.isdir("/home/student/filestocopy/"+i):
            sftp.put("/home/student/filestocopy/"+i, "/tmp/"+i)

    sftp.close()
    t.close()

if __name__ == "__main__":
    main()
