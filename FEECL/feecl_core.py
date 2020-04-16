"""module for all key functions"""
from .operator import Wedge, ExteriorDerivative, HodgeStar
from .terminal import Argument,BasisForm,Coefficent,Constant,VolForm
from .complex import Complex,Formspace
from .domain import Domain
from .integral import Integral
from numbers import Number


def as_form(value):
    if isinstance(value,Form):
        return Value
    elif isinstance(value,Number):
        return Constant(value)
    else:
        raise TypeError("cannot convert {} to form".format(type(value)))

#wedge
def wedge(a,b):
    a=as_form(a)
    b=as_form(b)
    if a.domain != b.domain or None in (a.domain,b.domain) :
        return ImplementedError("operands missmatched domains")
    return Wedge(a,b)

#outline for d function
def d(a):
    a=as_form(a)
    return ExteriorDerivative(a)


def hodgestar(a):
    a=as_form(a)
    return HodgeStar(a)

def volform(domain):
    vol=BasisForm(domain,0)
    for i in range(1,domain.topological_dim):
        vol=wedge(vol,Basisform(domain,i))
    return vol

def InnerProduct(a,b):
    #outline return intragal of 2 forms using wedgehodgestar
