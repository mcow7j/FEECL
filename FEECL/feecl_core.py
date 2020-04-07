"""module for all key functions"""
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
