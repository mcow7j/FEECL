"""This module defines the ``Operator`` class, the superclass
for all types that are non-terminal nodes in an expression tree."""

from .form import Form

class Operator(Form):
    def __init__(self,degree,domain,operands):
        Form.__init__(self,degree,domain)
        self.operands=operands

    def __len__(self):
            return 1

    def __str__(self):
        if len(self.operands)==2:
          return "({}{}{})".format(str(self.operands[0]),self.symbol,str(self.operands[1]))
        elif len(self.operands) == 1:
          return "{}({})".format(self.symbol, str(self.operands[0]))
        else:
          raise NotImplementedError("No string representation for operators with arity greater than 2")

    def __repr__(self):
        "Default repr string construction for operators."
        # This should work for most cases
        if len(self.operands)==1:
          r = "{}({})".format(self.__class__.__name__,repr(self.operands))
        else:
          r = "{}({})".format(self.__class__.__name__,",".join(repr(op) for op in self.operands))
        return r


### main operators in alphebetical order ###

class ExteriorDerivative(Operator):
    def __init__(self,a):
        Operator.__init__(self,a.degree,a.domain,(a,))
        self.symbol = "d"
        self.degree += 1


class HodgeStar(Operator):
    def __init__(self,a):
        Operator.__init__(self,a.domain.topological_dim,a.domain,(a,))
        self.symbol = "*"
        self.degree -= a.degree

    def __str__(self):
        return ("({}{})".format(str(self.operands),self.symbol))


class Sum(Operator):
    def __init__(self,a,b):
        Operator.__init__(self,a.degree, a.domain or b.domain,(a,b))
        self.symbol = "+"


class Wedge(Operator):
    def __init__(self,a,b):
        Operator.__init__(self,a.degree,a.domain or b.domain,(a,b))
        self.degree += b.degree
        #if self.domain is not None:
        #    if self.degree > self.domain.topological_dim:
        #        self.degree -= self.domain.topological_dim +1
        self.symbol = u'\u2227'




##### these operators are not needed or incomplete #####

class Contraction(Operator):
    def __init__(self,a,b):
        Operator.__init__(self,a.degree,a.domain,(a,b))
        self.degree -= b.degree
        self.name = "contraction"
        self.symbol= u'\u231F'

class InnerProduct(Operator):
    def __init__(self,a):
        Operator.__init__(self,a.degree,a.domain,(a))

    def __str__(self):
        return (u'\u3008'+ '{},{}'.format(str(self.operands[0]),str(self.operands[1]))+u'\u3009')
