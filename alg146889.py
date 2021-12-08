#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from solver.Q4riwu.NastySolver import NastySolver
from generator.Q4rwuInstance import Q4rwuInstance
from solver.Q4riwu.StaticInsertionDLLPTHWSM import StaticInsertionDLLPTHWSM

solver = StaticInsertionDLLPTHWSM()
if len(sys.argv) > 2:
    instance_path = sys.argv[1]
    output_filename = sys.argv[2]
    solver.solve(instance_path, output_filename=output_filename, klass=Q4rwuInstance)
elif len(sys.argv) > 1:
    instance_path = sys.argv[1]
    solver.solve(instance_path, klass=Q4rwuInstance)
