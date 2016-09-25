#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Download required NLTK datasets and prepopulate sqlite database from fixtures"""
from __future__ import division, print_function, absolute_import, unicode_literals
# from builtins import str  # noqa

import nltk

nltk.download('punkt')
nltk.download('vader_lexicon')

# nltk.download('snowball')
# nltk.download('hmm_treebank_pos_tagger')
# nltk.download('maxent_treebank_pos_tagger')
