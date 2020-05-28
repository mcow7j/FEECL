from FEECL import Complex,FormSpace, HarmonicSpace, Domain, Integral
from FEECL import Wedge,ExteriorDerivative,HodgeStar,Argument,BasisForm,Coefficient,Constant
from FEECL import wedge,d,hodgestar,vol,inner,trialfunction,testfunction

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

def test_possion():

    domain = Domain(3,3)
    complex_1 = Complex(domain,'P-',1)
    space = FormSpace(complex_1,0)
    Hspace = HarmonicSpace(complex_1,0)

    f = Coefficient(space)
    p = Coefficient(Hspace)
    u = trialfunction(space)
    v = testfunction(space)
    kappa = Constant(1)

    a = inner(wedge(kappa,d(u)),d(v))
    L = inner((f-p),u)

    print(repr(a))
    print(repr(L))
    assert False
