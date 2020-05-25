"""This module defines the ``Expr`` class, the superclass
for all expression tree node types in FEECL.
"""
from .domain import Domain
from numbers import Number

##check add and what error should i be returning

class Form(object):
    """base class for all feecl objects
    """

    def __init__(self,degree,domain):
        self.degree=degree
        self.domain=domain

    def getdegree(self):
        return ("The degree is: {}".format(self.degree))

    def getdomain(self):
        return ("The degree is: {}".format(self.domain))

#check over return/raise
    def __add__(self,other):
        other=as_form(other)
        if self.domain != other.domain or None not in (self.domain,other.domain) :
            raise ValueError("operands missmatched domains")
        if self.degree != other.degree:
            raise ValueError("operands missmatched degrees/not constants")
        return Sum(self,other)

    def __radd__(self,other):
      return Form.__add__(other,self)

    def __pos__(self):
        return self

    def __neg__(self):
        return wedge(-1,self)

    def __sub__(self,other):
        return Form.__add__(wedge(-1,self),other)
