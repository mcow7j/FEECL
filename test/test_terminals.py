from FEECL import Complex,FormSpace, HarmonicSpace, Domain, Integral
from FEECL import Constant, Wedge,ExteriorDerivative,HodgeStar,Argument,BasisForm,Coefficient,Constant

def test_argument():

    D=Domain(2,3)
    complex_1=Complex(D,'P-',2)
    space=FormSpace(complex_1,1)

    f=Argument(space,1)
    g=Argument(space,0)


    assert f.degree==1 and g.degree==1 and f.domain==D


def test_coefficient():

    D=Domain(2,3)
    complex_1=Complex(D,'P-',2)
    space=FormSpace(complex_1,1)

    f=Coefficient(space)

    assert f.degree==1 and f.domain==D


def test_basis():

    D=Domain(2,3)

    f=BasisForm(D)

    assert f.degree==1 and f.domain==D

def test_constant():

    D=Domain(2,3)
    g=Constant(5)
    k=Constant(2.5,D)
    f=g*k

    assert f.degree==0 and f.domain==D and f.value==12.5
