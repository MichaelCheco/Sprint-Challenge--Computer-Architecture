#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

args = sys.argv

if len(args) < 2:
    print("Please provide the path of the file")
    sys.exit(1)

program = args[1]

cpu = CPU()

cpu.load(program)
cpu.run()
