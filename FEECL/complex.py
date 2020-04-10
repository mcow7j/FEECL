"""This module defines the ``Complex`` class,"""
from .domain import Domain

#dictionary tuple of family raise exception
familys=('P-','P','Q-','S')

class Complex():
    def __init__(self,domain,family,polynomial_degree):
        self.domain=domain
        if family not in familys:
            raise NotImplementedError("input string not a known family")
        self.family=family
        self.degrees=[i for i in range(0,domain.topological_dim)]
        self.degree=domain.topological_dim
        self.polynomial_degree=polynomial_degree

    def __getitem__(self,degree):
      if degree not in self.degrees:
        raise NotImplementedError("degree not within dimensions of complex")
      w=Complex(self.domain,self.family,self.polynomial_degree)
      w.degree=degree
      return w

    def __str__(self):
        return "Complex"

    def __repr__(self):
        return "{}({},{},{})".format(self.__class__.__name__,repr(self.domain),self.family,self.polynomial_degree)

class FormSpace():
    def __init__(self,complex,degree):
        self.complex=complex[degree]
        self.degree=degree

    def __str__(self):
        return "Space"

    def __repr__(self):
        return "{}({}[{}])".format(self.__class__.__name__,repr(self.complex),self.degree)
