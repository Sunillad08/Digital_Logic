## Designing flip flop logic for 
'''
1. AND
2. OR
3. NOT
4. NAND
5. NOR
6. XOR
7. XNOR
'''

# format to define functions

'''
define function(Input1 , Input2 , clock)
Input1 and Input2 : *args
clock : *args should have same length as Inputs
return output in list/tuple (decide!)
'''

from main_functions import *

def logic_and(val1, val2):
  if ((isinstance(val1 , int) or isinstance(val1 , float)) and (isinstance(val2 , int) or isinstance(val2 , float))):      
    normalize_logic_values(val1, val2)    
    return(val1 and val2)
  else:
    raise ValueError("Invalid Values!")

def logic_or(val1, val2):
  if ((isinstance(val1 , int) or isinstance(val1 , float)) and (isinstance(val2 , int) or isinstance(val2 , float))):      
    normalize_logic_values(val1, val2)    
    return(val1 or val2)
  else:
    raise ValueError("Invalid Values!")

def logic_not(val, val2):
  if ((isinstance(val1 , int) or isinstance(val1 , float)) and (isinstance(val2 , int) or isinstance(val2 , float))):      
    normalize_logic_values(val1, val2)    
    return(not(val))
  else:
    raise ValueError("Invalid Values!")

def logic_nand(val1, val2):
  return logic_not(logic_and(val1, val2))
  
if __name__ == "__main__":
    print(logic_and(1,0))
    print(logic_and(1,1))
    print(logic_and(0,1))
    print(logic_and(0,0))
