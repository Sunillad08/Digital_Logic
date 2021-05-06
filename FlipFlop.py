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
from Gates import *

'''Nor latch'''
def latch_nor(s , r , q , clock):

    # to check input is int or float only!
    if (valid_value(s , r , q , clock)):

        # normalizing values
        s , r ,clock = normalize_logic_values(s, r, clock)

        # checking clock pulse
        if clock == 0:
            return q
        else:
            '''NOR Latch main logic : -1 means last stage and None for race around condition'''
            if s == 0 :
                if r == 0:
                    return q # last state
                else:
                    return 0 # 0
            else:
                if r == 0:
                    return 1 # 1
                else:
                    return -1 # race around

    # raising ValueError
    else:
        raise ValueError("Invalid Values!")

'''Nand latch'''        
def latch_nand(s , r , q , clock):

    # to check input is int or float only!
    if (valid_value(s , r , q , clock)):

        # normalizing values
        s , r ,clock = normalize_logic_values(s, r, clock)

        # checking clock pulse
        if clock == 0:
            return q
        else:
            '''NAND Latch main logic : -1 means last stage and None for race around condition'''
            if s == 0 :
                if r == 0:
                    return -1 # race around
                else:
                    return 1 # 0
            else:
                if r == 0:
                    return 0 # 1
                else:
                    return q # last state

    # raising ValueError
    else:
        raise ValueError("Invalid Values!")
                
'''SR flip flop'''        
def flip_flop_sr(s , r , q , clock , active = "high"):
    if (valid_value(s , r , q , clock)):
        '''Since Active High SR latch is same as nor latch'''
        if active.lower() == "high":
            return latch_nor(s , r , q , clock) # SR latch logic
        
            '''Since Active Low SR latch is same as nand latch'''
        elif active.lower() == "low":
            return latch_nand( s , r , q , clock) #S'R' logic
        else:
            raise SyntaxError("Unknown Mode")
    else:
        ValueError("Invalid Values!")

'''D flip flop''' 
def flip_flop_d(d , q , clock):
    if (valid_value(d , clock)):
        '''D flip flop implementation using sr flip flop'''
        d , q , clock = normalize_logic_values(d , q , clock) # normalizing values
        return flip_flop_sr(d , not(d) , q , clock , active="high") # D flip-flop from SR flip flop
              
    # raising ValueError
    else:
        raise ValueError("Invalid Values!")

'''T flip flop''' 
def flip_flop_t(t , q , clock):
    if (valid_value(t , q , clock)):
        '''T flip flop implementation using D flip flop'''
        t , q ,clock = normalize_logic_values(t , q ,clock) # normalizing values
        t = logic_xor(t , q)
        return flip_flop_d(t , q , clock) # t flip-flop from d flip flop
     
    # raising ValueError
    else:
        raise ValueError("Invalid Values!")

'''JK Normal and master slave flip flop''' 
def flip_flop_jk(j , k , q , clock , master_slave = False):
    if (valid_value(j , k , q , clock)):
        '''Same logic as SR flip flop'''
        # master slave configuration
        if master_slave :
            output = flip_flop_jk(j , k , q , clock) # calling self without master slave config
            if output == -1:
                return int(not(q))
            else:
                return output
        # normal JK flip flop
        else:
            return flip_flop_sr(j , k , q , clock , active="high")
    
    # raising ValueError
    else:
        raise ValueError("Invalid Values!")
        
    
if __name__ == "__main__":

    def check_possible_combinations2(func):
        print("Clock : 0 , q : 1")
        print(func(0 , 0 , 0 ))
        print(func(0 , 0 , 0 ))
        print(func(1 , 0 , 0 ))
        print(func(1 , 0 , 0 ))
        print("Clock : 0 , q : 1")
        print(func(0 , 1 , 0 ))
        print(func(0 , 1 , 0 ))
        print(func(1 , 1 , 0 ))
        print(func(1 , 1 , 0 ))
        print("Clock : 1 , q : 0")
        print(func(0 , 0 , 1 ))
        print(func(0 , 0 , 1 ))
        print(func(1 , 0 , 1 ))
        print(func(1 , 0 , 1 ))
        print("Clock : 1 , q : 1")
        print(func(0 , 1 , 1 ))
        print(func(0 , 1 , 1 ))
        print(func(1 , 1 , 1 ))
        print(func(1 , 1 , 1 ))
        print(f"Ended checking {func.__name__}\n")
    
    def check_possible_combinations3(func):
        print("Clock : 0 , q : 0")
        print(func(0 , 0 , 0 , 0 , master_slave=True))
        print(func(0 , 1 , 0 , 0 , master_slave=True))
        print(func(1 , 0 , 0 , 0 , master_slave=True))
        print(func(1 , 1 , 0 , 0 , master_slave=True))
        print("Clock : 0 , q : 1")
        print(func(0 , 0 , 1 , 0 , master_slave=True))
        print(func(0 , 1 , 1 , 0 , master_slave=True))
        print(func(1 , 0 , 1 , 0 , master_slave=True))
        print(func(1 , 1 , 1 , 0 , master_slave=True))
        print("Clock : 1 , q : 0")
        print(func(0 , 0 , 0 , 1 , master_slave=True))
        print(func(0 , 1 , 0 , 1 , master_slave=True))
        print(func(1 , 0 , 0 , 1 , master_slave=True))
        print(func(1 , 1 , 0 , 1 , master_slave=True))
        print("Clock : 1 , q : 1")
        print(func(0 , 0 , 1 , 1 , master_slave=True))
        print(func(0 , 1 , 1 , 1 , master_slave=True))
        print(func(1 , 0 , 1 , 1 , master_slave=True))
        print(func(1 , 1 , 1 , 1 , master_slave=True))
        print(f"Ended checking {func.__name__}\n")

    #check_possible_combinations3(flip_flop_jk)
    check_possible_combinations2(flip_flop_t)
    #check_possible_combinations(latch_nand)
    #check_possible_combinations(flip_flop_jk)
