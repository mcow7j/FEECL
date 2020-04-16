"""This module defines the ``Complex`` class,"""
from .domain import Domain


### add count and harmonicform class


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
        self.harmonicdegree=None
        self.count=self._count
        self._count+=1
    _count=0
        #attribute of harmonic form space

    def __getitem__(self,degree):
      if degree not in self.degrees:
        raise NotImplementedError("degree not within dimensions of complex")
      w=Complex(self.domain,self.family,self.polynomial_degree)
      w.degree=degree
      return w

    def __str__(self):
        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        return ("Complex{}".format(self.count)).translate(SUB)

    def __repr__(self):
        return "{}({},{},{})".format(self.__class__.__name__,repr(self.domain),self.family,self.polynomial_degree)

class FormSpace():
    def __init__(self,complex,degree):
        self.complex=complex[degree]
        self.degree=degree
        self.count=self._count

    def __str__(self):
        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        return ("Space{}{}".format(self.complex.count,self.degree)).translate(SUB)

    def __repr__(self):
        return "{}({}[{}])".format(self.__class__.__name__,repr(self.complex),self.degree)

#does it need to be based on Formspace
class HarmonicSpace(FormSpace):
    def __init__(self,complex,degree,harmonicdegree):
        FormSpace.__init__(self,complex,degree)
        self.complex.harmonicdegree=harmonicdegree

    def __str__(self):
        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        return ("HSpace{}{}".format(self.complex.count,self.harmonicdegree)).translate(SUB)


class HarmonicSpace(FormSpace):
    def __init__(self,harmonicdegree):
        self.harmonicdegree=harmonicdegree
        if harmonicdegree == 0:
            FormSpace.__init__(self,complex[0])

    def __str__(self):
        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        return ("HSpace{}{}".format(self.complex.count,self.harmonicdegree)).translate(SUB)

##### harmonic space inherit from Formspasce
