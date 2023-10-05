#!/usr/bin/env python3

from subprocess import call

call(["ip", "link", "show", "up"])

print("Checking interfaces in UP status")

interface = input("Enter an interface to check address info: ")

call(["ip", "addr", "show", "dev", interface])
call(["ip", "route", "show", "dev", interface])
