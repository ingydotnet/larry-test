#!/usr/bin/env python

import sys

print "Number of arguments: %s" % len(sys.argv[1:])

for arg in sys.argv[1:]:
  print ">>> %s" % arg
