#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pathlib import Path
from solver.InsertionSolver import InsertionSolver

solver = InsertionSolver()
if len(sys.argv) > 1:
    instance_path = sys.argv[1]
    solver.solve(instance_path)
    print(instance_path)
elif Path('alg_files.txt').exists():
    f = open('alg_files.txt')
    l_maxs = []
    timings = []
    while True:
        instance_filename = f.readline().strip()
        if instance_filename == '':
            break
        l_max, timing = solver.solve(instance_filename)
        l_maxs.append(l_max)
        timings.append(timing)
    print('Ordered L maxes:')
    for l_max in l_maxs:
        print(str(l_max))
    print('Ordered timings in ms:')
    for timing in timings:
        print(str(timing).replace('.', ','))
else:
    for instance_path in Path('./').iterdir():
        if instance_path.name.startswith('in_'):
            solver.solve(instance_path.name)
            print(instance_path)
