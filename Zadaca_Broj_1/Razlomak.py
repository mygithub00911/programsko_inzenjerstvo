class Razlomak(object):

    def __init__(self, brojnik, nazivnik):
        self._brojnik = brojnik
        self._nazivnik = nazivnik

    @property #getter
    def brojnik(self):
        return self._brojnik

    @brojnik.setter #setter
    def brojnik(self, value):
        self._brojnik = value

    @property #getter
    def nazivnik(self):
        return self._nazivnik

    @nazivnik.setter #setter
    def nazivnik(self, value):
        self._nazivnik = value

    def skrati(self):
        manji = 0
        nasao = False
        if self.brojnik < self.nazivnik:
            manji = self.brojnik
        elif self.brojnik > self.nazivnik:
            manji = self.nazivnik
        else:
            self.brojnik = 1
            self.brojnik = 1
            nasao = True
        if (nasao == False):
            while manji > 0:
                if self.brojnik % manji == 0 and self.nazivnik % manji == 0:
                    self.brojnik = self.brojnik // manji
                    self.nazivnik = self.nazivnik // manji
                manji = manji - 1

    def __str__(self):
        return "%d|%d" % (self.brojnik, self.nazivnik)
    def __repr__(self):
        return "Razlomak(%r, %r)" % (self.brojnik, self.nazivnik)
    def __eq__(self, other):
        return (self.brojnik/self.nazivnik).__eq__(other.brojnik/other.nazivnik)
    def __ge__(self, other):
        return (self.brojnik/self.nazivnik).__ge__(other.brojnik/other.nazivnik)
    def __lt__(self, other):
        return (self.brojnik/self.nazivnik).__lt__(other.brojnik/other.nazivnik)
    def __add__(self, other):
        naz = self.nazivnik * other.nazivnik
        return Razlomak(self.brojnik * (naz / self.nazivnik) + other.brojnik * (naz / other.nazivnik), naz)
    def __sub__(self, other):
        naz = self.nazivnik * other.nazivnik
        return Razlomak(self.brojnik * (naz / self.nazivnik) - other.brojnik * (naz / other.nazivnik), naz)
    def __mul__(self, other):
        return Razlomak(self.brojnik * other.brojnik, self.nazivnik * other.nazivnik)
    def __truediv__(self, other):
        brojnik1 = Razlomak(self.brojnik, other.brojnik)
        nazivnik1 = Razlomak(self.nazivnik, other.nazivnik)
        novonastali = Razlomak(brojnik1.brojnik * nazivnik1.nazivnik, brojnik1.nazivnik * nazivnik1.brojnik)
        return novonastali

        print("**test zadaca**")