"""This module defines the ``Operator`` class, the superclass
for all types that are non-terminal nodes in an expression tree."""

from .expr import Expr
from .domain import Domain

class Operator(Expr):
    def __init__(self,degree,domain,operands):
        Expr.__init__(self,degree,domain)
        self.operands=operands

    def __len__(self):
            return 1

    def _wedge(self,b):
        if self.domain != b.domain:
            raise ValueError("operands missmatched domains")
        return Wedge(self,b)

    def _sum(self,b):
        if self.domain != b.domain:
            raise ValueError("operands missmatched domains")
        if self.degree != b.degree and self.degree != 0 and b.degree != 0:
            raise ValueError("operands missmatched degrees/not constants")
        return Sum(self,b)

    def _exterior_derivative(self):
        #place exceptions here
        return ExteriorDerivative(self)

    def _contraction(self):
        #place exceptions here
        return Contraction(self)

    def _inner_product(self):
        #place exceptions here
        return InnerProduct(self)

    def __str__(self):
        if len(self.operands)==2:
          return ("({}{}{})".format(str(self.operands[0]),self.symbol,str(self.operands[1])))
        else:
          return ("{}({})".format(self.symbol,str(self.operands)))

    def __repr__(self):
        "Default repr string construction for operators."
        # This should work for most cases
        if len(self.operands)==1:
          r = "{}({})".format(self.__class__.__name__,repr(self.operands))
        else:
          r = "{}({})".format(self.__class__.__name__,",".join(repr(op) for op in self.operands))
        return r

class Wedge(Operator):
    def __init__(self,a,b):
        Operator.__init__(self,a.degree,a.domain,(a,b))
        self.degree += b.degree
        self.symbol = u'\u2227'

class ExteriorDerivative(Operator):
    def __init__(self,a):
        Operator.__init__(self,a.degree,a.domain,(a))
        self.symbol = "d"
        if a.degree != a.domain:
          self.degree += 1
        #will need improving at a later date
        else:
          self.degree = 0

class InnerProduct(Operator):
    def __init__(self,a):
        Operator.__init__(self,a.degree,a.domain,(a))

    def __str__(self):
        return (u'\u3008'+ '{},{}'.format(str(self.operands[0]),str(self.operands[1]))+u'\u3009')

class Contraction(Operator):
    def __init__(self,a,b):
        Operator.__init__(self,a.degree,a.domain,(a,b))
        self.degree -= b.degree
        self.name = "contraction"
        self.symbol= u'\u231F'

class Sum(Operator):
    def __init__(self,a,b):
        Operator.__init__(self,(a,b))
        self.degree = max(a.degree,b.degree)
