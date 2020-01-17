# -*- coding: utf-8 -*-
"""This module defines the ``Expr`` class, the superclass
for all expression tree node types in UFL.

NB! A note about other operators not implemented here:

More operators (special functions) on ``Expr`` instances are defined in
``exproperators.py``, as well as the transpose ``A.T`` and spatial derivative
``a.dx(i)``.
This is to avoid circular dependencies between ``Expr`` and its subclasses.
"""


# --- The base object for all UFL expression tree nodes ---

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

    def __str__(self):

    def __repr__(self):

    def __add__(self,b):

    def __radd__(self):

    def __pos__(self):

    def __neg__(self):





#old stuff
    # --- Basic object behaviour ---

    def __getnewargs__(self):
        """The tuple returned here is passed to as args to cls.__new__(cls, *args).

        This implementation passes the operands, which is () for terminals.

        May be necessary to override if __new__ is implemented in a subclass.
        """
        return #self.ufl_operands

    def __init__(self):
        self._hash = None

    def __del__(self):
        pass





    def evaluate(self, x, mapping, component, index_values):
        """Evaluate expression at given coordinate with given values for terminals."""
        error("Symbolic evaluation of %s not available." % self._ufl_class_.__name__)

    def __float__(self):
        "Try to evaluate as scalar and cast to float."
        try:
            v = float(self._ufl_evaluate_scalar_())
        except Exception:
            v = NotImplemented
        return v

    def __complex__(self):
        "Try to evaluate as scalar and cast to complex."
        try:
            v = complex(self._ufl_evaluate_scalar_())
        except TypeError:
            v = NotImplemented
        return v


    # All subclasses must implement __repr__
    def __repr__(self):
        "Return string representation this object can be reconstructed from."
        raise NotImplementedError(self.__class__.__repr__)

    # All subclasses must implement __str__
    def __str__(self):
        "Return pretty print string representation of this object."
        raise NotImplementedError(self.__class__.__str__)

    # --- Special functions used for processing expressions ---

    def __eq__(self, other):
        """Checks whether the two expressions are represented the
        exact same way. This does not check if the expressions are
        mathematically equal or equivalent! Used by sets and dicts."""
        raise NotImplementedError(self.__class__.__eq__)

    def __iter__(self):
        "Iteration over vector expressions."
        for i in range(len(self)):
            yield self[i]

    def __floordiv__(self, other):
        "UFL does not support integer division."
        raise NotImplementedError(self.__class__.__floordiv__)

    def __pos__(self):
        "Unary + is a no-op."
        return self
