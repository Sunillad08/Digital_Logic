## Designing flip flop logic for 
'''
1. NOR Latch
2. NAND latch
3. SR flip flop
4. D flip flop
5. JK flip flop
6. Master slave JK flip flop
7. T flip flop
'''

# format to define functions

'''
define function(Input1 , Input2 , clock)
Input1 and Input2 : *args
clock : *args should have same length as Inputs
return output in list/tuple (decide!)
'''

'''
Normalize values above 1 to 1 and below 1 to 0
'''

from main_functions import *


def nor_latch(s , r , clock):
    if (isinstance(s , int) or isinstance(s , float)) and (isinstance(r , int) or isinstance(r , float)) and (isinstance(clock , int) or isinstance(clock , float)):
        s , r ,clock = normalize_logic_values(s, r, clock)
        if clock == 0:
            return -1
        else:
            if s == 0 :
                if r == 0:
                    return None
                else:
                    return 0
            else:
                if r == 0:
                    return 1
                else:
                    return -1
    else:
        raise ValueError("Invalid Values!")
        
        
if __name__ == "__main__":
    print(nor_latch(1,0,0))
    print(nor_latch(1 , 1, 0))
