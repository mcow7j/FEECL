"""creates the domain class used by expr"""
from .core import BasisForm

class Domain():
    _count=0
    def __init__(self,topological_dim,geometric_dim):
        self.geometric_dim=geometric_dim
        self.topological_dim=topological_dim
        self.basis={}
        for i in range(self.topological_dim):
            self.basis[i]=BasisForm(self,i+1)
        self.__class__._count+=1
        self.count=self._count

    def __str__(self):
        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        return ("{}{}".format(u'\u03A9',self.count)).translate(SUB)

    def __repr__(self):
      return "{}({},{})".format(__class__.__name__,self.topological_dim,self.geometric_dim)

    def __eq__(self, other):
        if other.__class__.__name__==self.__class__.__name__:
            return self.count == other.count
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

class ReferenceCell():
    def __init__(self,domain):
        self.domain = domain
        self.topological_dim = domain.topological_dim
        self.count = domain.count

    def __str__(self):
        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        return ("{}{}".format("E",self.count)).translate(SUB)

    def __repr__(self):
      return "{}({})".format(__class__.__name__,repr(self.domain))

    def __eq__(self, other):
        if other.__class__.__name__==self.__class__.__name__:
            return self.count == other.count
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
