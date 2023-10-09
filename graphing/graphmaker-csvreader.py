#!/usr/bin/env python3

import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

def parsecsvdata():
    ''' returns alist
    [0] is LAN
    [1] WAN data'''
    summary = []

    # open csv data
    with open("/home/student/mycode/graphing/2018summary.csv", "r") as downtime:
        # parse csv data with csv.reader
        downdata = csv.reader(downtime, delimiter=",")
        for row in downdata:
            rowdat = (int(row[0]), int(row[1]), int(row[2]), int(row[3]))
            summary.append(rowdat) # add dict to list
        return summary

def main():
    N = 4
    summary = parsecsvdata()
    localnetMeans = summary[0] # LAN data
    wanMeans = summary[1] # data

    ind = np.arange(N)    # the x locations for the groups
    # the width of the bars: can also be len(x) sequence
    width = 0.35

    # describe where to display p1
    p1 = plt.bar(ind, localnetMeans, width)
    # stack p2 on top of p1
    p2 = plt.bar(ind, wanMeans, width, bottom=localnetMeans)

    # Describe the table metadata
    plt.ylabel("Length of Outage (mins)")
    plt.title("2018 Network Summary")
    plt.xticks(ind, ("Q1", "Q2", "Q3", "Q4"))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ("LAN", "WAN"))

    # display the graph
    # plt.show() # you can try this on a Python IDE with a GUI if you'd like
    plt.savefig("/home/student/mycode/graphing/2018summary_v2.png")
    # save a copy to "~/static" (the "files" view)
    plt.savefig("/home/student/static/2018summary_v2.png")
    print("graph created.")


if __name__ == "__main__":
    main()

