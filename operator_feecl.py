

#operator is subclass of expr
from expr_feecl import Expr


class Operator(Expr):
    def __init__(self):
        Expr.__init__(self)
