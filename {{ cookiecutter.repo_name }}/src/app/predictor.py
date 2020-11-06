# -*- coding: utf-8 -*-

from src.ml.code.model import Model


class Predictor(object):

    def __init__(self):
        self.model = Model()
        pass

    def predict(self, data):
        pass
