from FEECL import Constant, Wedge, ExteriorDerivative

def test_wedge_constant():
    f = Constant(1.0)
    g = Constant(2.0)

    L = Wedge(f,g)

    assert str(L) == '(1.0∧2.0)'

def test_wedge_and_ext_deriv():

    f = Constant(5.0)
    g = Constant(7)
    w = Constant(8)
    L = Wedge(Wedge(f,g),w)
    G = ExteriorDerivative(f)
    F = Wedge(L,G)
    assert str(F) == '(((5.0∧7)∧8)∧d(5.0))'
