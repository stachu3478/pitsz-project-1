#!/usr/bin/env python
# -*- coding: utf-8 -*-

from verifier import Verifier
from solver.NastySolver import NastySolver
from pathlib import Path

for instance_path in Path('./').iterdir():
    if instance_path.name.startswith('in_'):
        print(instance_path)
        verifier = Verifier(instance_path.name[3:])
        verifier.verify()

