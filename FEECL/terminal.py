# -*- coding: utf-8 -*-
"""This module defines the ``Terminal`` class, the superclass
for all types that are terminal nodes in an expression tree."""

from .expr import Expr


class Terminal(Expr):
    def __init__(self,degree,domain):
        Expr.__init__(self,degree,domain)

class Coefficent(Terminal):
    def __init__(self,space,name):
        super().__init__(degree,domain)
        self.space=space
        self.name=name
        self.count=self._count
        self._count+=1

    _count=0

    def __str__(self):
        return ("W_{}".format(self.count))


class Argument(Terminal):
    def __init__(self,space,count):
        super().__init__(degree,domain)
        self.space=space
        self.count=count

class Constant(Terminal):
    def __init__(self,value):
        super().__init__(degree=0,domain=None)
        self.value=value

    def __str__(self):
        return("{}".format(self.value))

    def __repr__(self):
        return("constant({})".format(self.value))

class Zero(Terminal):
    def __init__(self):
        super().__init__(degree=0,domain=None)
        self.value=0
