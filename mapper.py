#!/usr/bin/env python
import sys
import csv
infile = sys.stdin
next(infile)
for line in infile:
    line = line.strip()
    line = line.lower()
    words = csv.reader([line])
    for word in words:
        print '%s\t%s' % (word[9], 1)
