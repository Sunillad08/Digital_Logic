from main_functions import *
from Gates import *



def half_adder(val1,val2):
    if(valid_value(val1,val2)):
        val1,val2 = normalize_logic_values(val1,val2)
        sum_ha = logic_xor(val1,val2)
        carry_out = logic_and(val1,val2)
        return(sum_ha,carry_ha)
    else:
        raise ValueError("Invalid Values!")

def full_adder(val1,val2,carry_in = 0):
    sum_ha, carry_ha = half_adder(val1,val2)[0],half_adder(val1,val2)[1]
    sum_fa = logic_xor(sum_ha,carry_in)
    carry_fa = logic_or(logic_and(sum_ha,carry_in),carry_ha)
    return(sum_fa,carry_fa)


def half_subtractor(val1,val2):
    if(valid_value(val1,val2)):
        val1,val2 = normalize_logic_values(val1,val2)
        diff_hs = logic_xor(val1,val2)
        borrow_hs = logic_and(logic_not(val1),val2)
        return(diff_hs,borrow_hs)
    else:
        raise ValueError("Invalid Values!")

def full_subtractor(val1,val2,borrow_in = 0):
    diff_hs, borrow_hs = half_subtractor(val1,val2)[0], half_subtractor(val1,val2)[1]
    diff_fs = logic_xor(diff_hs, borrow_in)
    borrow_fs = logic_or(logic_and(logic_not(diff_hs),borrow_in),borrow_hs)
    return(diff_fs,borrow_fs)



        
      


    
    
    
        
