#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solver.NastySolver import NastySolver
from pathlib import Path

solver = NastySolver()
for instance_path in Path('./').iterdir():
    if instance_path.name.startswith('in_'):
        solver.solve(instance_path.name)
        print(instance_path)
