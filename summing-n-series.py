#! /usr/bin/env python

# https://www.hackerrank.com/challenges/summing-the-n-series
# Problem name ::: Summing the N series
# Accepted

# Proof by induction:
# Sn = n^2
# S(n+1) = Sn + T(n+1)
# T(n+1) = (n+1)^2-((n+1)-1)^2 = (n+1)^2-n^2 = 2n + 1
# S(n+1) = Sn + 2n + 1 = n^2 + 2n + 1
# S(n+1) = (n+1)^2
# The sum is simply the sum first n odd numbers

def main():

    import sys
    
    # don't even need the first line of data
    data = [int(line.rstrip()) for line in sys.stdin.readlines()][1:]
    for val in data:
    	# forgot to put the modulo here
        print(val**2 % ((10**9) + 7))

if __name__ == '__main__':
    main()
