from FEECL import Constant, Wedge

def test_wedge_constant():
    f = Constant(1.0)
    g = Constant(2.0)

    w = Wedge(f, g)

    assert w.degree == 0
