#!/usr/bin/env python3
##
## EPITECH PROJECT, 2018
##
## File description:
## 101 pong
##

import  sys
import  math
from velocity import *

def main():
    last_parameter = []

    if len(sys.argv) != 8:
        usage_pong()
        sys.exit(84)
    last_parameter = sys.argv[7]
    if '-' in last_parameter:
        print("We can't calculate a negative time...")
        sys.exit(84)
    elif '.' in last_parameter:
        print("Time must be an unsigned integer")
        sys.exit(84)
    else:
        execute_101pong()
        sys.exit(0)

def usage_pong():
    print("USAGE")
    print("      ./101pong x0 y0 z0 x1 y1 z1 n")
    print("DESCRIPTION\n")
    print("       x0   ball abscissa at time t - 1")
    print("       y0   ball ordinate at time t - 1")
    print("       z0   ball altitude at time t - 1\n")
    print("       x1   ball absissa at time t")
    print("       y1   ball ordinate at time t")
    print("       z1   ball altitude at time t\n")
    print("       n    time shift (greater than or equal to zero, integer)")

if __name__ == "__main__":
    main()
