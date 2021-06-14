'''
arithematic_circuit\n
type:function | class\n
name-format: [name]\n
half adder\n
full adder\n
half subtractor\n
full subtractor\n
comparator
'''

from LogicPy.main_functions import *
from LogicPy.gates import *

'''Half adder'''
def half_adder(val1,val2):
    if(valid_value(val1,val2)):
        val1,val2 = normalize_logic_values(val1,val2)
        sum_ha = logic_xor(val1,val2)
        carry_ha = logic_and(val1,val2)
        return(sum_ha,carry_ha)
    else:
        raise ValueError("Invalid Values!")

'''Full adder'''
def full_adder(val1,val2,carry_in = 0):
    sum_ha, carry_ha = half_adder(val1,val2)[0],half_adder(val1,val2)[1]
    sum_fa = logic_xor(sum_ha,carry_in)
    carry_fa = logic_or(logic_and(sum_ha,carry_in),carry_ha)
    return(sum_fa,carry_fa)

'''Half subtractor'''
def half_subtractor(val1,val2):
    if(valid_value(val1,val2)):
        val1,val2 = normalize_logic_values(val1,val2)
        diff_hs = logic_xor(val1,val2)
        borrow_hs = logic_and(logic_not(val1),val2)
        return(diff_hs,borrow_hs)
    else:
        raise ValueError("Invalid Values!")

'''Full subtractor'''
def full_subtractor(val1,val2,borrow_in = 0):
    diff_hs, borrow_hs = half_subtractor(val1,val2)[0], half_subtractor(val1,val2)[1]
    diff_fs = logic_xor(diff_hs, borrow_in)
    borrow_fs = logic_or(logic_and(logic_not(diff_hs),borrow_in),borrow_hs)
    return(diff_fs,borrow_fs)

'''Comparator'''
class comparator():
                    
    def __init__(self, level,inputno = None):
        self.level = level
        self.inputno = inputno
        self.__output_pins_count = 3
        
    def comparator_input(self, inputno):
        #For list input
        if isinstance(inputno , list):
            # nested lists required for bit combinations
            if len(inputno) == 2:
                for i in inputno:
                    # binary only
                    if isinstance(i , list):
                        for j in i:
                            if j not in [0,1]:
                                raise ValueError("Invalid value datatype for input pins")
                            
                    else:
                        raise ValueError("Input every bit combination in a list")       
                    
                for each in inputno:
                    if len(each) != self.level:
                        if len(each) > self.level:
                            if(all(each[0:len(each) - self.level]) != 0):
                                raise ValueError(f"Input value of input {inputno.index(each) + 1} is large")    

            else:
                raise ValueError("Input list must have only two values")
        
        else:
            raise ValueError("Input must be a list datatype")
        
        self.inputno = inputno
        
        
    def A_gt_B(self):
        if(int("".join(str(bit) for bit in self.inputno[0]),2) > int("".join(str(bit) for bit in self.inputno[1]),2)):
            return(1)
        else: return 0
        
    def A_eq_B(self):
        if(int("".join(str(bit) for bit in self.inputno[0]),2) == int("".join(str(bit) for bit in self.inputno[1]),2)):
            return(1)
        else: return 0
        
    def A_ls_B(self):
        if(int("".join(str(bit) for bit in self.inputno[0]),2) < int("".join(str(bit) for bit in self.inputno[1]),2)):
            return(1)
        else: return 0

      


    
    
    
        
