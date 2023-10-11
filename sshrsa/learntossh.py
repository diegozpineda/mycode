#!/usr/bin/env python3
#
#

import os
import paramiko

def commandissue(command_to_issue, sshsession):
    """when sshsession.exec_command is issued, it returns a 3-tuple, we are
       only interested in standard out, which is what this function returns"""
    
    # issue command and return 3-touple
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read() # return the standard out

def main():
    """sending commands across ssh"""

    # create ssh via paramiko
    sshsession = paramiko.SSHClient()

    ############# IF YOU WANT TO CONNECT USING UN/PW ################
    #sshsession.connect(server, username=username, password=password)
    ############## IF USING KEYS ####################################

    # our priv key
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")


    # if we never went to this SSH host
    # auto add the fingerprint to the known host file (otherwise the script will hang)
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # if we never went to this SSH host
    # auto add the fingerprint to the known host file (otherwise the script will hang)

    sshsession.connect(hostname="10.10.2.3", username="bender", pkey=mykey)

    # list of commands to issue
    our_commands = ["touch sshworked.txt", "touch create.txt", "touch file3.txt", "ls"]

    # iterate through commands and execute on remote 
    for i in our_commands:
        print(commandissue(i, sshsession).decode('utf-8'))

    # close connection
    sshsession.close()

# exectute main
if __name__ == "__main__":
    main()