#!/usr/bin/env python

import math
import sys


def extra(length=10.20, width=2.85):
    base_price = 440 * 10.20
    print("Base Price is %d EUR" % base_price)
    if width > 2.5:
        print("Extra is %d EUR" % (math.ceil((width - 2.5) / 0.25) * 0.1 * base_price))


if __name__ == "__main__":
    extra()
