from FEECL import Complex,FormSpace, HarmonicSpace, Domain, Integral
from FEECL import Constant, Wedge,ExteriorDerivative,HodgeStar,Argument,BasisForm,Coefficient,Constant

def test_domain():

    D=Domain(3,3)
    D1=Domain(3,3)

    assert D!=D1 and D==D


def test_integral_1():

    domain = Domain(3,3)
    complex = Complex(domain,'P-',2)
    space = FormSpace(complex,1)

    G = Coefficent(space)
    u = Argument(space,1)

    form=wedge(wedge(d(u),Constant(3)),G)
    a = Integral(form)

    assert a.Domain==domain and a.integrand==form
