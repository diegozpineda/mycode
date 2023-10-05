#!/usr/bin/env python3

import subprocess

subprocess.call(["ip", "link", "show", "up"])

print("Checking interfaces in UP status")

interface = input("Enter an interface to check address info: ")

subprocess.call(["ip", "addr", "show", "dev", interface])
subprocess.call(["ip", "route", "show", "dev", interface])
