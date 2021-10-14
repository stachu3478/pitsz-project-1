#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pathlib import Path

from solver.PanicSolver import PanicSolver
from solver.NastySolver import NastySolver

solver = NastySolver()
if len(sys.argv) > 1:
    instance_path = sys.argv[1]
    solver.solve(instance_path)
    print(instance_path)
else:
    for instance_path in Path('./').iterdir():
        if instance_path.name.startswith('in_'):
            solver.solve(instance_path.name)
            print(instance_path)
