"""This module defines the ``Complex`` class,"""
class Complex():
    # family,cell,degree?
   def __init__(self,family,domain):
       self.family=family
       self.domain=domain
       return

       def __getitem__(self,degree):
