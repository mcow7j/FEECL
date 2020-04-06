"""This module defines the ``Expr`` class, the superclass
for all expression tree node types in FEECL.
"""

class Expr(object):
    """base class for all feecl objects
    """

    def __init__(self,degree,domain):
        self.degree=degree
        self.domain=domain

    def getdegree(self):
        return ("The degree is: {}".format(self.degree))

    def getdomain(self):
        return ("The degree is: {}".format(self.domain))

#    def __str__(self):
#        "Return pretty print string representation of this object."
#        return ("{}".format(self))

#    def __repr__(self):
#        "Return a short string to represent this Expr in an error message."
#        return ("{}".format(self,self.degree,self.domain))

    def __add__(self,other):
        raise NotImplementedError

    def __radd__(self):
        raise NotImplementedError

    def __pos__(self):
        raise NotImplementedError

    def __neg__(self):
        raise NotImplementedError
