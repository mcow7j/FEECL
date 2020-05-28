from FEECL import Complex,FormSpace, HarmonicSpace, Domain, Integral
from FEECL import Wedge,ExteriorDerivative,HodgeStar,Argument,BasisForm,Coefficient,Constant


def test_domain_and_complex():

    D=Domain(3,3)
    complex_1=Complex(D,'P-',2)

    assert D!=complex_1

def test_complex():

    D=Domain(2,3)
    complex_1=Complex(D,'P-',2)
    complex_2=Complex(D,'P-',2)
    complex_3=Complex(D,'P',2)
    complex_4=Complex(D,'P',1)

    assert complex_1!=complex_2 and complex_2!=complex_3 and complex_4!=complex_3

def test_space():
    D=Domain(2,3)
    complex_1=Complex(D,'P-',2)

    space1=FormSpace(complex_1,1)
    space2=complex_1[1]
    space3=FormSpace(complex_1,0)

    assert space1==space2 and space1!=space3

def test_harmonic_space():
    D=Domain(2,3)
    complex_1=Complex(D,'P-',2)
    complex_2=Complex(D,'P',2)

    space1=HarmonicSpace(complex_1,1)
    space2=HarmonicSpace(complex_1,1)
    space3=HarmonicSpace(complex_2,1)
    space4=HarmonicSpace(complex_1,0)

    assert space1==space2 and space2!=space3 and space3!=space4
