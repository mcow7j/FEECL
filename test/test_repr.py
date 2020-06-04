from FEECL import Complex,FormSpace, HarmonicSpace, Domain, Integral
from FEECL import Wedge,ExteriorDerivative,HodgeStar,Argument,BasisForm,Coefficient,Constant
from FEECL import wedge,d,hodgestar,inner,trialfunction

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

def test_possion_repr():

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


    assert repr(a)== 'Integral(Wedge(Wedge(Constant(1),ExteriorDerivative(Argument(FormSpace(Complex(Domain(3,3),"P-",1),0),1))),HodgeStar(ExteriorDerivative(Argument(FormSpace(Complex(Domain(3,3),"P-",1),0),0)))),Domain(3,3))' \
    and repr(L)== 'Integral(Wedge(Sum(Wedge(Constant(-1),Coefficient(FormSpace(Complex(Domain(3,3),"P-",1),0))),Coefficient(HarmonicSpace(Complex(Domain(3,3),"P-",1),0))),HodgeStar(Argument(FormSpace(Complex(Domain(3,3),"P-",1),0),1))),Domain(3,3))'
