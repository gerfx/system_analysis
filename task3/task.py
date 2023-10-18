import sys
from math import log


def task(path):
    with open(path) as csvfile:
        filedata = [[item.rstrip() for item in line.split(",")] for line in csvfile.readlines()]
    H = 0
    print(filedata)
    n = len(filedata)
    for line in filedata:
        for item in line:
            if item != "0":
                t = float(item)/(n - 1)
                H += t * log(t, 2)
    print(-H)


if __name__ == "__main__":
    # task("task3.csv")
    task(sys.argv[1])
