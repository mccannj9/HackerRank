#! /usr/bin/env python

# https://www.hackerrank.com/challenges/maximum-draws
# Problem name ::: Maximum Draws


def main():

    import sys

    data = [int(line.rstrip()) for line in sys.stdin.readlines()]
    num_tests = data[0]
    for x in range(1, num_tests+1):
        print(data[x]+1)


if __name__ == "__main__":
    main()