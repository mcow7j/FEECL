from FEECL import Complex,FormSpace, HarmonicSpace, Domain, Integral
from FEECL import Wedge,ExteriorDerivative,HodgeStar,Argument,BasisForm,Coefficient,Constant
from FEECL import wedge,d,hodgestar,vol,inner,volform,trialfunction


def test_possion():

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

    assert L.domain==domain and L.integrand.degree==3 and a.integrand.degree==3
