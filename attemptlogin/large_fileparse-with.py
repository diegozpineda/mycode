#!/usr/bin/python3 

loginfail = 0
post = 0

#keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi", "r")
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    for line in kfile:
        if "- - - - -] Authorization failed" in line:
            loginfail += 1
        elif "POST" in line:
            post += 1

print(f"Failed login attempts: {loginfail}")
print(f"Succesfull Posts: {post}")
#keystone_file.close()
