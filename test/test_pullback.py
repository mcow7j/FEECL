from FEECL import Complex,FormSpace, HarmonicSpace, Domain, Integral,ReferenceCell
from FEECL import Form,Wedge,ExteriorDerivative,HodgeStar,Argument,BasisForm,Coefficient,Constant,Pullback
from FEECL import wedge,d,hodgestar,vol,inner,volform,trialfunction,simplify,pullback


def test_pullback():

    domain = Domain(3,3)
    complex_1 = Complex(domain,'P-',1)
    space = FormSpace(complex_1,0)
    Hspace = HarmonicSpace(complex_1,0)
    ref=ReferenceCell(domain)

    f = Coefficient(space)
    p = Coefficient(Hspace)
    u = trialfunction(space)
    v = Argument(space,0)
    kappa = Constant(1)

    g1=wedge(kappa,d(u))
    a = inner(wedge(kappa,d(u)),d(v))
    L = inner((f-p),u)

    w=pullback(a)
    w1=pullback(g1)

    w2=simplify(w)
    w3=simplify(w1)

    assert w1.domain==domain and w.integrand.degree==3 and w.domain==ref

def test_simplifiy():

    domain = Domain(3,3)
    complex_1 = Complex(domain,'P-',1)
    space = FormSpace(complex_1,0)
    Hspace = HarmonicSpace(complex_1,0)
    ref=ReferenceCell(domain)

    f = Coefficient(space)
    p = Coefficient(Hspace)
    u = trialfunction(space)
    v = Argument(space,0)
    kappa = Constant(1)

    g1=wedge(kappa,d(u))
    a = inner(wedge(kappa,d(u)),d(v))
    L = inner((f-p),u)

    w=pullback(a)
    w1=pullback(g1)

    w2=simplify(w)
    w3=simplify(w1)

    assert w3.domain==domain and w2.integrand.degree==3 and w2.domain==ref
