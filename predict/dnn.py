#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Keras Dense NNRegressor."""
from __future__ import print_function, absolute_import, division
from future.utils import viewitems  # noqa
from past.builtins import basestring  # noqa
from builtins import str  # noqa

from keras.models import Sequential
from keras.layers import Dense, Activation


class NNRegressor(Sequential):
    """Dense (Fully-Connected) Neural Net Regressor based on a stack of Keras layers"""

    # random_state = None
    nb_epoch = 20
    batch_size = 128
    num_inputs = None
    num_outputs = None

    def __init__(self, layers=(400, 64, 10), activation_functions=('relu', 'softmax')):  # , random_state=random_state):
        """Construct a NN model with `layer_sizes` neurons in each layer, including the input and output layers"""
        super(self, NNRegressor).__init__()
        assert len(layers) == len(activation_functions) + 1, "There should be one extra layer, without activation for the input"
        self.num_inputs = layers[0]
        self.num_outputs = layers[-1]
        for (i, (num_neurons, activation_fun)) in enumerate(zip(layers[1:], activation_functions)):
            self.model.add(Dense(output_dim=num_neurons, input_dim=layers[i]))
            self.model.add(Activation(activation_fun))
        self.model.compile(loss='mean_absolute_error', optimizer='rmsprop')
        # self.random_state = random_state

    def fit(self, X, y, nb_epoch=nb_epoch, batch_size=batch_size):
        # self.random_state_ = check_random_state(self.random_state)
        return self.fit(X, y, nb_epoch=nb_epoch, batch_size=batch_size)

    def transform(self, X):
        # num_samples = X.shape[0]
        return self.predict(X)  # random_state_.randn(num_samples, self.num_outputs)
