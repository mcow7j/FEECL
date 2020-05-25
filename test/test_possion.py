from FEECL import Wedge, ExteriorDerivative, HodgeStar
from FEECL import Argument,BasisForm,Coefficent,Constant
from FEECL import Complex,FormSpace, HarmonicSpace
from FEECL import Domain
from FEECL import Integral
from FEECL import wedge,d,hodgestar,vol,inner,volform


def test_form():

    domain = Domain(3,3)
    complex = Complex(domain,'P-',2)
    space = FormSpace(complex,1)

    G = Coefficent(space)
    u = Argument(space,1)

    a = Integral(wedge(wedge(d(u),Constant(3)),G))

    assert False #something


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

    assert False #something
