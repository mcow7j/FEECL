"""creates the domain class used by expr"""
from .core import BasisForm

class Domain():
    def __init__(self,geometric_dim,topological_dim):
        self.geometric_dim=geometric_dim
        self.topological_dim=topological_dim
        self.basis={}
        for i in range(self.topological_dim):
            self.basis[i]=BasisForm(self,i+1)
        self.count=self._count
        self._count+=1
    _count=0

    def __str__(self):
        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        return ("Domain{}".format(self.count)).translate(SUB)

    def __repr__(self):
      return "{}({},{})".format(__class__.__name__,self.geometric_dim,self.topological_dim)
