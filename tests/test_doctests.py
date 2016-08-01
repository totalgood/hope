#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import pytest
"""Run doctests and unittests for talkingdata.clean module"""

import doctest
import predict.lstm
import predict.imdb

__author__ = "Hobson Lane"
__copyright__ = "Hobson Lane"
__license__ = "mit"


def test_predict(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS):
    assert doctest.testmod(predict.lstm, optionflags=optionflags).failed == 0
    assert doctest.testmod(predict.imdb, optionflags=optionflags).failed == 0
    # with pytest.raises(AssertionError):
    #     fib(-10)
