from FEECL import Complex,FormSpace, HarmonicSpace, Domain, Integral
from FEECL import Wedge,ExteriorDerivative,HodgeStar,Argument,BasisForm,Coefficient,Constant,Sum
from FEECL import wedge,d,hodgestar

def test_wedge_constant():
    f = Constant(1.0)
    g = Constant(2.0)

    w = Wedge(f, g)

    assert w.degree == 0

def test_ext_div_constant():

    f = Constant(1.0)

    w = ExteriorDerivative(f)

    assert w.degree == 1

def test_wedge():

    D=Domain(2,3)
    complex_1=Complex(D,'P-',2)
    space=FormSpace(complex_1,1)

    f=Coefficient(space)
    u=Argument(space,1)
    v=Argument(space,0)

    w=wedge(wedge(u,v),f)

    assert w.degree==3 and w.domain==D

def test_wedge_2():

    D=Domain(2,3)
    complex_1=Complex(D,'P-',2)
    space=FormSpace(complex_1,1)
    space2=FormSpace(complex_1,2)

    f=Coefficient(space2)
    u=Argument(space,1)
    v=Argument(space,0)

    w1=wedge(wedge(u,v),7)
    w2=wedge(w1,f)

    assert w1.degree==2 and w1.domain==D and w2.degree==4

def test_d():

    D=Domain(2,3)
    complex_1=Complex(D,'P-',2)
    space=FormSpace(complex_1,1)
    space2=FormSpace(complex_1,2)

    f=Coefficient(space)
    u=Argument(space,1)
    v=Argument(space2,0)

    w1=d(u)
    w2=d(v)
    w3=d(f)

    assert w1.degree==2 and w1.domain==D and w2.degree==3 and w3.degree==2

def test_d_2():

    D=Domain(2,3)
    complex_1=Complex(D,'P-',2)
    space=FormSpace(complex_1,1)
    space2=FormSpace(complex_1,2)

    f=Coefficient(space2)
    u=Argument(space,1)
    v=Argument(space,0)

    w1=d(wedge(3.45,wedge(u,v)))
    w2=d(wedge(w1,f))

    assert w1.degree==3 and w1.domain==D and w2.degree==6 and w2.domain==D

def test_Sum():

    D=Domain(2,3)
    complex_1=Complex(D,'P-',2)
    space=FormSpace(complex_1,1)
    space2=FormSpace(complex_1,2)

    f=Coefficient(space2)
    u=Argument(space,1)
    v=Argument(space,0)

    w=Sum(u,v)
    w1=Sum(w,f)

    assert w.degree==1 and w.domain==D and w1.degree==1 and w1.domain==D

def test_forms():

    D=Domain(2,3)
    complex_1=Complex(D,'P-',2)
    space=FormSpace(complex_1,1)

    f=Coefficient(space)
    u=Argument(space,1)
    v=Argument(space,0)

    w=u+v
    w1=f+w
    w2=w1-v

    assert w2.degree==1 and w2.domain==D

def test_ints_with_forms():

    D=Domain(2,3)
    complex_1=Complex(D,'P-',2)
    space=FormSpace(complex_1,0)

    f=Coefficient(space)
    u=Argument(space,1)
    v=Argument(space,0)

    w=u+1
    w1=w-v
    w2=w1-f
    w3=w2-5

    assert w3.domain==D and w3.degree==0
