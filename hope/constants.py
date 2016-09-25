#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Constants ;)"""

import os

MODULE_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(MODULE_ROOT)
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
DB_PATH = os.path.join(DATA_DIR, 'db.sqlite3')
JSON_PATH = os.path.join(DATA_DIR, 'db.json')
