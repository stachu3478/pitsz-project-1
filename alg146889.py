#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pathlib import Path

from solver.BalancedSolver import BalancedSolver
from solver.BalancingBubbleSolver import BalancingBubbleSolver
from solver.BalancingSolver import BalancingSolver
from solver.BubbleSolver import BubbleSolver
from solver.LocalCdmaxCminSolver import LocalCdmaxCminSolver
from solver.LocalCdmaxSolver import LocalCdmaxSolver
from solver.LocalLdmaxSolver import LocalLdmaxSolver
from solver.LocalLdminCminSolver import LocalLdminCminSolver
from solver.LocalLmax0CminSolver import LocalLmax0CminSolver
from solver.LocalLmaxCminSolver import LocalLmaxCminSolver
from solver.LocalLmaxSolver import LocalLmaxSolver
from solver.NastySolver import NastySolver
from solver.SijCmaxSolver import SijCmaxSolver

solver = LocalLdmaxSolver()
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
