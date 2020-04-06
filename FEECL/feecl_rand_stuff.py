#rough outline of files needed
from expr_feecl import expr
from operator_feecl import operands
from terminal_feecl import terminal
from complex_feecl import complex


#outline for wedge function
def wedge(a,b):
    try:
        w=a._wedge(b)
    except AttributeError:
        w=NotImplemented
    if w is NotImplemented:
        try:
        w=b._rwedge(a):
        except AttributeError:
            w=NotImplemented
    if w is NotImplemented:
        raise NotImplementedError("Cannot wedge %s and %s" %(a,b))
    return w

#outline for d function
def d(a):
    return w


#old stuff from ufl
    # --- Basic object behaviour ---

def __getnewargs__(self):
"""The tuple returned here is passed to as args to cls.__new__(cls, *args).

This implementation passes the operands, which is () for terminals.

May be necessary to override if __new__ is implemented in a subclass.
"""
return #self.ufl_operands






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

def __pos__(self):
    "Unary + is a no-op."
    return self
