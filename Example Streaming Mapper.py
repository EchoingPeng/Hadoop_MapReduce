#!/usr/bin/python
import re
import sys

for line in sys.stdin:
    vals = line.strip()
    key = vals.split(' ')[0]
    print key, "\t", "1"