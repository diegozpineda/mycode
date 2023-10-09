#!/usr/bin/env python3
'''graphs and charts with matplotlib and numpy'''

import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

def main():
    # lan length of outage min
    N = 4
    localnetMeans = (20, 35, 30, 35)
    # wan outage (min)
    wanMeans = (25, 32, 34, 20)
    # bar width (can also ben len(x))
    width = 0.35

    #describe where to display p1
    p1 = plt.bar(ind, localnetMeans, width)
    # stack p2 on top of p1
    p2 = plt.bar(ind, wanMeans, width, bottom=localnetMeans)

    #describe the table metadata
    plt.ylabel("Length of Outage (mins)")
    plt.title("2018 Network Summary")
    plt.xticks(ind, ("Q1", "Q2", "Q3", "Q4"))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ("LAN", "WAN"))

    #display graph
    # plt.show()
    plt.savefig("/home/student/mycode/graphing/2018summary.png")
    # save a copy to ~/static
    plt.savefig("/home/student/static/2018summary.png")

if __name__ == "__main__":    
    main()
