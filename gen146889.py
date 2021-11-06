#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generator.generator import Generator
from generator.Q4rwuInstance import Q4rwuInstance

prefix = 'in_146889_'
print('Generating instances with prefix ' + prefix)
Generator.create_series(prefix, klass=Q4rwuInstance)
print('Done')