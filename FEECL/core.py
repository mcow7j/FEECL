"""This module defines the ``Expr`` class, the superclass
for all expression tree node types in FEECL.
"""
from numbers import Number

class Form(object):
    """base class for all feecl objects
    """

    def __init__(self,degree,domain):
        self.degree=degree
        self.domain=domain

    def getdegree(self):
        return ("The degree is: {}".format(self.degree))

    def getdomain(self):
        return ("The degree is: {}".format(self.domain))


#check over return/raise
    def __add__(self,other):
        other=as_form(other)
        if self.domain != other.domain and None not in (self.domain,other.domain) :
            raise ValueError("operands missmatched domains")
        if self.degree != other.degree:
            raise ValueError("operands missmatched degrees/not constants")
        return Sum(self,other)

    def __radd__(self,other):
      return Form.__add__(other,self)

    def __pos__(self):
        return self

    def __neg__(self):
        return Wedge(Constant(-1), self)

    def __sub__(self,other):
        return Form.__add__(Wedge(Constant(-1), self),other)

####Terminals##########

class Terminal(Form):
    def __init__(self,degree,domain):
        Form.__init__(self,degree,domain)
        self.operands=()
    def __len__(self):
        return 1
    def __repr__(self):
      attribute_dict=(self.__dict__).copy()
      #delete unwanted info e.g degree
      del attribute_dict['degree'],attribute_dict['domain']
      # This should work for most cases
      r = "%s(%s)" % (self.__class__.__name__, ",".join(str(attribute_dict[i]) for i in attribute_dict))
      return r

### below are the main terminal subclasses in alphebetical order ###

class Argument(Terminal):
    def __init__(self,space,count):
        self.space = space
        super().__init__(space.degree,space.complex.domain)
        if count != 1 and count != 0:
          raise NotImplementedError("Needs to be 1 or 0")
        self.count = count

    def __str__(self):
        if self.count==1:
            return "U"
           # return ("Trial Function")
        else:
           # return ("Test Function")
           return "V"

    def __repr__(self):
        return ("{}({},{})".format(self.__class__.__name__,repr(self.space),self.count))

    def __eq__(self, other):
        if other.__class__.__name__==self.__class__.__name__:
            return self.count == other.count and self.space==other.space
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

class BasisForm(Terminal):
    def __init__(self,domain,index=1):
        Terminal.__init__(self,1,domain)
        #index goes from 1 to topological_dim
        self.index=index

    def __str__(self):
        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        return "dx{}".format(self.index).translate(SUB)

    def __repr__(self):
         return "{}({},{})".format(self.__class__.__name__,repr(self.domain),self.index)

    def __eq__(self, other):
        if other.__class__.__name__==self.__class__.__name__:
            return self.domain==other.domain and self.index==other.index
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


class Coefficient(Terminal):
    def __init__(self,space):
        self.space=space
        super().__init__(self.space.degree,self.space.complex.domain)
        self.count=self._count
        self.__class__._count+=1
    _count=0

    def __str__(self):
        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        return ("W{}".format(self.count)).translate(SUB)

    def __repr__(self):
        return ("{}({})".format(self.__class__.__name__,repr(self.space)))

    def __eq__(self, other):
        if other.__class__.__name__==self.__class__.__name__:
            return self.count == other.count
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


class Constant(Terminal):
    def __init__(self,value,domain=None):
        super().__init__(0,domain)
        self.value=value

    def __str__(self):
        return("{}".format(self.value))

    def __repr__(self):
        return ("{}({})".format(self.__class__.__name__,self.value))

    def __mul__(self,other):
        if isinstance(other, Constant):
            if self.domain != other.domain and None not in (self.domain,other.domain) :
                raise ValueError("operands missmatched domains")
            return Constant(self.value*other.value,self.domain or other.domain)
        else :
            raise ValueError("not possible to multiply try wedge")

    def __rmul__(self,other):
        return self*other

    def __eq__(self, other):
        if other.__class__.__name__==self.__class__.__name__:
            return self.domain==other.domain and self.value==other.value
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

####Operators############

class Operator(Form):
    def __init__(self,degree,domain,operands):
        Form.__init__(self,degree,domain)
        self.operands=operands

    def __len__(self):
        return len(self.operands)


    def __str__(self):
        if len(self.operands)==2:
          return "({}{}{})".format(str(self.operands[0]),self.symbol,str(self.operands[1]))
        elif len(self.operands) == 1:
          return "{}({})".format(self.symbol, str(self.operands[0]))
        else:
          raise NotImplementedError("No string representation for operators with arity greater than 2")

    def __repr__(self):
        "Default repr string construction for operators."
        # This should work for most cases
        if len(self.operands)==1:
          r = "{}({})".format(self.__class__.__name__,repr(self.operands[0]))
        else:
          r = "{}({})".format(self.__class__.__name__,",".join(repr(op) for op in self.operands))
        return r


### main operators in alphebetical order ###

class ExteriorDerivative(Operator):
    def __init__(self,a):
        Operator.__init__(self,a.degree,a.domain,(a,))
        self.symbol = "d"
        self.degree += 1


class HodgeStar(Operator):
    def __init__(self,a):
        Operator.__init__(self,a.domain.topological_dim,a.domain,(a,))
        self.symbol = "*"
        self.degree -= a.degree


class Sum(Operator):
    def __init__(self,a,b):
        Operator.__init__(self,a.degree, a.domain or b.domain,(a,b))
        self.symbol = "+"

class Wedge(Operator):
    def __init__(self,a,b):
        Operator.__init__(self,a.degree,a.domain or b.domain,(a,b))
        self.degree += b.degree
        self.symbol = u'\u2227'

class Contraction(Operator):
    def __init__(self,a,b):
        Operator.__init__(self,a.degree,a.domain,(a,b))
        self.degree -= b.degree
        self.name = "contraction"
        self.symbol= u'\u231F'

class Pullback(Operator):
    def __init__(self,a):
        Operator.__init__(self,a.degree,a.domain,(a,))
        self.symbol = "L*"

#######core function #######

def as_form(value):
    if isinstance(value,Form):
        return value
    elif isinstance(value,Number):
        return Constant(value)
    else:
        raise TypeError("cannot convert {} to form".format(type(value)))
