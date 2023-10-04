#!/usr/bin/env python3
''' Catch specific errors | Alta3 Research'''

while True:
    try:
        print("Let's divide x by y!")
        x = int(input("What is the integer value of x? "))
        y = int(input("What is the integer value of y? "))
        print("The value of x/y: ", x/y)
    except ZeroDivisionError as zerr:
        print("Handling run-time error:", zerr)

    #general error handling
    # meant to catch errors we can't uniquely specify (i.e. don't know of yet)
    except Exception as err:
        # sys.exc_info returns a 3 tuple with info about the exception handled
        print("We did not anticipate that: ", err)
