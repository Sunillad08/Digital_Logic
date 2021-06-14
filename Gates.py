'''
gates\n
type:function\n
name-format: logic_[name]\n
AND\n
OR\n
NOT\n
NAND\n
NOR\n
XOR\n
XNOR
'''

from main_functions import *

'''Logic AND'''
def logic_and(val1, val2):
  if valid_value(val1,val2):      
    val1 , val2 = normalize_logic_values(val1, val2) 
    return(val1 and val2)
  else:
    raise ValueError("Invalid Values!")

'''Logic OR'''
def logic_or(val1, val2):
  if valid_value(val1,val2):      
    val1 , val2 = normalize_logic_values(val1, val2)    
    return(val1 or val2)
  else:
    raise ValueError("Invalid Values!")

'''Logic NOT'''
def logic_not(val):
  if valid_value(val):      
    val = normalize_logic_values(val)[0]
    print(val)
    if val == 1:
      return 0
    else:
      return 1
  else:
    raise ValueError("Invalid Values!")

'''Logic NAND'''
def logic_nand(val1, val2):
  return logic_not(logic_and(val1, val2))

'''Logic NOR'''
def logic_nor(val1, val2):
  return logic_not(logic_or(val1, val2))

'''Logic XOR'''
def logic_xor(val1, val2):
  cp1 = logic_and(val1, logic_not(val2))
  cp2 = logic_and(logic_not(val1), val2)
  return(logic_or(cp1, cp2))

'''Logic XNOR'''
def logic_xnor(val1, val2):
  cp1 = logic_nor(val1, val2)
  cp2 = logic_and(val1, val2)
  return(logic_or(cp1, cp2)) 
