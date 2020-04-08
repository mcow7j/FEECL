"""This module defines the ``Complex`` class,"""
from .domain import Domain

class Complex():
    def __init__(self,domain,family):
        self.domain=domain
        self.family=family
    def __getitem__(self,degree):
        return

class Formspace(Complex):
    def __init__(self,domain,family,degree):
        Complex.__init__(domain,family)
        self.degree=degree
