"""

    TINLML02
    Thijs Dregmans
    https://github.com/tdregmans/TINLML02-persoonlijk-verslag

    Link.py
    Last edited: 2024-04-18 (YYYY-MM-DD)
    Version: 1.2

"""

import random

class Link:
    def __init__(self, target):
        self.target = target
        self.previousWeights = []
        self.weight = random.random() # random float between 0 and 1 

    def activate(self, value):
        self.target.addValue(value * self.weight)

    def reCalculateWeight(self):
        self.previousWeights.append(self.weight)
        self.weight = random.random() # random float between 0 and 1
