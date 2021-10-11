#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generator.generator import Generator

prefix = 'in_146889_'
print('Generating instances with prefix ' + prefix)
Generator.create_series(prefix)
print('Done')