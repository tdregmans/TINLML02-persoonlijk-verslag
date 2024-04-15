"""

    TINLML02
    Thijs Dregmans
    https://github.com/tdregmans/TINLML02-persoonlijk-verslag

    Link.py
    Last edited: 2024-04-15 (YYYY-MM-DD)
    Version: 1.0

"""

class Link:
    def __init__(self, target):
        self.target = target
        self.weight = 1 # change weight later

    def activate(self, value):
        self.target.addValue(value * self.weight)
