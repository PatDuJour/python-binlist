# -*- coding: utf-8 -*-
from binlist import network


class BIN(object):
    def __init__(self, number):
        self.number = number

    def lookup(self):
        for nw in network.ALL:
            for iin in nw.iin_ranges:
                if iin == self.number[:len(iin)]:
                    return nw
