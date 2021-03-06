from decimal import *
from math import *

class Razlomak(object):
    '''Klasa razlomak'''
    def __init__(self, brojnik, nazivnik = 1):
        if nazivnik == 0: raise Exception('Nazivnik ne moze biti 0')
        self._brojnik = brojnik
        self._nazivnik = nazivnik
    def __str__(self):
        return '%d|%d' % (self._brojnik, self._nazivnik)

    @staticmethod
    def inverz(self):
        return Razlomak(self._nazivnik, self._brojnik)

    @staticmethod
    def stvori(broj):
        broj_decimala = 0
        naz = 10

        while (broj % 1 != 0):
            broj *= 10
            broj_decimala += 1
        naz = pow(naz, broj_decimala)

        return Razlomak(broj, naz)