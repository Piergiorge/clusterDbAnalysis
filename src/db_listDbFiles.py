#!/usr/bin/python

import os, optparse, pprint, sys

usage = "%prog [options] > filelist"
description="List all executable files provided as part of this software package"
parser = optparse.OptionParser(usage=usage, description=description)
parser.add_option("-w", "--maxw", help="Maximum number of characters (D=100)", action="store", type="int", dest="maxw", default=100)
(options, args) = parser.parse_args()

fileloc = os.path.abspath(__file__)
path = os.path.dirname(fileloc)
ls = os.listdir(path)

# Pretty-print into columns
maxw = options.maxw
maxl = max( [ len(s) for s in ls ] )
maxn = int(maxw/maxl)
c = 0
for s in sorted(ls):
    if c >= maxn:
        sys.stdout.write("\n")
        c = 0
    sys.stdout.write(s.ljust(maxl) + "\t")
    c += 1

