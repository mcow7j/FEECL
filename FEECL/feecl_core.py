"""module for all key functions"""
from .operator import Wedge, ExteriorDerivative, HodgeStar
from .terminal import Argument,BasisForm,Coefficent,Constant
from .complex import Complex,FormSpace,HarmonicSpace
from .domain import Domain
from .integral import Integral
from .form import Form
from numbers import Number
from functools import reduce

def as_form(value):
    if isinstance(value,Form):
        return value
    elif isinstance(value,Number):
        return Constant(value)
    else:
        raise TypeError("cannot convert {} to form".format(type(value)))

#wedge
def wedge(a,b):
    a=as_form(a)
    b=as_form(b)
    #remove mul in terminal if this wrong
    if isinstance(a, Constant) and isinstance(b, Constant):
        return a*b
    if a.domain != b.domain and None not in (a.domain,b.domain) :
        raise ValueError("operands missmatched domains")
    return Wedge(a,b)

#outline for d function
def d(a):
    a=as_form(a)
    return ExteriorDerivative(a)


def hodgestar(a):
    a=as_form(a)
    return HodgeStar(a)

def vol(domain):
    vol=BasisForm(domain,0)
    for i in range(1,domain.topological_dim):
        vol=wedge(vol,Basisform(domain,i))
    return vol

def volform(domain):
    return reduce(wedge, (BasisForm(domain,i) for i in range(domain.topological_dim)))

def inner(a,b):
    return Integral(wedge(a,hodgestar(b)))

def trialfunction(a):
    return NotImplementedError

def testfunction(a):
    return NotImplementedError
