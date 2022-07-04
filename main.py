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
from math import (pi, sqrt, sin, cos)
from cmath import exp  # the normal exp from math module will not work.


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


def dft(sequence: list):
    """calculate discrete-fourier-transform for given sequence."""

    N = len(sequence)

    # define x(k):
    def x(k: int): return sum(sequence_value*exp((-1j*2*pi*k*i)/N)
                              for i, sequence_value in enumerate(sequence))

    return [x(k) for k in range(N)]


def idft(sequence: list):
    """calculate inverse-discrete-fourier-transform for given sequence."""


def main():
    l = dft([*range(1, 5)])

    print(f"Kth\t Real\t Imag")
    for k, item in enumerate(l):
        print(f"X({k})\t  ", end='')
        print(
            f"{str(round(item.real)).center(2)}\t {(str(round(item.imag))+'j').center(3)}")


if __name__ == "__main__":
    main()
