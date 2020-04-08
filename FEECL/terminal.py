# -*- coding: utf-8 -*-
"""This module defines the ``Terminal`` class, the superclass
for all types that are terminal nodes in an expression tree."""

from .expr import Expr
from .domain import Domain


class Terminal(Expr):
    def __init__(self,degree,domain):
        Expr.__init__(self,degree,domain)
    def __len__(self):
        return 1
    def __repr__(self):
      attribute_dict=(self.__dict__).copy()
      #delete unwanted info e.g degree
      del attribute_dict['degree'],attribute_dict['domain']
      # This should work for most cases
      r = "%s(%s)" % (self.__class__.__name__, ",".join(str(attribute_dict[i]) for i in attribute_dict))
      return r

class Coefficent(Terminal):
    def __init__(self,space,name):
        #obtain degree domain from space
        super().__init__(degree=None,domain=None)
        self.space=space
        self.name=name
        self.count=self._count
        self._count+=1
    _count=0

    def __str__(self):
        return ("W_{}".format(self.count))

class Argument(Terminal):
    def __init__(self,space,count):
        #obtain degree domain from space?
        super().__init__(degree=None,domain=None)
        self.space = space
        self.count = count

class Constant(Terminal):
    def __init__(self,value):
        super().__init__(degree=0,domain=None)
        self.value=value

    def __str__(self):
        return("{}".format(self.value))

    def __repr__(self):
        return ("{}({})".format(self.__class__.__name__,self.value))

class Zero(Terminal):
    def __init__(self):
        super().__init__(degree=0,domain=None)
        self.value=0
