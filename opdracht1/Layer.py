"""

    TINLML02
    Thijs Dregmans
    https://github.com/tdregmans/TINLML02-persoonlijk-verslag

    Layer.py
    Last edited: 2024-04-18 (YYYY-MM-DD)
    Version: 2.0

"""

import random

# constants for classification of Layers
FIRST = 0
HIDDEN = 1
LAST = 2

class Layer:
    def __init__(self, type = HIDDEN):
        self.type = type
        self.target = target
        self.previousWeights = []
        self.weight = random.random() # random float between 0 and 1 

    def activate(self, value):
        self.target.addValue(value * self.weight)

    def reCalculateWeight(self):
        self.previousWeights.append(self.weight)
        self.weight = random.random() # random float between 0 and 1
