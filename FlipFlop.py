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
def nor_latch(s , r , clock):

    # to check input is int or float only!
    if (isinstance(s , int) or isinstance(s , float)) and (isinstance(r , int) or isinstance(r , float)) and (isinstance(clock , int) or isinstance(clock , float)):

        # normalizing values
        s , r ,clock = normalize_logic_values(s, r, clock)

        # checking clock pulse
        if clock == 0:
            return -1
        else:
            '''NOR Latch main logic : -1 means last stage and None for race around condition'''
            if s == 0 :
                if r == 0:
                    return -1 # last state
                else:
                    return 0 # 0
            else:
                if r == 0:
                    return 1 # 1
                else:
                    return None # race around

    # raising ValueError
    else:
        raise ValueError("Invalid Values!")

'''Nand latch'''        
def nand_latch(s , r , clock):

    # to check input is int or float only!
    if (isinstance(s , int) or isinstance(s , float)) and (isinstance(r , int) or isinstance(r , float)) and (isinstance(clock , int) or isinstance(clock , float)):

        # normalizing values
        s , r ,clock = normalize_logic_values(s, r, clock)

        # checking clock pulse
        if clock == 0:
            return -1
        else:
            '''NAND Latch main logic : -1 means last stage and None for race around condition'''
            if s == 0 :
                if r == 0:
                    return None # race around
                else:
                    return 1 # 0
            else:
                if r == 0:
                    return 0 # 1
                else:
                    return -1 # last state

    # raising ValueError
    else:
        raise ValueError("Invalid Values!")
                
'''SR flip flop'''        
def sr_flip_flop(s , r , clock , active = "high"):
    if (isinstance(s , int) or isinstance(s , float)) and (isinstance(r , int) or isinstance(r , float)) and (isinstance(clock , int) or isinstance(clock , float)):
        '''Since Active High SR latch is same as nor latch'''
        if active.lower() == "high":
            return nor_latch(s , r , clock) # SR latch logic
        
            '''Since Active Low SR latch is same as nand latch'''
        elif active.lower() == "low":
            return nand_latch( s , r , clock) #S'R' logic
    else:
        raise SyntaxError("UnknownMode")

'''D flip flop''' 
def d_flip_flop(d , clock):
    if (isinstance(d , int) or isinstance(d , float)) and (isinstance(clock , int) or isinstance(clock , float)):
        '''D flip flop implementation using sr flip flop'''
        d ,clock = normalize_logic_values(d ,clock) # normalizing values
        return sr_flip_flop(d , not(d) , clock) # D flip-flop from SR flip flop
              
    # raising ValueError
    else:
        raise ValueError("Invalid Values!")

'''T flip flop''' 
def t_flip_flop(t , q , clock):
    if (isinstance(t , int) or isinstance(t , float)) and (isinstance(q , int) or isinstance(q , float)) and (isinstance(clock , int) or isinstance(clock , float)):
        '''T flip flop implementation using D flip flop'''
        t , q ,clock = normalize_logic_values(t , q ,clock) # normalizing values
        t = logic_xor(t , q)
        return d_flip_flop(t , clock) # t flip-flop from d flip flop
     
    # raising ValueError
    else:
        raise ValueError("Invalid Values!")

'''JK flip flop''' 
def jk_flip_flop(j , k , clock):
    if (isinstance(j , int) or isinstance( j, float)) and (isinstance(k , int) or isinstance(k , float)) and (isinstance(clock , int) or isinstance(clock , float)):
        '''Same logic as SR flip flop'''
        return sr_flip_flop(j , k , clock , active="high")
    
    # raising ValueError
    else:
        raise ValueError("Invalid Values!")
    
'''Master slave JK flip flop''' 
def jk_master_flip_flop(j , k , clock):
    if (isinstance(j , int) or isinstance( j, float)) and (isinstance(k , int) or isinstance(k , float)) and (isinstance(clock , int) or isinstance(clock , float)):
        '''Same logic as SR flip flop'''
        output = jk_flip_flop(j , k , clock)
        if output == None:
            return '-1 Q Complement'
        else:
            return output
    # raising ValueError
    else:
        raise ValueError("Invalid Values!")
        
    
if __name__ == "__main__":

    def check_possible_combinations(func):
        print("Clock : 0")
        print(func(0 , 0 , 0 ))
        print(func(0 , 1 , 0 ))
        print(func(1 , 0 , 0 ))
        print(func(1 , 1 , 0 ))
        print("Clock : 1")
        print(func(0 ,  0 , 1 ))
        print(func(0 ,  1 , 1 ))
        print(func(1 ,  0 , 1 ))
        print(func(1 ,  1 , 1 ))
        print(f"Ended checking {func.__name__}\n")
    
    #check_possible_combinations(nor_latch)
    #check_possible_combinations(nand_latch)
    check_possible_combinations(jk_master_flip_flop)