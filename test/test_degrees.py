from FEECL import Constant, Wedge, Ext_div

def test_wedge_constant():
    f = Constant(1.0)
    g = Constant(2.0)

    w = Wedge(f, g)

    assert w.degree == 0

def test_ext_div_constant():

    f = Constant(1.0)

    w = Ext_div(f)

    assert w.degree == 1
