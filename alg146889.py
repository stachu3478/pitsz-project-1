#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from solver.InsertionSolver import InsertionSolver

solver = InsertionSolver()
if len(sys.argv) > 2:
    instance_path = sys.argv[1]
    output_filename = sys.argv[2]
    solver.solve(instance_path, output_filename=output_filename)
elif len(sys.argv) > 1:
    instance_path = sys.argv[1]
    solver.solve(instance_path)
