"""This module defines the ``Operator`` class, the superclass
for all types that are non-terminal nodes in an expression tree."""

from expr import Expr


class Operator(Expr):
    def __init__(self,degree,domain,operands):
        Expr.__init__(self,degree,domain)
        self.operands=operands

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

    def _ext_div(self):
        #place exception here if not possible
        return Ext_div(self)



class Wedge(Operator):
  def __init__(self,a,b):
      Operator.__init__(self,a.degree,a.domain,(a,b))
      self.degree += b.degree
      self.name = "Wedge"

class Ext_div(Operator):
    def __init__(self,a):
        Operator.__init__(self,a.degree,a.domain,(a))
        if a.degree != a.domain:
          self.degree += 1
        #will need improving at a later date
        else:
          self.degree = 0

class Sum(Operator):
    def __init__(self,a,b):
        Operator.__init__(self,(a,b))
        self.degree = max(a.degree,b.degree)
