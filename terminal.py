# -*- coding: utf-8 -*-
"""This module defines the ``Terminal`` class, the superclass
for all types that are terminal nodes in an expression tree."""

from ufl.log import error, warning
from expr_feecl import Expr



class Terminal(Expr):

    def __init__(self):
        Expr.__init__(self)



    def coefficent(cls):
        def __init__(self,space,name):
            super().__init__()
            self.space=space
            self.name=name

    @classmethod
    def argument(cls):
        def __init__(self,space,count):
            super().__init__()
            self.space=space
            self.count=count

    @classmethod
    def constant(cls):
        def __init__(self,iszero):
            super().__init__()
            self.iszero=iszero




    def evaluate(self, x, mapping, component, index_values, derivatives=()):
        "Get *self* from *mapping* and return the component asked for."
        f = mapping.get(self)
        # No mapping, trying to evaluate self as a constant
        if f is None:
            try:
                try:
                    f = float(self)
                except TypeError:
                    f = complex(self)
                if derivatives:
                    f = 0.0
                return f
            except Exception:
                pass
            # If it has an ufl_evaluate function, call it
            if hasattr(self, 'ufl_evaluate'):
                return self.ufl_evaluate(x, component, derivatives)
            # Take component if any
            warning("Couldn't map '%s' to a float, returning ufl object without evaluation." % str(self))
            f = self
            if component:
                f = f[component]
            return f

class Coefficent(Terminal):
    def __init__(self,space,name):
        super().__init__()
        self.space=space
        self.name=name
        self.count=self._count
        self._count+=1

    _count=0

    def __str__():
