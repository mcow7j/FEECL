# -*- coding: utf-8 -*-
"""This module defines the ``Terminal`` class, the superclass
for all types that are terminal nodes in an expression tree."""

from .form import Form
from .domain import Domain


class Terminal(Form):
    def __init__(self,degree,domain):
        Form.__init__(self,degree,domain)
    def __len__(self):
        return 1
    def __repr__(self):
      attribute_dict=(self.__dict__).copy()
      #delete unwanted info e.g degree
      del attribute_dict['degree'],attribute_dict['domain']
      # This should work for most cases
      r = "%s(%s)" % (self.__class__.__name__, ",".join(str(attribute_dict[i]) for i in attribute_dict))
      return r

### below are the main terminal subclasses in alphebetical order ###

class Argument(Terminal):
    def __init__(self,space,count):
        self.space = space
        super().__init__(space.degree,space.complex.domain)
        if count != 1 and count != 0:
          raise NotImplementedError("Needs to be 1 or 0")
        self.count = count

    def __str__(self):
        if self.count==1:
            return "U"
           # return ("Trial Function")
        else:
           # return ("Test Function")
           return "V"

    def __repr__(self):
        return ("{}({},{})".format(self.__class__.__name__,repr(self.space),self.count))

class BasisForm(Terminal):
    def __init__(self,domain,index=1):
        Terminal.__init__(self,1,domain)
        #index goes from 1 to topological_dim
        self.index=index

    def __str__(self):
        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        return "dx{}".format(self.index).translate(SUB)

    def __repr__(self):
         return "{}({},{})".format(self.__class__.__name__,repr(self.domain),self.index)


class Coefficent(Terminal):
    def __init__(self,space):
        self.space=space
        super().__init__(self.space.degree,self.space.complex.domain)
        self.count=self._count
        self._count+=1
    _count=0

    def __str__(self):
        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        return ("W{}".format(self.count)).translate(SUB)

    def __repr__(self):
        return ("{}({})".format(self.__class__.__name__,repr(self.space)))


class Constant(Terminal):
    def __init__(self,value,domain=None):
        super().__init__(degree=0,domain)
        self.value=value

    def __str__(self):
        return("{}".format(self.value))

    def __repr__(self):
        return ("{}({})".format(self.__class__.__name__,self.value))

    def __mul__(self,other):
        if isinstance(other, Constant):
            return Constant(self.value*other.value)
        else :
            raise ValueError("not possible to multiply try wedge")

    def __rmul__(self,other):
        return self*other

#class VolForm(Terminal):
#    def __init__(self,domain,indexing=None):
#        #indexing is a list, but can be changed to default
##        Terminal.__init__(self,domain.topological_dim,domain)
#        #default indexing from
#        if indexing==None:
#          indexing=[i for i in range(1,domain.topological_dim)]
#        self.indexing=indexing
#
#    def __str__(self):
#        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
#        s=""
#        for i in self.indexing:
#            s += "dx{}{}".format(i,u'\u2227')
#        return s.translate(SUB)[:-1]
#       # return "Vol"
#
#    def __repr__(self):
#        return "{}({},{})".format(self.__class__.__name__,repr(self.domain),self.indexing)
#

#class Zero(Terminal):
#    def __init__(self):
#        super().__init__(degree=0,domain=None)
#        self.value=0
