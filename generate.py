#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generator import Generator

prefix = 'instances'
print('Generating instances with prefix ' + prefix)
Generator.create_series_into_folder(prefix)
print('Done')