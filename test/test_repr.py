from FEECL import Constant, Wedge, ExteriorDerivative

def test_wedge_constant():
    f = Constant(1.0)
    g = Constant(2.0)

    L = Wedge(f,g)

    assert repr(L) == 'Wedge(Constant(1.0),Constant(2.0))'

def test_wedge_and_ext_deriv():

    f = Constant(5.0)
    g = Constant(7)
    w = Constant(8)
    L = Wedge(Wedge(f,g),w)
    G = ExteriorDerivative(f)
    F = Wedge(L,G)
    assert repr(F) == 'Wedge(Wedge(Wedge(Constant(5.0),Constant(7)),Constant(8)),ExteriorDerivative(Constant(5.0)))'
