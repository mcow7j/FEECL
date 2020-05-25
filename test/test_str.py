from FEECL import Constant, Wedge, ExteriorDerivative, Domain, Complex, FormSpace, HarmonicSpace, Coefficent, Argument, inner, wedge, d

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

def test_possion():

    domain = Domain(3,3)
    complex_1 = Complex(domain,'P-',1)
    space = FormSpace(complex_1,0)
    Hspace = HarmonicSpace(complex_1,0)

    f = Coefficent(space)
    p = Coefficent(Hspace)
    u = Argument(space,1)
    v = Argument(space,0)
    kappa = Constant(1)

    a = inner(wedge(kappa,d(u)),d(v))
    L = inner((f-p),u)

    assert False  
