"""module for all key functions"""
#from .form import Form
#from .operator import Wedge, ExteriorDerivative, HodgeStar
#from .terminal import Argument,BasisForm,Coefficent,Constant
from .core import Operator,Terminal,Form
from .core import Wedge,ExteriorDerivative,HodgeStar,Argument,BasisForm,Coefficient,Constant,Pullback
from .complex import Complex,FormSpace,HarmonicSpace
from .domain import Domain,ReferenceCell
from .integral import Integral

from numbers import Number
from functools import reduce


def as_form(value):
    if isinstance(value,Form):
        return value
    elif isinstance(value,Number):
        return Constant(value)
    else:
        raise TypeError("cannot convert {} to form".format(type(value)))

#wedge
def wedge(a,b):
    a=as_form(a)
    b=as_form(b)
    #remove mul in terminal if this wrong
    if isinstance(a, Constant) and isinstance(b, Constant):
        return a*b
    if a.domain != b.domain and None not in (a.domain,b.domain) :
        raise ValueError("operands missmatched domains")
    return Wedge(a,b)

#outline for d function
def d(a):
    a=as_form(a)
    return ExteriorDerivative(a)

def hodgestar(a):
    a=as_form(a)
    return HodgeStar(a)

def volform(domain):
    return reduce(wedge, (BasisForm(domain,i) for i in range(domain.topological_dim)))

def inner(a,b):
    return Integral(wedge(a,hodgestar(b)))

def trialfunction(space):
    return Argument(space,1)

def testfunction(space):
    return Argument(space,0)

def pullback(a):
    if isinstance(a,Integral):
        return Integral(Pullback(a.integrand),ReferenceCell(a.domain))
    else:
        a=as_form(a)
        return Pullback(a)

def simplify(a):
    if isinstance(a,Integral):
        return Integral(simplify_pullback(a.integrand),a.domain)
    else:
        a=as_form(a)
        return simplify_pullback(a)

def simplify_pullback(a):

    processed_dict={}
    processing_stack=[a]

    while processing_stack:
      item=processing_stack.pop()
      if repr(item) in processed_dict:
          continue
      if isinstance(item,Pullback):
        o=item.operands[0]
        if isinstance(o,Terminal):
            processed_dict[repr(item)]=item
        elif isinstance(o,Operator):
            processedchildren=[]
            toprocess=[]
            for grandchild in o.operands:
                pchild=processed_dict.get(repr(Pullback(grandchild)),None)
                if pchild:
                    processedchildren.append(pchild)
                else:
                    toprocess.append(Pullback(grandchild))
            if toprocess:
                processing_stack.append(item)
                processing_stack+=toprocess
            else:
                processed_dict[repr(item)]=o.__class__(*processedchildren)
      else:
          processedchildren=[]
          toprocess=[]
          for child in item.operands:
              pchild=dict1.get(repr(child),None)
              if pchild:
                  processedchildren.append(pchild)
              else:
                  toprocess.append(child)
          if toprocess:
              processing_stack.append(item)
              processing_stack+=toprocess
          else:
              processed_dict[repr(item)]=item.__class__(*processedchildren)

    return processed_dict[repr(a)]
