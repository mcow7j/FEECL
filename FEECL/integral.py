"""creates the integral class"""

from .domain import Domain
from .form import Form

#sort this out

class Integral(Form):
    def __init__(self,integrand,domain):
        self.integrand=integrand
        self.domain=domain
        Form.__init__(self,intergrand.degree,domain)

class Integral(Form):
    def __init__(self,integrand,domain):
        Form.__init__(self,intergrand.degree,domain)
        self.integrand=integrand
        self.domain=domain

    def __str__(self):
      return u"\u222B"+str(self.integrand)

    def __repr__(self):
      return "{}({},{})".format(__class__.__name__,self.integrand,repr(self.domain))

    def __add__(self):
        raise NotImplementedError

    def __sum__(self):
        raise NotImplementedError

    def __pos__(self):
        raise NotImplementedError

    def __neg__(self):
        raise NotImplementedError
