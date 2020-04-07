"""This module defines the ``Complex`` class,"""
class Complex():
    # family,cell,degree?
   def __init__(self,domain,family):
       self.domain=domain
       self.family=family
       return

       def __getitem__(self,degree):

class Formspace(Complex):
    def __init__(self,degree):
        super().__init__(domain,family)
        self.degree=degree
