"""This module defines the ``Complex`` class,"""
from .domain import Domain

#dictionary tuple of family raise exception
familys=('P-','P','Q-','S')

class Complex():
    def __init__(self,domain,family,polynomial_degree):
        if family not in familys:
            raise ValueError("input string not a known family")
        self.domain=domain
        self.family=family
        self.degree=domain.topological_dim
        self.polynomial_degree=polynomial_degree

        self.harmonic_space = [HarmonicSpace(self,i) for i in range(self.degree+1)]
        self.form_space = [FormSpace(self,i) for i in range(self.degree+1)]
        self.count=self._count
        self._count+=1
    _count=0
        #attribute of harmonic form space

    def __getitem__(self,degree):
      return FormSpace(self,degree)

    def __str__(self):
        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        return ("Complex{}".format(self.count)).translate(SUB)

    def __repr__(self):
        return "{}({},{},{})".format(self.__class__.__name__,repr(self.domain),self.family,self.polynomial_degree)

class FormSpace():
    def __init__(self,complex,degree):
        self.complex=complex
        if degree not in [i for i in range(0,complex.domain.topological_dim+1)]:
            raise ValueError("degree not within dimensions of complex")
        self.degree=degree

    def __str__(self):
        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        return ("Space{}{}".format(self.complex.count,self.degree)).translate(SUB)

    def __repr__(self):
        return "{}({}[{}])".format(self.__class__.__name__,repr(self.complex),self.degree)


class HarmonicSpace(FormSpace):
    def __init__(self,complex,degree):
        FormSpace.__init__(self,complex,degree)

    def __str__(self):
        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        return ("HSpace{}{}".format(self.complex.count,self.degree)).translate(SUB)

    def __repr__(self):
        return "{}({}[{}])".format(self.__class__.__name__,repr(self.complex),self.degree)
