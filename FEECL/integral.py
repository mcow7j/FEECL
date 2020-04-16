"""creates the integral class"""

from .domain import Domain
from .form import Form
from numbers import Number


def as_form(value):
    if isinstance(value,Form):
        return Value
    elif isinstance(value,Number):
        return Constant(value)
    else:
        raise TypeError("cannot convert {} to form".format(type(value)))

#sort this out

#class Integral(Form):
#    def __init__(self,integrand,domain = None):
#        #integrand is a form
#        self.integrand=integrand
#        self.domain=domain

#        if domain == None:
#            Form.__init__(self,integrand.domain.topological_dim,integrand.domain)
#        elif integrand.degree != domain.topological_dim and domain != None :
#            return ImplementedError("intergrand and domain mismattacted")
#        else:
#            Form.__init__(self,integrand.degree,domain)


class Integral():
    def __init__(self,integrand,domain = None):
        self.integrand=integrand
        if domain == None:
            self.domain=integrand.domain
        else:
            self.domain=domain
        if integrand.degree != domain.topological_dim:
            return ImplementedError("integrand and domain mismattacted")

    def __str__(self):
      return u"\u222B"+str(self.integrand)

    def __repr__(self):
      return "{}({},{})".format(__class__.__name__,self.integrand,repr(self.domain))


    def __add__(self,other):
        self=as_form(self)
        other=as_form(other)
        if self.integrand.degree == other.integrand.degree and domain==domain:
            self.integrand=Sum(self.integrand,other.integrand)
            return self

    def __mul__(self,other):
        self=as_form(self)
        other=as_form(other)
        if wedge(self.integrand,other.integrand).degree==self.degree:
            self.integrand = wedge(self.integrand,other.integrand)
            return self

    def __pos__(self):
        return self

    def __neg__(self):
        self.integrand=wedge(-1,self.integrand)
        return self
