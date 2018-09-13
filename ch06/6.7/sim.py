#!/usr/bin/env python

import argparse
from datetime import datetime
import random

nr_boys = 0
nr_girls = 0

def birth_until_daughter():
    nr_boys = 0
    while True:
        if random.randint(0, 1) == 1:
            nr_boys += 1
        else:
            break
    return nr_boys

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('family', nargs='?', type=int, default=1000,
            metavar='family', help='number of families')
    args = parser.parse_args()
    nr_families = args.family

    random.seed(datetime.now())

    nr_boys = 0
    nr_girls = 0
    while nr_girls < nr_families:
        nr_boys += birth_until_daughter()
        nr_girls += 1
    print "%.5f boys per girls (%d boys, %d girs)" % (
            (float(nr_boys) / nr_girls), nr_boys, nr_girls)
