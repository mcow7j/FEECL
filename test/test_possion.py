from FEECL import Wedge, ExteriorDerivative, HodgeStar
from FEECL import Argument,BasisForm,Coefficent,Constant
from FEECL import Complex,Formspace, HarmonicSpace
from FEECL import Domain
from FEECL import Integral
from FEECL import wedge,d,hodgestar,vol,inner,volform

def test_possion():
    
    domain = Domain(3,3)
    complex = Complex(domain,'P-',1)
    space = Formspace(complex,0)
    Hspace = HarmonicSpace(space)

    f = Coefficent(space)
    p = Coefficent(Hspace)
    u = Argument(space,1)
    v = Argument(space,0)

    a = inner(d(u),d(v))
    L = inner((f-p),u)

    assert #something
