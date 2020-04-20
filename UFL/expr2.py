element = FiniteElement("Lagrange", triangle, 1)

u = TrialFunction(element)
v = TestFunction(element)

f = Coefficent(element)
kappa = Coefficent(element)

A = kappa*inner(grad(u), curl(v))
