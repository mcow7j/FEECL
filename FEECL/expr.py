"""This module defines the ``Expr`` class, the superclass
for all expression tree node types in FEECL.
"""
from .domain import Domain

class Domain():
    def __init__(self,geometric_dim,topological_dim):
        self.geometric_dim=geometric_dim
        self.topological_dim=topological_dim
        self.basis={}
        for i in range(self.topological_dim):
            self.basis[i]="dx{}".format(i)

    def __str__(self):
      return "Domain"

    def __repr__(self):
      return "{}({},{})".format(__class__.__name__,self.geometric_dim,self.topological_dim)


class Expr(object):
    """base class for all feecl objects
    """

    def __init__(self,degree,domain):
        self.degree=degree
        self.domain=domain

    def getdegree(self):
        return ("The degree is: {}".format(self.degree))

    def getdomain(self):
        return ("The degree is: {}".format(self.domain))

    def __add__(self,other):
      raise NotImplementedError
      #e.g if dtype is interger or float convert to constant with same domain
        #if type(self)==

    def __radd__(self,other):
      return add(other,self)

    def __pos__(self):
        return self

    def __neg__(self):
        return Wedge(Constant(-1),self)
