"""

    TINLML02
    Thijs Dregmans
    https://github.com/tdregmans/TINLML02-persoonlijk-verslag

    Node.py
    Last edited: 2024-04-15 (YYYY-MM-DD)
    Version: 1.0

"""

import Link

class Node:
    def __init__(self):
        self.value = 0
        self.outgoingLinks = []

    def addValue(self, value):
        self.value += value

    def hardReset(self):
        # at the start of the epoch
        self.value = 0

    def addOutgoingLink(self, link):
        self.outgoingLinks.append(link)

    def activateLinks(self):
        for link in self.outgoingLinks:
            link.activate(self.value)