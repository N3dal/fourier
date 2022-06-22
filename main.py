#!/usr/bin/python3
# -----------------------------------------------------------------
# simple script contain common fourier functions for ex:
# DFT, FFT, FOURIER-SERIES, ....., etc.
#
#
#
# Author:N84.
#
# Create Date:Wed Jun 22 23:21:41 2022.
# ///
# ///
# ///
# -----------------------------------------------------------------


from os import system
from os import name as OS_NAME
from math import (pi, sqrt, sin, cos, exp)

# todo: make the script work from the command line directly, by passing args.


def clear():
    """wipe terminal screen."""

    if OS_NAME == "posix":
        # for *nix machines.
        system("clear")

    elif OS_NAME == "windows":
        system("cls")

    else:
        # for other system in the world
        # system("your-os-clear-command")
        pass


clear()


def main():
    pass


if __name__ == "__main__":
    main()
