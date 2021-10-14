#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pathlib import Path

from verifier import Verifier
from solver.PanicSolver import PanicSolver
from solver.NastySolver import NastySolver

solver = NastySolver()
if len(sys.argv) > 2:
    instance_path = sys.argv[1]
    alg_or_result_path = sys.argv[2]
    verifier = None
    if alg_or_result_path.find('out') == -1:
        with open(alg_or_result_path, 'r') as f:
            exec(f.read())
        verifier = Verifier(instance_path, instance_path.replace('in', 'out'))
    else:
        verifier = Verifier(instance_path, alg_or_result_path)
    verifier.verify()
else:
    for instance_path in Path('./').iterdir():
        if instance_path.name.startswith('in_'):
            print(instance_path)
            verifier = Verifier(instance_path.name, instance_path.name.replace('in', 'out'))
            verifier.verify()

