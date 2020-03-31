

#operator is subclass of expr
from expr_feecl import Expr


class Operator(Expr):
    def __init__(self):
        Expr.__init__(self)

    def _wedge(self,b):
        if self.domain != b.domain:
            return AttributeError:
        return (self.degree=self.degree+b.degree)

class Wedge(Operator):
