#! /usr/bin/env python

# https://www.hackerrank.com/challenges/find-point
# Problem name ::: Find the Point


def main():

    import sys

    data = [line.rstrip().split() for line in sys.stdin.readlines()]
    num_points = int(data[0][0])
    for x in range(1, num_points+1):
        points = [int(y) for y in data[x]]
        xcomp = 2*points[2]-points[0]
        ycomp = 2*points[3]-points[1]
        print("%s %s" % (xcomp, ycomp))

if __name__ == '__main__':
    main()