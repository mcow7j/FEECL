from FEECL import Complex,FormSpace, HarmonicSpace, Domain, Integral
from FEECL import Wedge,ExteriorDerivative,HodgeStar,Argument,BasisForm,Coefficient,Constant
from FEECL import wedge,d,hodgestar,inner,volform,trialfunction

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

def test_possion_str():

    domain = Domain(3,3)
    complex_1 = Complex(domain,'P-',1)
    space = FormSpace(complex_1,0)
    Hspace = HarmonicSpace(complex_1,0)

    f = Coefficient(space)
    p = Coefficient(Hspace)
    u = trialfunction(space)
    v = Argument(space,0)
    kappa = Constant(1)

    a = inner(wedge(kappa,d(u)),d(v))
    L = inner((f-p),u)

    print("This test will fail if all tests are run, due to string numbers changing, use command py.test.exe test_str.py to check")
    assert (str(a)== "∫Ω₁{(((-1∧W₀)+W₁)∧*(U))}" or str(a)=="\u222b\u03a9\u2081{((1\u2227d(U))\u2227*(d(V)))}" or str(a)=="\u222b\u03a9\u2081\u2087{((1\u2227d(U))\u2227*(d(V)))}" ) and (str(L) == "∫Ω₁{(((-1∧W₀)+W₁)∧*(U))}" or str(L) == "\u222b\u03a9\u2081{(((-1\u2227W\u2080)+W\u2081)\u2227*(U))}" or str(L)=="\u222b\u03a9\u2081\u2087{(((-1\u2227W\u2081\u2082)+W\u2081\u2083)\u2227*(U))}")
