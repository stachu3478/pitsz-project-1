#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import os
from pathlib import Path
from solver.Q4riwu.ProperSolver import ProperSolver

from verifier.Q4rwuVerifier import Q4rwuVerifier
from solver.Q4riwu.NastySolver import NastySolver

solver = NastySolver()
if len(sys.argv) > 2:
    instance_path = sys.argv[1]
    alg_or_result_path = sys.argv[2]
    verifier = None
    if (alg_or_result_path.find('alg') != -1) or not (alg_or_result_path.endswith('.txt')):
        with open(alg_or_result_path, 'r') as f:
            exec(f.read())
        verifier = Q4rwuVerifier(instance_path, instance_path.replace('in', 'out'))
    else:
        verifier = Q4rwuVerifier(instance_path, alg_or_result_path)
    verifier.verify()
else:# Path('alg_files.txt').exists():
    my_id = '146889'
    alg_id = '136822'
    for n in range(50, 550, 50):
        out = f"out_{my_id}_{alg_id}_{n}.txt"
        #out = f"out_{alg_id}_{my_id}_{n}.txt"
        in_file = f"in_{my_id}_{n}.txt"
        #if os.path.isfile(out):
        start = time.perf_counter()
        os.system(f"python alg{alg_id}.py {in_file} {out}")
        end = time.perf_counter()
        #print(str(end - start).replace('.', ','))
        verifier = Q4rwuVerifier(in_file, out)
        verifier.verify()

