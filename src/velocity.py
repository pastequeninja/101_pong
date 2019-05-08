#!/usr/bin/env python3
##
## EPITECH PROJECT, 2018
## 101pong
## File description:
## calculates speed vector
##

import math
import sys
from usage import *

def checking_errors(nbr):
    try:
        nbr = int(nbr)
    except ValueError:
        try:
            nbr = float(nbr)
        except ValueError:
            sys.exit(84)
    return (nbr)

def fill_corrects_values(ac, av):
    i = 1

    while (i < ac):
        av[i] = checking_errors(av[i])
        i += 1
    return (av)

def calc_velocity(argv):
    velocity_res = []
    i = 0
    x = 4
    y = 1

    while (i < 3):
        velocity_res.append(argv[x] - argv[y])
        i += 1
        x += 1
        y += 1
    return (velocity_res)

def execute_101pong():
    velocity = []

    sys.argv = fill_corrects_values(len(sys.argv), sys.argv)
    velocity = calc_velocity(sys.argv)
    display_res(velocity)

def display_res(velocity):
    n = sys.argv[7]
    if (velocity[0] == 0 and velocity[1] == 0 and velocity[2] == 0):
        sys.exit(84)
    non = math.acos(math.sqrt(velocity[0]*velocity[0] + velocity[1]*velocity[1]) / math.sqrt(velocity[0]*velocity[0] + velocity[1]*velocity[1] + velocity[2]*velocity[2]))

    print("The velocity vector of the ball is:\n(", end='')
    print("%.2f" % velocity[0], end=', ')
    print("%.2f" % velocity[1], end=', ')
    print("%.2f" % velocity[2], end =')\n')
    print("At time t +", sys.argv[7], end=', ')
    print("ball coordinates will be:\n(", end='')
    print("%.2f" % (sys.argv[4] + velocity[0] * n), end =', ')
    print("%.2f" % (sys.argv[5] + velocity[1] * n), end =', ')
    print("%.2f" % (sys.argv[6] + velocity[2] * n), end =')\n')
    if (sys.argv[3] == 0 and sys.argv[6] == 0):
        print("The incidence angle is:\n0.00 degrees")
        sys.exit(0)
    if (sys.argv[3] > 0 and velocity[2] >= 0):
        print("The ball won't reach the bat.")
        sys.exit(0)
    if (sys.argv[3] < 0 and velocity[2] <= 0):
        print("The ball won't reach the bat.")
        sys.exit(0)
    non_deg = abs(non) * 57.2958
    print("The incidence angle is:")
    while(non_deg > 90):
        non_deg = abs(non_deg - 180)
    print("%.2f" % non_deg, end =' degrees')
    sys.exit(0)
