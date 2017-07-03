#! /usr/bin/env python

# https://www.hackerrank.com/challenges/birthday-cake-candles
# Problem name ::: Birthday Cake Candles


def main():

    import sys

    data = [line.rstrip().split() for line in sys.stdin.readlines()]
    num_candles = int(data[0][0])
    for x in range(1, num_candles+1):
        heights = [int(y) for y in data[x]]
        maximum = max(heights)
        blown_out = heights.count(maximum)
        print(blown_out)

if __name__ == '__main__':
    main()