"""creates the integral class"""

from .domain import Domain

class Integral():
    def __init__(self,integrand,domain):
        self.integrand=integrand
        self.domain=domain

    def __str__(self):
      return u"\u222B"+str(self.integrand)+"Vol"

    def __repr__(self):
      return "{}({},{})".format(__class__.__name__,self.integrand,self.domain=domain)

    def __add__(self):
        raise NotImplementedError

    def __sum__(self):
        raise NotImplementedError

    def __pos__(self):
        raise NotImplementedError

    def __neg__(self):
        raise NotImplementedError
