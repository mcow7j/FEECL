"""creates the integral class"""
#from .terminl import Constant
#from .form import Form
from .core import Form,Constant
from numbers import Number


def as_form(value):
    if isinstance(value,Form):
        return value
    elif isinstance(value,Number):
        return Constant(value)
    else:
        raise TypeError("cannot convert {} to form".format(type(value)))

class Integral():
    def __init__(self,integrand,domain = None):
        self.integrand=integrand
        if domain is None:
            self.domain=integrand.domain
        else:
            self.domain=domain
        if not self.domain:
            raise ValueError("integral has no domain")
        if integrand.degree != self.domain.topological_dim and not isinstance(self.integrand,Constant):
            #won't work for intergrating a constant
            raise ValueError("integrand and domain mismattacted")

    def __str__(self):
      return u"\u222B"+str(self.domain)+'{'+str(self.integrand)+'}'

    def __repr__(self):
      return "{}({},{})".format(__class__.__name__,repr(self.integrand),repr(self.domain))


    def __add__(self,other):
        if isinstance(other,integral):
            return Integral(Sum(self.integrand,other.integrand),self.domain)
        else:
            raise ValueError("other is not an integral type")

    def __mul__(self,other):
        other=as_form(other)
        if isinstance(other,Constant):
            return Integral (wedge(self.integrand,other.integrand),self.domain)
        else:
            raise ValueError("can only multiply by a scalar")

    def __rmul__(self,other):
        return self*other

    def __pos__(self):
        return self

    def __neg__(self):
        return -1*self

    def __eq__(self, other):
        return self.domain==other.domain and self.integrand==other.integrand

    def __ne__(self, other):
        return not self.__eq__(other)
